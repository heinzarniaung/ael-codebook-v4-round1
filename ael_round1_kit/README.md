# AEL Round 1 kit

Builds the Round 1 scenario set: 8 situations × 3 levels = 24 scenes, 304 scenarios, in one file, `scenarios.json`.
Full instructions are in the "Scaling Scenario Generation" doc (Start here, then your own guide).
What changed since the first release, and who added it: see [CHANGELOG.md](CHANGELOG.md).

Requires Python 3.10+ and `pip install pyyaml==6.0.3 jsonschema==4.26.0`. On Windows, use Git Bash.

## Build and check (2 minutes)

```
python make_scenes.py                                  # wrote 24 scene files   (scenes/ must not change)
python reference_pipeline.py scenes/*.yaml --out out   # ... wrote out/scenarios.json with 304 scenarios
python verify_round.py out                             # last line: ... ALL CHECKS PASS
diff -r out expected && echo IDENTICAL                 # must print only IDENTICAL
```

The deliverable is `out/scenarios.json` (the approved copy is `expected/scenarios.json`).
Each entry holds the scenario id, scene, situation, level, anchor id, changed variable, bin, every variable's value,
the narrative, the Codebook v4 record, and the U and K labels.

## Files

| Path | What it is |
| --- | --- |
| `make_scenes.py` | The eight situation definitions; writes the 24 scene files. Change a situation here, never in `scenes/` |
| `scenes/<situation>_<level>.yaml` | The 24 scene files |
| `reference_pipeline.py` | Expands each scene into its anchor and twins, builds the records, labels them, writes the narratives, and merges everything into `scenarios.json` |
| `codebook/labeler.py`, `codebook/schema_scenario_v4.json` | Codebook v4's labeler and record schema |
| `verify_round.py` | Checks every scene (counts, anchor conflict, Kantian twins flip K, scenery twins change nothing) and `scenarios.json` (unique ids, schema, labels reproduced) |
| `lint.py` | Checks scene files for structural mistakes; used when writing new situations |
| `show_scenario.py` | `python show_scenario.py one_vs_five_high-S01` prints one scenario for review; `--all` with a scene id prints the whole scene |
| `reviews.py` | `python reviews.py new <name> <situation> <situation>` creates a review sheet; `python reviews.py summary` checks all sheets |
| `make_catalog.py`, `catalog.md` | The scene catalog |
| `expected/` | The correct output: `scenarios.json`, `ALL_expected_labels.csv`, and one folder per scene |

The per-scene folders also contain `packets/` and `key.csv`, prompt files for a later model round. This round does not use them.
