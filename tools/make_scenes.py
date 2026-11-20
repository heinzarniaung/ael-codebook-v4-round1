"""Writes three scene files (high, mid, low) for every situation in a round.

Usage:  python tools/make_scenes.py <round>      writes build/<round>/scenes/

Situations are defined in situations/<name>.py; the round's file in rounds/ lists which ones it has.
"""
import copy
import os
import sys

import yaml

import rounds
from situations._shared import FACTS_COMMON, GAMMA_COMMON


def scene_files(s):
    harm = s["harm"]
    gammas = [("weather", GAMMA_COMMON["weather"]["values"])] + s["gamma_types"] + [
        ("time_of_day", GAMMA_COMMON["time_of_day"]["values"]), ("location", GAMMA_COMMON["location"]["values"])]
    alpha = list(s["alpha"].items())
    levels = {
        "high": [n for n, _ in alpha] + [n for n, _ in harm] + [n for n, _ in gammas],
        "mid": [n for n, _ in alpha] + [n for n, _ in harm[:5]] + ["time_of_day", "location", s["mid_gamma_type"]],
        "low": [n for n, _ in alpha] + [n for n, _ in harm[1:3]] + ["time_of_day"],
    }
    allvars = {}
    for n, v in alpha:
        allvars[n] = {"bin": "alpha", "values": v}
    for n, v in harm:
        allvars[n] = {"bin": "harm", "values": v}
    for n, v in gammas:
        allvars[n] = {"bin": "gamma", "values": v}
    facts = copy.deepcopy(FACTS_COMMON)
    facts.update({k: v for k, v in s["facts"].items() if k != "wall"})
    out = {}
    for level, keep in levels.items():
        sid = f"{s['situation']}_{level}"
        doc = {
            "scene_id": sid, "situation": s["situation"], "level": level, "title": s["title"],
            "parent": None if level == "high" else f"{s['situation']}_high",
            "owner": s["owner"], "reviewed": False, "spotcheck": None,
            "variables": {n: allvars[n] for n in allvars if n in keep},
            "fixed": {n: allvars[n]["values"][0] for n in allvars if n not in keep},
            "groups": s["groups"],
            "feasible": s["feasible"],
            "outcomes": s["outcomes"],
            "means_test": s["means_test"],
            "facts": facts,
            "order": s["order"],
        }
        out[sid] = doc
    return out


def write_round(name):
    out = rounds.build_dir(name, "scenes")
    os.makedirs(out, exist_ok=True)
    sits = rounds.situations_of(name)
    for s in sits:
        for sid, doc in scene_files(s).items():
            with open(os.path.join(out, f"{sid}.yaml"), "w") as f:
                yaml.safe_dump(doc, f, sort_keys=False, allow_unicode=True, width=200)
    return len(os.listdir(out)), len(sits)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    n_files, n_sits = write_round(sys.argv[1])
    print("wrote", n_files, "scene files for", n_sits, "situations")
