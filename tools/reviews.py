"""Review sheets, one folder per round: reviews/<round>/<reviewer>.csv.

  python tools/reviews.py <round> new <reviewer> <situation> ...   creates reviews/<round>/<reviewer>.csv
  python tools/reviews.py <round> summary                          checks the round's sheets, lists every failed item

Build the round first (python tools/build.py <round>): new sheets are made from its expected labels.

A sheet has one row per scenario. R1-R8 are the checklist items in Auden's guide; each cell is Y, N or NA
(NA only where the guide allows it). Any N needs a note.
"""
import csv
import glob
import os
import sys

import rounds

ITEMS = [f"R{i}" for i in range(1, 9)]
COLS = ["scene_id", "scenario_id", "case", "changed_variable"] + ITEMS + ["note"]
NA_OK = {"R4"}  # R4 (only the changed variable changed) is NA for anchors


def new(round_name, reviewer, situations):
    listed = rounds.load_round(round_name)["situations"]
    missing = [s for s in situations if s not in listed]
    if missing:
        sys.exit(f"not in {round_name}: {', '.join(missing)}")
    rows = [r for r in csv.DictReader(open(rounds.build_dir(round_name, "expected", "ALL_expected_labels.csv")))
            if r["scene_id"].rsplit("_", 1)[0] in situations]
    order = {"high": 0, "mid": 1, "low": 2}
    rows.sort(key=lambda r: (r["scene_id"].rsplit("_", 1)[0], order[r["scene_id"].rsplit("_", 1)[1]], r["scenario_id"]))
    folder = os.path.join(rounds.ROOT, "reviews", round_name)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{reviewer}.csv")
    if os.path.exists(path):
        sys.exit(f"{path} already exists; not overwriting it")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({**{c: r[c] for c in COLS[:4]}, **{i: "" for i in ITEMS}, "note": ""})
    print(f"wrote {path} with {len(rows)} rows")


def summary(round_name):
    rounds.load_round(round_name)
    problems, fails, total = [], [], 0
    for path in sorted(glob.glob(os.path.join(rounds.ROOT, "reviews", round_name, "*.csv"))):
        if path.endswith("_recount.csv"):
            continue
        for n, r in enumerate(csv.DictReader(open(path)), start=2):
            total += 1
            anchor = r["changed_variable"] == "none"
            for i in ITEMS:
                v = r[i].strip().upper()
                ok = v in ("Y", "N") or (v == "NA" and i in NA_OK and anchor)
                if not ok:
                    problems.append(f"{path} line {n} {r['scenario_id']}: {i} is '{r[i]}' (must be Y or N" + (", or NA for an anchor)" if i in NA_OK else ")"))
                if v == "N":
                    fails.append(f"{path} {r['scenario_id']} (case {r['case']}): {i} failed. Note: {r['note'] or 'MISSING NOTE'}")
                    if not r["note"].strip():
                        problems.append(f"{path} line {n} {r['scenario_id']}: {i} is N but the note is empty")
    print(f"rows: {total} | incomplete or invalid cells: {len(problems)} | failed items: {len(fails)}")
    for p in problems:
        print("  INCOMPLETE", p)
    for p in fails:
        print("  FAILED    ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    if len(sys.argv) >= 5 and sys.argv[2] == "new":
        new(sys.argv[1], sys.argv[3], sys.argv[4:])
    elif len(sys.argv) == 3 and sys.argv[2] == "summary":
        summary(sys.argv[1])
    else:
        sys.exit(__doc__)
