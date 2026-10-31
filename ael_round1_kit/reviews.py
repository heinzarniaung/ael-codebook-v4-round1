"""Review sheets.

  python reviews.py new <reviewer> <situation> <situation>   creates reviews/<reviewer>.csv, one row per scenario
  python reviews.py summary                                  checks every sheet and lists every failed item

A sheet has one row per scenario. R1-R8 are the checklist items in Auden's guide; each cell is Y, N or NA
(NA only where the guide allows it). Any N needs a note.
"""
import csv
import glob
import os
import sys

ITEMS = [f"R{i}" for i in range(1, 9)]
COLS = ["scene_id", "scenario_id", "case", "changed_variable"] + ITEMS + ["note"]
NA_OK = {"R4"}  # R4 (only the changed variable changed) is NA for anchors


def new(reviewer, situations):
    rows = [r for r in csv.DictReader(open("expected/ALL_expected_labels.csv"))
            if r["scene_id"].rsplit("_", 1)[0] in situations]
    order = {"high": 0, "mid": 1, "low": 2}
    rows.sort(key=lambda r: (r["scene_id"].rsplit("_", 1)[0], order[r["scene_id"].rsplit("_", 1)[1]], r["scenario_id"]))
    os.makedirs("reviews", exist_ok=True)
    path = f"reviews/{reviewer}.csv"
    if os.path.exists(path):
        sys.exit(f"{path} already exists; not overwriting it")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({**{c: r[c] for c in COLS[:4]}, **{i: "" for i in ITEMS}, "note": ""})
    print(f"wrote {path} with {len(rows)} rows")


def summary():
    problems, fails, total = [], [], 0
    for path in sorted(glob.glob("reviews/*.csv")):
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
    if len(sys.argv) >= 4 and sys.argv[1] == "new":
        new(sys.argv[2], sys.argv[3:])
    elif sys.argv[1:] == ["summary"]:
        summary()
    else:
        sys.exit(__doc__)
