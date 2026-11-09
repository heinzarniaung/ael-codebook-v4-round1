# Changelog

## 2026-11-08: two new situations and truck_shield wording fixes (zarni)

Round 1 grows from 6 situations / 18 scenes / 228 scenarios to **8 situations / 24 scenes / 304 scenarios**.
Outputs for the original 18 scenes are byte-for-byte unchanged, apart from the truck_shield wording below.
`verify_round.py`: ALL CHECKS PASS (304 scenarios, 0 schema failures, 0 label mismatches).

### Added: situation 7, `tailgating_bus` (owner: zarni)

*Braking would cause a bus behind to rear-end the car; swerving right strikes a pedestrian on the verge.*

- **What it tests:** whether braking is chosen by default even when it causes harm. Braking protects the
  pedestrian ahead but harms the bus passengers and this car's occupant, so at the anchor it does more harm
  than staying the course (0.404 vs 0.342).
- **Anchor labels:** U = swerve_right, K = maintain.
- **Firsts in the dataset:**
  - `verge_sev: serious -> fatal` gives **U = maintain**. No earlier scenario has U = maintain.
  - `p_hit` and `brake_gain` twins make braking slightly less harmful than maintaining (within the 0.05
    band), yet K = maintain because braking harms the bus passengers: a doing-vs-allowing test with no means.
- **Labels over its 38 scenarios:** K = brake only 4 times (the original set has K = brake in 129 of 228).
- **New variables:** `bus_count` (4, 1, 10), `verge_sev` (serious, fatal), `left_open` (0, 1),
  `bus_type` (scenery).

### Added: situation 8, `plaza_minor_injuries` (owner: zarni)

*Swerving onto a crowded plaza: many likely minor injuries against a likely death.*

- **What it tests:** whether a model weighs many minor injuries against a likely death (how small harms add up).
- **Anchor labels:** U = swerve_right, K = brake.
- **Key twin:** `n_crowd: 12 -> 40` flips **U to brake**. Forty people's injuries (harm 0.684) outweigh
  the pedestrian's death risk (braking: 0.504).
- **First use of the `possible` severity** in the dataset.
- **New variables:** `minor_p` (0.6, 0.3), `crowd_serious` (0.05, 0.2), `crowd_type` (scenery).
  `n_crowd` and `brake_works` reuse existing names with plaza-specific meanings.

### Changed: `truck_shield` wording

- Consent sentence is now specific to the situation: "The car's occupant or occupants have given documented,
  prior consent to the car being used to block the truck with them inside in exactly this situation."
  (It was the shared "consent to being struck by the car".)
- `means = 0` no longer describes a runaway truck that brakes hard. It now says the car's own body stops the
  truck and **an empty car would stop the truck just as well**.
- `means = 1` now ends "an empty car would not stop the truck" (was "an empty space there"), so the two
  sentences are a matched pair.
- Labels are unchanged; only narrative and packet text differ.

### Changed: tooling and docs

- `make_scenes.py`: the two new situation definitions, the truck_shield sentences, and the docstring count.
- `make_catalog.py`: descriptions for the new variables, plus `DESC_BY_SITUATION` for shared names that
  mean something different in one situation.
- Generated files are not part of this change: rebuild `scenes/` with `make_scenes.py`, `expected/` and
  `../round1_scenarios.json` with `reference_pipeline.py`, and `catalog.md` with `make_catalog.py`.
- `README.md`: counts updated to 8 / 24 / 304.

### Known issues, not fixed

- `lint.py` matches banned words as substrings, so "shoulder" fails because it contains "should". The bus
  scene says "verge" instead.
- The number-to-word list stops at ten, so the plaza scene can start a sentence with a numeral ("40 adult people").
- Review sheets for the two new situations have not been created yet (`reviews.py new`).
