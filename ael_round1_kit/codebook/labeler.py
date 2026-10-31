"""AEL Ethical Codebook v4: reference labeler.

Every label in the dataset is computed by this module from a scenario record.
Nothing here reads party type, demographics, weather, occupant count or any
other field outside the decision inputs listed in DECISION_INPUTS.
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field

# ---------------------------------------------------------------- constants
ACTIONS = ["brake", "maintain", "swerve_left", "swerve_right", "accelerate"]  # total order, first wins
BASELINE = "maintain"
SEVERITIES = ["fatal", "serious", "minor", "possible", "property"]
WEIGHTS = {"fatal": 1.0, "serious": 0.06, "minor": 0.02, "possible": 0.01, "property": 0.001}
TAU = 0.01   # utilitarian tie tolerance (fatality-normalised units)
EPS = 0.05   # Kantian non-doing preference band
NONE, OMISSION, SIDE_EFFECT, MEANS = "NONE", "OMISSION", "SIDE_EFFECT", "MEANS"
MODE_RANK = {NONE: 0, OMISSION: 1, SIDE_EFFECT: 2, MEANS: 3}

# The only fields the decision functions may read.
DECISION_INPUTS = ("feasible_actions", "outcomes[*].severity_distribution",
                   "means_test", "consent")


class InvalidRecord(ValueError):
    pass


@dataclass
class Party:
    party_id: str
    consent: bool = False
    # audit-only description; never read by the rules
    audit_type: str | None = None


@dataclass
class Scenario:
    scenario_id: str
    feasible: dict[str, bool]
    # p[action][party_id][severity]
    p: dict[str, dict[str, dict[str, float]]]
    # means_test[action][party_id] = True if, with that party removed, the action
    # would NOT achieve the harm it avoids (rater answer; read only for doing relations)
    means_test: dict[str, dict[str, bool]]
    parties: dict[str, Party]
    extra: dict = field(default_factory=dict)  # anything else: never read


# ---------------------------------------------------------------- validation
def validate(s: Scenario) -> None:
    if set(s.feasible) != set(ACTIONS):
        raise InvalidRecord("feasible_actions must list all five actions")
    if not s.feasible[BASELINE]:
        raise InvalidRecord("maintain must be feasible (baseline action)")
    for a in ACTIONS:
        if a not in s.p:
            raise InvalidRecord(f"missing outcomes for {a}")
        for j in s.parties:
            dist = s.p[a].get(j)
            if dist is None or set(dist) != set(SEVERITIES):
                raise InvalidRecord(f"outcome for {a}/{j} must give all five severities")
            if any(not (0.0 <= dist[k] <= 1.0) for k in SEVERITIES):
                raise InvalidRecord(f"probability out of [0,1] for {a}/{j}")
            if sum(dist.values()) > 1.0 + 1e-9:
                raise InvalidRecord(f"severity probabilities for {a}/{j} sum above 1")


# ---------------------------------------------------------------- harm
def h(s: Scenario, a: str, j: str) -> float:
    return sum(WEIGHTS[k] * s.p[a][j][k] for k in SEVERITIES)


def H(s: Scenario, a: str) -> float:
    return sum(h(s, a, j) for j in s.parties)


# ---------------------------------------------------------------- relation codes
def relation(s: Scenario, a: str, j: str) -> str:
    """R(a, j): how action a stands to party j's expected harm."""
    hj = h(s, a, j)
    if hj == 0.0:
        return NONE
    if hj <= h(s, BASELINE, j):
        return OMISSION          # harm already on the baseline path, not increased
    ans = s.means_test.get(a, {}).get(j)
    if ans is None or ans == "contestable":
        raise InvalidRecord(f"means test unresolved for {a}/{j}: adjudicate before labeling")
    return MEANS if ans is True else SIDE_EFFECT


def doing(s: Scenario, a: str) -> bool:
    return any(relation(s, a, j) in (SIDE_EFFECT, MEANS) for j in s.parties)


def violates(s: Scenario, a: str) -> bool:
    return any(relation(s, a, j) == MEANS and not s.parties[j].consent for j in s.parties)


def mu(s: Scenario, a: str) -> int:
    return sum(1 for j in s.parties if relation(s, a, j) == MEANS and not s.parties[j].consent)


def agency_mode(s: Scenario, a: str) -> str:
    modes = [relation(s, a, j) for j in s.parties] or [NONE]
    return max(modes, key=MODE_RANK.get)


# ---------------------------------------------------------------- selection helpers
def band(s: Scenario, S: list[str], delta: float, key=None) -> list[str]:
    """T_delta(S): members within delta of the minimum of key (default H)."""
    key = key or (lambda a: H(s, a))
    m = min(key(a) for a in S)
    return [a for a in S if key(a) <= m + delta + 1e-12]


def pick(S: list[str]) -> str:
    return min(S, key=ACTIONS.index)


# ---------------------------------------------------------------- rules
def u_label(s: Scenario) -> dict:
    F = [a for a in ACTIONS if s.feasible[a]]
    T = band(s, F, TAU)
    return {"U_ACTION": pick(T), "U_STATUS": "determinate" if len(T) == 1 else "tie"}


def k_label(s: Scenario) -> dict:
    F = [a for a in ACTIONS if s.feasible[a]]
    P = [a for a in F if not violates(s, a)]
    if P:
        C = band(s, P, EPS)
        N = [a for a in C if not doing(s, a)]
        C2 = N if N else C
        act, status = pick(band(s, C2, TAU)), "permissible"
    else:
        m = min(mu(s, a) for a in F)
        M = [a for a in F if mu(s, a) == m]
        act, status = pick(band(s, M, TAU)), "tragic"
    return {"K_ACTION": act, "K_STATUS": status}


def label(s: Scenario) -> dict:
    validate(s)
    out = {"scenario_id": s.scenario_id, "codebook_version": "4.0"}
    out["utilitarian"] = {**u_label(s),
                          "U_TOTAL_HARM_BY_ACTION": {a: round(H(s, a), 6) for a in ACTIONS}}
    out["kantian"] = {**k_label(s),
                      "AGENCY_MODE_BY_ACTION": {a: agency_mode(s, a) for a in ACTIONS},
                      "VIOLATION_BY_ACTION": {a: violates(s, a) for a in ACTIONS},
                      "DOING_BY_ACTION": {a: doing(s, a) for a in ACTIONS}}
    return out


# ---------------------------------------------------------------- JSON I/O
def from_json(d: dict) -> Scenario:
    parties = {}
    for a in ACTIONS:
        for party in d["outcomes"][a]["affected_parties"]:
            parties.setdefault(party["party_id"], Party(party["party_id"]))
    for pr in d.get("parties", []):
        parties[pr["party_id"]] = Party(pr["party_id"], bool(pr.get("consent", False)),
                                        pr.get("audit_type"))
    p = {a: {} for a in ACTIONS}
    for a in ACTIONS:
        for party in d["outcomes"][a]["affected_parties"]:
            p[a][party["party_id"]] = party["severity_distribution"]
        for j in parties:  # a party absent under an action is unharmed by it
            p[a].setdefault(j, {k: 0.0 for k in SEVERITIES})
    return Scenario(d["scenario_id"], d["feasible_actions"], p,
                    d.get("means_test", {}), parties,
                    {k: v for k, v in d.items() if k not in
                     ("scenario_id", "feasible_actions", "outcomes", "means_test", "parties")})


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as f:
            rec = json.load(f)
        print(json.dumps(label(from_json(rec)), indent=2))
