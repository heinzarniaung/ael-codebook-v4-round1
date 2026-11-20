# AEL scenario codebook

Text dilemma scenarios for the Automotive Ethics Lab, labelled with Codebook v4: a utilitarian label U and a Kantian label K
over five actions (brake, maintain, swerve_left, swerve_right, accelerate).

Each **situation** is written once. It expands into three **scenes** (high, mid, low), and each scene into an anchor
scenario plus "twins" that change one variable at a time. Situations are released in **rounds**: a round is a fixed list
of situations that is reviewed together and then frozen.

| Round | Situations | Scenarios | Status |
| --- | --- | --- | --- |
| [round1](rounds/round1.yaml) | 6 | 228 | in review: 41 failed review items open in [reviews/round1/failed_items.yaml](reviews/round1/failed_items.yaml) |
| [round2](rounds/round2.yaml) | 13 | 494 | open: not reviewed yet |

What changed, and who added it: [CHANGELOG.md](CHANGELOG.md). The full writing and review guide is still the
"Scaling Scenario Generation" doc.

## Build a round

Requires Python 3.10+ and `pip install pyyaml==6.0.3 jsonschema==4.26.0`. Run from the repository root, on any OS:

```
python tools/build.py round1        # or round2, or --all
```

This writes `build/round1/`: the scene files, `expected/` and `catalog.md`. **The deliverable is
`build/<round>/expected/scenarios.json`.** It then runs every check and ends with `round1: ALL CHECKS PASS`
or a list of what failed. `build/` is generated and never committed.

Each entry in `scenarios.json` holds the scenario id, scene, situation, level, anchor id, changed variable, bin, every
variable's value, the narrative, the Codebook v4 record, and the U and K labels.

## Add or change a situation

1. Edit `situations/<name>.py`, or copy a similar file to a new name. The file name must equal its `"situation"` field.
2. List a new situation in the open round's file under `rounds/`. Every situation must be in exactly one round.
3. `python tools/build.py <round>` and fix anything it reports.

Never edit or commit files in `build/`. Don't change a situation in a frozen round; add a new one to the open round.

## Review a round

```
python tools/build.py round2
python tools/reviews.py round2 new <your name> <situation> <situation>   # creates reviews/round2/<your name>.csv
python tools/show_scenario.py market_street_high-S01                     # read one scenario
python tools/reviews.py round2 summary                                   # check the sheets, list failed items
```

Record each failure's cause in `reviews/<round>/failed_items.yaml`. To freeze a round once every failure is fixed or
accepted: set its `status` to `frozen`, tag the commit (`git tag round-1`), and attach its `scenarios.json` to a
GitHub release.

## Layout

| Path | What it is |
| --- | --- |
| `situations/` | One file per situation; `_shared.py` holds the scenery and sentences several situations use |
| `rounds/` | One file per round: which situations it has, and its status |
| `codebook/` | Codebook v4's labeler and record schema |
| `tools/build.py` | Builds a round and runs every check below |
| `tools/make_scenes.py` | Writes a round's scene files from its situations |
| `tools/reference_pipeline.py` | Expands scenes into anchors and twins, builds records, labels them, writes narratives and `scenarios.json` |
| `tools/verify_round.py` | Per scene: counts, anchor conflict, Kantian twins flip K, scenery twins change nothing; then schema, labels and unique case codes |
| `tools/check_independent.py` | Re-checks `scenarios.json` against Codebook v4 using only the standard library, without the labeler |
| `tools/lint.py` | Structural checks on scene files |
| `tools/show_scenario.py`, `tools/reviews.py`, `tools/make_catalog.py` | Review helpers and the scene catalog |
| `reviews/<round>/` | Review sheets and `failed_items.yaml`; `claude_assisted/` holds a Claude-assisted review |

The per-scene output folders also contain `packets/` and `key.csv`, prompt files for a later model round.

## Known issues

- Line numbers in `reviews/round1/failed_items.yaml` (`make_scenes.py:63` and so on) refer to the old single
  `ael_round1_kit/make_scenes.py`, as of commit `15fcb0c`.
