"""Rounds: which situations belong to which round, and where a round's build goes."""
import glob
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import situations  # noqa: E402


def names():
    return sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, "rounds", "*.yaml")))


def load_round(name):
    path = os.path.join(ROOT, "rounds", f"{name}.yaml")
    if not os.path.exists(path):
        raise SystemExit(f"no round {name!r}; rounds are: {', '.join(names())}")
    with open(path) as f:
        r = yaml.safe_load(f)
    if r.get("name") != name:
        raise SystemExit(f"rounds/{name}.yaml has name {r.get('name')!r}; it must match the file name")
    return r


def situations_of(name):
    """The round's situation definitions, in the round file's order."""
    return [situations.load(s) for s in load_round(name)["situations"]]


def build_dir(name, *parts):
    return os.path.join(ROOT, "build", name, *parts)


def check_membership():
    """Every situation file is in exactly one round, and every listed situation exists."""
    problems, seen = [], {}
    for r in names():
        for s in load_round(r)["situations"]:
            if s in seen:
                problems.append(f"{s} is in both {seen[s]} and {r}")
            seen[s] = r
    for s in situations.names():
        if s not in seen:
            problems.append(f"situations/{s}.py is not in any round")
    for s, r in seen.items():
        if s not in situations.names():
            problems.append(f"rounds/{r}.yaml lists {s}, but situations/{s}.py does not exist")
    return problems
