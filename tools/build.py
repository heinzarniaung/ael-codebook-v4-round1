"""Build and check one round (or all of them) with one command.

Usage:  python tools/build.py round1
        python tools/build.py --all

Writes build/<round>/: scenes/, expected/ (the deliverable is expected/scenarios.json) and catalog.md.
Runs every check and exits 1 if any failed.
"""
import glob
import os
import shutil
import subprocess
import sys

import rounds

TOOLS = os.path.dirname(os.path.abspath(__file__))


def run(label, args):
    shown = [os.path.relpath(a, rounds.ROOT) if os.path.isabs(a) else a for a in args]
    yamls = [a for a in shown if a.endswith(".yaml")]
    if len(yamls) > 1:  # don't print every scene file
        shown = [a for a in shown if not a.endswith(".yaml")]
        shown.insert(1, f"<{len(yamls)} scene files>")
    print(f"\n== {label}: python {' '.join(shown)}", flush=True)
    return subprocess.run([sys.executable] + args, cwd=rounds.ROOT).returncode == 0


def build(name):
    rounds.load_round(name)
    shutil.rmtree(rounds.build_dir(name), ignore_errors=True)
    tool = lambda t: os.path.join(TOOLS, t)
    if not run("scenes", [tool("make_scenes.py"), name]):
        return ["make_scenes"]
    scenes = sorted(glob.glob(rounds.build_dir(name, "scenes", "*.yaml")))
    expected = rounds.build_dir(name, "expected")
    failed = []
    steps = [
        ("lint", [tool("lint.py")] + scenes),
        ("pipeline", [tool("reference_pipeline.py")] + scenes + ["--out", expected]),
        ("verify", [tool("verify_round.py"), expected]),
        ("independent check", [tool("check_independent.py"), os.path.join(expected, "scenarios.json")]),
        ("catalog", [tool("make_catalog.py"), name]),
    ]
    if glob.glob(os.path.join(rounds.ROOT, "reviews", name, "*.csv")):
        steps.append(("reviews", [tool("reviews.py"), name, "summary"]))
    for label, args in steps:
        if not run(label, args):
            failed.append(label)
            if label == "pipeline":
                break  # later steps need its output
    return failed


if __name__ == "__main__":
    if sys.argv[1:] == ["--all"]:
        names = rounds.names()
    elif len(sys.argv) == 2:
        names = [sys.argv[1]]
    else:
        sys.exit(__doc__)
    problems = rounds.check_membership()
    for p in problems:
        print("ROUNDS:", p)
    results = {n: build(n) for n in names}
    print()
    for n, failed in results.items():
        print(f"{n}: {'ALL CHECKS PASS' if not failed else 'FAILED: ' + ', '.join(failed)}  ->  {os.path.relpath(rounds.build_dir(n, 'expected', 'scenarios.json'), rounds.ROOT)}")
    sys.exit(1 if problems or any(results.values()) else 0)
