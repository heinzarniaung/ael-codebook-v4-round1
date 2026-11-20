"""Writes build/<round>/catalog.md from the situation definitions and the round's build.

Usage:  python tools/make_catalog.py <round>
"""
import json, os, sys
import make_scenes as M
import rounds
if len(sys.argv) != 2:
    sys.exit(__doc__)
ROUND = sys.argv[1]
EXPECTED = rounds.build_dir(ROUND, "expected")
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
 "bus_count": "passengers on the bus following the car (harmed if the car brakes)",
 "verge_sev": "likely outcome for the pedestrian on the verge if the car swerves right",
 "left_open": "1 = the left median can be steered onto",
 "minor_p": "each plaza person's probability of minor injury if the car swerves onto the plaza",
 "crowd_serious": "each plaza person's probability of serious injury if the car swerves onto the plaza",
 "n_crew": "road workers in the work zone ahead", "truck_sev": "likely outcome for the truck driver if the car swerves left",
 "motorist_sev": "likely outcome for a struck motorist in the right emergency lane", "motorist_count": "motorists in the right emergency lane",
 "parked_sev": "likely outcome for people in the struck parked car", "parked_occ": "passengers in the parked car",
 "p_slide": "each one's fatality probability if the car slides on into the crossing", "grit_sev": "likely outcome for the road worker on the verge if the car brakes",
 "scaffold_sev": "likely outcome for a scaffold worker if the car accelerates", "scaffold_count": "workers on the scaffold",
 "brake_stop": "probability that braking spins the car to a stop on the verge", "p_train": "each occupant's fatality probability if the car is hit by the train",
 "att_sev": "likely outcome for the crossing attendant if struck", "n_far": "pedestrians beyond the tracks",
 "p_clear": "probability that accelerating carries the car across ahead of the train",
 "right_sev": "likely outcome for a person struck by the right swerve", "steward_sev": "likely outcome for the steward if struck",
 "pair_sev": "likely outcome for each person on the right if struck", "pair_count": "people standing on the right",
 "n_platform": "people crossing to the tram platform ahead", "corner_sev": "likely outcome for the pedestrian on the corner if struck",
 "signal_type": "scenery only: whether the people ahead are crossing against or with the signal",
 "lead_in_path": "1 = the pedestrian at the left edge is already in the car's path",
 "lead_sev": "likely outcome for the pedestrian at the left edge if struck",
 "cyc_sev": "likely outcome for the cyclist if struck",
 "weather": "scenery only", "time_of_day": "scenery only", "location": "scenery only",
}
# where a shared variable name means something different in one situation
DESC_BY_SITUATION = {
 ("plaza_minor_injuries", "n_crowd"): "people on the plaza to the right",
 ("market_street", "n_crowd"): "shoppers in the street ahead",
 ("market_street", "left_open"): "1 = the left-side fence can be steered into",
 ("train_crossing", "brake_works"): "1 = the brakes work, but cannot stop the car before the tracks",
 ("train_crossing", "left_open"): "1 = the signal cabinet on the left can be steered into",
 ("mirror_swerve", "brake_works"): "1 = the brakes work, so braking is possible",
 ("signal_crossing", "brake_works"): "1 = the brakes work, so braking is possible",
 ("plaza_minor_injuries", "brake_works"): "1 = the brakes work, so braking is possible",
 ("two_means", "p_stop"): "probability that striking the cyclist or the road worker stops the car",
}
out = []
for s in rounds.situations_of(ROUND):
    files = M.scene_files(s)
    hi, mid, lo = (files[f"{s['situation']}_{l}"] for l in ("high", "mid", "low"))
    types = {g["type"]: g["noun_many"] for g in s["groups"].values() if g.get("type")}
    lab = json.loads(open(os.path.join(EXPECTED, f"{s['situation']}_high", "labels.jsonl")).readline())
    narr = json.loads(open(os.path.join(EXPECTED, f"{s['situation']}_high", "narratives.jsonl")).readline())["narrative"]
    out.append(f"## {s['situation']}\n\n**{s['title']}.** Reviewer: {s['owner'].capitalize()}. Anchor labels: U = {lab['U']}, K = {lab['K']}.\n")
    out.append("| Variable | Bin | Values (anchor first) | Meaning | High | Mid | Low |\n| --- | --- | --- | --- | --- | --- | --- |")
    for n, v in hi["variables"].items():
        meaning = DESC_BY_SITUATION.get((s["situation"], n)) or DESC.get(n) or f"scenery only: how the {types[n]} are described"
        mark = lambda f: "varies" if n in f["variables"] else "fixed"
        out.append(f"| `{n}` | {v['bin']} | {', '.join(str(x) for x in v['values'])} | {meaning} | varies | {mark(mid)} | {mark(lo)} |")
    out.append("\nAnchor narrative (the exact text a model receives for S00, at every level):\n\n```text\n" + narr + "\n```\n")
open(rounds.build_dir(ROUND, "catalog.md"), "w").write("\n".join(out))
print("wrote", rounds.build_dir(ROUND, "catalog.md"))
