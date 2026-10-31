"""Checks every scene: counts, anchor conflict, Kantian twins flip K, scenery twins change nothing, unique case codes."""
import csv, glob, json, os, sys, collections
base = sys.argv[1] if len(sys.argv) > 1 else "expected"
LEVEL_N = {"low": 6, "mid": 12, "high": 20}
ok = True; codes = collections.Counter(); rows_out = []
for d in sorted(glob.glob(base + "/*/")):
    sid = os.path.basename(d.rstrip("/")); level = sid.rsplit("_", 1)[1]
    labs = [json.loads(l) for l in open(d + "labels.jsonl")]
    sc = [json.loads(l) for l in open(d + "scenarios.jsonl")]
    key = list(csv.DictReader(open(d + "key.csv")))
    a = labs[0]; by = {s["changed_variable"].split(":")[0]: l for s, l in zip(sc, labs)}
    gam = [l for s, l in zip(sc, labs) if s["changed_variable"].split(":")[0] in ("weather", "time_of_day", "location") or s["changed_variable"].split(":")[0].endswith("_type")]
    checks = {"count": len(labs) == LEVEL_N[level], "anchor U!=K": a["U"] != a["K"],
              "means twin flips K": by["means"]["K"] != a["K"], "consent twin flips K": by["consent"]["K"] != a["K"],
              "scenery twins change nothing": all((l["U"], l["K"]) == (a["U"], a["K"]) for l in gam)}
    for k in key: codes[k["case"]] += 1
    for k, s, l in zip(key, sc, labs):
        rows_out.append({"scene_id": sid, "scenario_id": l["scenario_id"], "case": k["case"], "changed_variable": s["changed_variable"],
                         "U": l["U"], "K": l["K"], **{f"H_{x}": l["harm"][x] for x in ["brake", "maintain", "swerve_left", "swerve_right", "accelerate"]}})
    bad = [k for k, v in checks.items() if not v]; ok &= not bad
    print(f"{sid:<27} {len(labs):>2} scenarios  U={a['U']:<12} K={a['K']:<9} {'OK' if not bad else 'FAIL ' + ', '.join(bad)}")
dups = [c for c, n in codes.items() if n > 1]; ok &= not dups
# the unified file: every scenario once, every record valid against the v4 schema, every label reproduced by the labeler
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "codebook"))
import jsonschema, labeler as L
schema = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "codebook", "schema_scenario_v4.json")))
data = json.load(open(os.path.join(base, "scenarios.json")))
items = data["scenarios"]; ids = [s["scenario_id"] for s in items]
schema_bad = relabel_bad = 0
for s in items:
    rec = {"scenario_id": s["scenario_id"], **s["record"]}
    try:
        jsonschema.validate(rec, schema)
    except jsonschema.ValidationError:
        schema_bad += 1
    lab = L.label(L.from_json(rec))
    relabel_bad += (lab["utilitarian"]["U_ACTION"], lab["kantian"]["K_ACTION"]) != (s["labels"]["U"], s["labels"]["K"])
file_ok = data["count"] == len(items) == sum(codes.values()) and len(set(ids)) == len(ids) and not schema_bad and not relabel_bad
ok &= file_ok
print(f"scenarios.json: {len(items)} scenarios | duplicate ids: {len(ids) - len(set(ids))} | schema failures: {schema_bad} | label mismatches: {relabel_bad} | {'OK' if file_ok else 'FAIL'}")
print("total scenarios:", sum(codes.values()), "| duplicate case codes:", dups or "none", "|", "ALL CHECKS PASS" if ok else "FAILURES")
with open(os.path.join(base, "ALL_expected_labels.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0])); w.writeheader(); w.writerows(rows_out)
sys.exit(0 if ok else 1)
