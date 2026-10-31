"""Writes catalog.md from the situation definitions and the expected outputs."""
import json, sys
sys.path.insert(0, ".")
import make_scenes as M
DESC = {
 "means": "Kantian. 1 = harming this group is how the action works (means test: yes); 0 = they are only in the car's new path",
 "consent": "Kantian. 1 = that group gave documented prior consent",
 "n_ahead": "people in the car's lane ahead", "p_hit": "each one's fatality probability if the car keeps going",
 "brake_gain": "factor braking multiplies that probability by", "left_sev": "likely outcome for a person struck by the left swerve",
 "left_count": "people in the left lane", "right_open": "1 = the right-side barrier can be steered into",
 "occupants": "people in this car", "n_cross": "pedestrians ahead", "cyclist_sev": "likely outcome for a struck cyclist",
 "cyclist_count": "cyclists in the bike lane", "oncoming_present": "1 = an oncoming car with 2 occupants is in the left lane",
 "ego_occ": "people in this car", "brake_works": "1 = the brakes partly work, so braking is possible",
 "van_sev": "likely outcome for people in the struck van", "van_occ": "people in the van",
 "guardrail_open": "1 = the right guardrail can be steered into", "n_stop": "people at the bus stop",
 "p_stop": "each one's fatality probability if the wrong-way car is not stopped", "success": "probability the interception stops the wrong-way car",
 "wrong_sev": "likely outcome for people in the wrong-way car", "wrong_occ": "people in the wrong-way car",
 "debris_ped": "1 = a pedestrian stands near the meeting point", "moto_present": "1 = a motorcyclist follows the car",
 "moto_sev": "likely outcome for the motorcyclist if the car brakes", "worker_sev": "likely outcome for a struck road worker",
 "worker_count": "road workers in the left lane", "n_crowd": "people in the crosswalk",
 "p_crowd": "each one's fatality probability if the truck is not blocked", "block_success": "probability the block stops the truck",
 "occ_sev": "likely outcome for this car's occupants if they block the truck", "driver_risk": "1 = the truck has a driver (seriously injured by the block)",
 "weather": "scenery only", "time_of_day": "scenery only", "location": "scenery only",
}
out = []
for s in M.SITUATIONS:
    files = M.scene_files(s)
    hi, mid, lo = (files[f"{s['situation']}_{l}"] for l in ("high", "mid", "low"))
    types = {g["type"]: g["noun_many"] for g in s["groups"].values() if g.get("type")}
    lab = json.loads(open(f"expected/{s['situation']}_high/labels.jsonl").readline())
    narr = json.loads(open(f"expected/{s['situation']}_high/narratives.jsonl").readline())["narrative"]
    out.append(f"## {s['situation']}\n\n**{s['title']}.** Reviewer: {s['owner'].capitalize()}. Anchor labels: U = {lab['U']}, K = {lab['K']}.\n")
    out.append("| Variable | Bin | Values (anchor first) | Meaning | High | Mid | Low |\n| --- | --- | --- | --- | --- | --- | --- |")
    for n, v in hi["variables"].items():
        meaning = DESC.get(n) or f"scenery only: how the {types[n]} are described"
        mark = lambda f: "varies" if n in f["variables"] else "fixed"
        out.append(f"| `{n}` | {v['bin']} | {', '.join(str(x) for x in v['values'])} | {meaning} | varies | {mark(mid)} | {mark(lo)} |")
    out.append("\nAnchor narrative (the exact text a model receives for S00, at every level):\n\n```text\n" + narr + "\n```\n")
open("catalog.md", "w").write("\n".join(out))
print("ok")
