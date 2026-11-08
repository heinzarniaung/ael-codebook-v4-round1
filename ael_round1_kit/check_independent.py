"""Independent check of scenarios.json against Codebook v4, using only the standard library.

Usage:  python check_independent.py out/scenarios.json

Does not import labeler, reference_pipeline or anything else from the repository.
Prints one line per check (A-G), then the total, and exits 0 only if there are no problems.
"""
import json
import sys
from collections import Counter, defaultdict

# Codebook v4 constants
WEIGHTS = {"fatal": 1.0, "serious": 0.06, "minor": 0.02, "possible": 0.01, "property": 0.001}
TAU = 0.01
ACTIONS = ["brake", "maintain", "swerve_left", "swerve_right", "accelerate"]
NAMES = {"brake": "Brake", "maintain": "Maintain course", "swerve_left": "Swerve left",
         "swerve_right": "Swerve right", "accelerate": "Accelerate"}
HARM_TOL = 0.000001
FLOAT_EPS = 1e-12  # guards the tau band against float rounding only

EXPECTED_LEVELS = {"low": 36, "mid": 72, "high": 120}
EXPECTED_BINS = {"anchor": 18, "alpha": 36, "harm": 102, "gamma": 72}


def possible(s):
    return [a for a in ACTIONS if s["record"]["feasible_actions"].get(a)]


def computed_harm(s, a):
    total = 0.0
    for party in s["record"]["outcomes"][a]["affected_parties"]:
        for sev, p in party["severity_distribution"].items():
            total += WEIGHTS[sev] * p
    return total


def check_counts(d, scen):
    bad = []
    if d.get("count") != len(scen):
        bad.append(f"count={d.get('count')}!=len={len(scen)}")
    ids = Counter(s["scenario_id"] for s in scen)
    bad += [sid for sid, n in ids.items() if n > 1]
    levels = Counter(s.get("level") for s in scen)
    for lv, n in EXPECTED_LEVELS.items():
        if levels.get(lv, 0) != n:
            bad.append(f"level {lv}={levels.get(lv, 0)}!={n}")
    for lv in levels:
        if lv not in EXPECTED_LEVELS:
            bad.append(f"unexpected level {lv}")
    bins = Counter(s.get("bin") for s in scen)
    for b, n in EXPECTED_BINS.items():
        if bins.get(b, 0) != n:
            bad.append(f"bin {b}={bins.get(b, 0)}!={n}")
    for b in bins:
        if b not in EXPECTED_BINS:
            bad.append(f"unexpected bin {b}")
    return bad


def check_twins(scen, by_id):
    bad = []
    for s in scen:
        sid, anc_id, cv = s["scenario_id"], s.get("anchor_id"), s.get("changed_variable")
        anchor = by_id.get(anc_id)
        if anchor is None:
            bad.append(sid)
            continue
        if anc_id == sid:  # an anchor
            if cv != "none" or s["variables"] != anchor["variables"]:
                bad.append(sid)
            continue
        diff = [k for k in set(s["variables"]) | set(anchor["variables"])
                if s["variables"].get(k, object()) != anchor["variables"].get(k, object())]
        if len(diff) != 1 or ":" not in cv or "->" not in cv:
            bad.append(sid)
            continue
        key = cv.split(":", 1)[0].strip()
        new = cv.split("->", 1)[1].strip()
        if diff[0] != key or str(s["variables"][key]) != new:
            bad.append(sid)
    return bad


def check_harm(scen):
    bad = []
    for s in scen:
        for a in possible(s):
            lab = s["labels"]["harm"].get(a)
            if lab is None or abs(computed_harm(s, a) - lab) > HARM_TOL:
                bad.append(s["scenario_id"])
                break
    return bad


def check_u(scen):
    bad = []
    for s in scen:
        P = possible(s)
        if not P:
            bad.append(s["scenario_id"])
            continue
        h = {a: computed_harm(s, a) for a in P}
        low = min(h.values())
        band = [a for a in ACTIONS if a in h and h[a] <= low + TAU + FLOAT_EPS]
        if band[0] != s["labels"]["U"]:
            bad.append(s["scenario_id"])
    return bad


def check_possible(scen):
    bad = []
    for s in scen:
        P = set(possible(s))
        ok = s["labels"]["U"] in P and s["labels"]["K"] in P
        lines = s["narrative"].split("\n")
        for a in ACTIONS:
            hits = [ln for ln in lines if ln.startswith(f"- {NAMES[a]}:")]
            if len(hits) != 1 or (("not possible" in hits[0]) != (a not in P)):
                ok = False
        if not ok:
            bad.append(s["scenario_id"])
    return bad


def check_scenery(scen, by_id):
    bad = []
    for s in scen:
        if s.get("bin") == "gamma":
            a = by_id.get(s.get("anchor_id"))
            if a is None or (s["labels"]["U"], s["labels"]["K"]) != (a["labels"]["U"], a["labels"]["K"]):
                bad.append(s["scenario_id"])
    return bad


def check_kantian(scen, by_id):
    bad = []
    twins = defaultdict(dict)  # anchor_id -> {"means": [ids], "consent": [ids]}
    anchors = []
    for s in scen:
        if s.get("anchor_id") == s["scenario_id"]:
            anchors.append(s)
            if s["labels"]["U"] == s["labels"]["K"]:
                bad.append(s["scenario_id"])
        else:
            var = s.get("changed_variable", "").split(":", 1)[0].strip()
            if var in ("means", "consent"):
                twins[s.get("anchor_id")].setdefault(var, []).append(s)
    for a in anchors:
        for var in ("means", "consent"):
            ts = twins[a["scenario_id"]].get(var, [])
            if not ts:
                bad.append(f"{a['scene_id']} has no {var} twin")
            for t in ts:
                if t["labels"]["K"] == a["labels"]["K"]:
                    bad.append(t["scenario_id"])
    return bad


def report(letter, name, bad):
    seen, uniq = set(), []
    for b in bad:
        if b not in seen:
            seen.add(b)
            uniq.append(b)
    if uniq:
        print(f"{letter} {name}: {len(uniq)} problems " + " ".join(uniq[:5]))
    else:
        print(f"{letter} {name}: OK")
    return len(uniq)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = json.load(open(sys.argv[1]))
    scen = d["scenarios"]
    by_id = {}
    for s in scen:
        by_id.setdefault(s["scenario_id"], s)
    total = 0
    total += report("A", "counts", check_counts(d, scen))
    total += report("B", "twins", check_twins(scen, by_id))
    total += report("C", "harm", check_harm(scen))
    total += report("D", "U label", check_u(scen))
    total += report("E", "possible actions", check_possible(scen))
    total += report("F", "scenery", check_scenery(scen, by_id))
    total += report("G", "Kantian", check_kantian(scen, by_id))
    print(f"INDEPENDENT CHECK: {total} problems")
    sys.exit(0 if total == 0 else 1)


if __name__ == "__main__":
    main()
