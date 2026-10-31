"""Print one scenario for review: narrative, numbers, labels, and what differs from its anchor.

Usage:  python show_scenario.py one_vs_five_high-S01            (reads expected/)
        python show_scenario.py one_vs_five_high-S01 --out out  (reads your own run)
        python show_scenario.py one_vs_five_high --all          (every scenario of a scene, one after another)
"""
import argparse
import json
import os
import re


def load(out, scene):
    d = os.path.join(out, scene)
    sc = [json.loads(l) for l in open(os.path.join(d, "scenarios.jsonl"))]
    labs = {l["scenario_id"]: l for l in map(json.loads, open(os.path.join(d, "labels.jsonl")))}
    narr = {n["scenario_id"]: n["narrative"] for n in map(json.loads, open(os.path.join(d, "narratives.jsonl")))}
    recs = {r["scenario_id"]: r for r in json.load(open(os.path.join(d, "records.json")))}
    return sc, labs, narr, recs


def sentences(text):
    head, _, actions = text.partition("\n\n")
    return re.split(r"(?<=\.) (?=[A-Z])", head) + actions.split("\n")


def show(out, sid):
    scene = sid.rsplit("-", 1)[0]
    sc, labs, narr, recs = load(out, scene)
    row = next(s for s in sc if s["scenario_id"] == sid)
    anchor = sc[0]["scenario_id"]
    lab, rec = labs[sid], recs[sid]
    print("=" * 100)
    print(f"{sid}    changed variable: {row['changed_variable']}")
    print(f"codebook labels: U = {lab['U']}   K = {lab['K']}")
    print("-" * 100)
    print(narr[sid])
    print("-" * 100)
    print("numbers in the record (per person; every person in a group has the same numbers):")
    for a in ["brake", "maintain", "swerve_left", "swerve_right", "accelerate"]:
        if not rec["feasible_actions"][a]:
            print(f"  {a:<13} not possible")
            continue
        seen = {}
        for p in rec["outcomes"][a]["affected_parties"]:
            g = p["party_id"].rsplit("_", 1)[0]
            seen.setdefault(g, [0, p["severity_distribution"]])[0] += 1
        parts = [f"{g} x{n}: " + ", ".join(f"{k} {v:g}" for k, v in d.items() if v) for g, (n, d) in seen.items()]
        print(f"  {a:<13} harm {lab['harm'][a]:<7} agency {lab['agency_mode'][a]:<12} " + ("; ".join(parts) or "no one harmed"))
    if sid != anchor:
        print("-" * 100)
        print("sentences that differ from the anchor (only the changed variable's sentences may appear here):")
        for s_a, s_t in zip(sentences(narr[anchor]), sentences(narr[sid])):
            if s_a != s_t:
                print(f"  anchor: {s_a}\n  twin:   {s_t}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario")
    ap.add_argument("--out", default="expected")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    if a.all:
        for s in load(a.out, a.scenario)[0]:
            show(a.out, s["scenario_id"])
    else:
        show(a.out, a.scenario)
