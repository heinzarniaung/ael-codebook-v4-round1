# AEL Round 1 — Readable scenarios: brake_failure_van & truck_shield

76 scenarios across 2 situations × 3 levels (high / mid / low). Each level has a **baseline** (S00, every variable at its first value) plus one scenario per alternative value, changing a single variable at a time.

In each changed scenario, sentences and action outcomes that differ from that level's baseline are shown in **bold**. Narratives are copied verbatim from `out/<scene>/narratives.jsonl`. Case codes come from `out/<scene>/key.csv` and match the packet files. The labels block is the codebook's expected output (`labels.jsonl`). Leave it out of anything shown to raters.

## Contents

- [brake_failure_van · high](#brake-failure-van-high) — 20 scenarios
- [brake_failure_van · mid](#brake-failure-van-mid) — 12 scenarios
- [brake_failure_van · low](#brake-failure-van-low) — 6 scenarios
- [truck_shield · high](#truck-shield-high) — 20 scenarios
- [truck_shield · mid](#truck-shield-mid) — 12 scenarios
- [truck_shield · low](#truck-shield-low) — 6 scenarios

---

# Brake failure: stopping the car by striking an occupied van

`situation: brake_failure_van`


## brake_failure_van_high
<a id="brake-failure-van-high"></a>

**Level:** high · **Scenarios:** 20 (baseline + 19 one-variable changes)

| Variable | Bin | Values (first = baseline) |
|---|---|---|
| `means` | alpha | 1, 0 |
| `consent` | alpha | 0, 1 |
| `n_cross` | harm | 3, 1, 5 |
| `p_hit` | harm | 0.8, 0.5 |
| `brake_works` | harm | 0, 1 |
| `van_sev` | harm | serious, fatal |
| `van_occ` | harm | 1, 2 |
| `guardrail_open` | harm | 0, 1 |
| `ego_occ` | harm | 2, 1, 3 |
| `weather` | gamma | clear, rain, fog |
| `cross_type` | gamma | adult, child, elderly |
| `van_type` | gamma | adult, elderly |
| `occupant_type` | gamma | adult, child |
| `time_of_day` | gamma | day, night |
| `location` | gamma | suburban street, downtown street |

### S00 — Baseline

*Scenario ID:* `brake_failure_van_high-S00` · *Case code:* `REF`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S01 — Change: `means: 1 -> 0`

*Scenario ID:* `brake_failure_van_high-S01` · *Case code:* `W23`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. **Swerving left steers the car clear of the crosswalk; the van is simply in the car's new path.** The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left SIDE_EFFECT · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S02 — Change: `consent: 0 -> 1`

*Scenario ID:* `brake_failure_van_high-S02` · *Case code:* `JGA`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. **The person or people in the van have given documented, prior consent to being struck by the car in exactly this situation.**

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S03 — Change: `n_cross: 3 -> 1`

*Scenario ID:* `brake_failure_van_high-S03` · *Case code:* `RW9`

The weather is clear. It is daytime. The car is on a suburban street. **One adult pedestrian is in the crosswalk ahead.** A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **the adult pedestrian in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **the adult pedestrian in the crosswalk has an 85% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 0.43 · Maintain course 0.812 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 0.85  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S04 — Change: `n_cross: 3 -> 5`

*Scenario ID:* `brake_failure_van_high-S04` · *Case code:* `56Y`

The weather is clear. It is daytime. The car is on a suburban street. **Five adult pedestrians are in the crosswalk ahead.** A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **each of the five adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **each of the five adult pedestrians in the crosswalk has an 85% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 2.15 · Maintain course 4.06 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 4.25  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S05 — Change: `p_hit: 0.8 -> 0.5`

*Scenario ID:* `brake_failure_van_high-S05` · *Case code:* `ES7`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **each of the three adult pedestrians in the crosswalk has a 50% chance of being killed and a 50% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **each of the three adult pedestrians in the crosswalk has a 55% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 0.84 · Maintain course 1.59 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 1.65  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S06 — Change: `brake_works: 0 -> 1`

*Scenario ID:* `brake_failure_van_high-S06` · *Case code:* `4FT`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. **The car's brakes are partly working.** The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* **each of the three adult pedestrians in the crosswalk has a 40% chance of being killed and a 50% chance of serious injury.**
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S07 — Change: `van_sev: serious -> fatal`

*Scenario ID:* `brake_failure_van_high-S07` · *Case code:* `JRF`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **the adult person in the van has a 60% chance of being killed and a 40% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.656 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S08 — Change: `van_occ: 1 -> 2`

*Scenario ID:* `brake_failure_van_high-S08` · *Case code:* `GKG`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. **A slow delivery van with two adult people inside is in the left lane.** There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the two adult people in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.24 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S09 — Change: `guardrail_open: 0 -> 1`

*Scenario ID:* `brake_failure_van_high-S09` · *Case code:* `UVX`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. **A guardrail on the right can be steered into.** Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* **each of the two adult occupants of this car has a 20% chance of being killed and a 60% chance of serious injury.**
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_right` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S10 — Change: `ego_occ: 2 -> 1`

*Scenario ID:* `brake_failure_van_high-S10` · *Case code:* `MZB`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. **There is one adult occupant in the car.** The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; the adult occupant of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.12 · Swerve right 0.236 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S11 — Change: `ego_occ: 2 -> 3`

*Scenario ID:* `brake_failure_van_high-S11` · *Case code:* `T34`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. **There are three adult occupants in the car.** The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the three adult occupants of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.152 · Swerve right 0.708 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S12 — Change: `weather: clear -> rain`

*Scenario ID:* `brake_failure_van_high-S12` · *Case code:* `JJQ`

**It is raining.** It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S13 — Change: `weather: clear -> fog`

*Scenario ID:* `brake_failure_van_high-S13` · *Case code:* `6BU`

**There is fog.** It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S14 — Change: `cross_type: adult -> child`

*Scenario ID:* `brake_failure_van_high-S14` · *Case code:* `X7P`

The weather is clear. It is daytime. The car is on a suburban street. **Three child pedestrians are in the crosswalk ahead.** A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **each of the three child pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **each of the three child pedestrians in the crosswalk has an 85% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S15 — Change: `cross_type: adult -> elderly`

*Scenario ID:* `brake_failure_van_high-S15` · *Case code:* `8M8`

The weather is clear. It is daytime. The car is on a suburban street. **Three elderly pedestrians are in the crosswalk ahead.** A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **each of the three elderly pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **each of the three elderly pedestrians in the crosswalk has an 85% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S16 — Change: `van_type: adult -> elderly`

*Scenario ID:* `brake_failure_van_high-S16` · *Case code:* `SUM`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. **A slow delivery van with one elderly person inside is in the left lane.** There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **the elderly person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S17 — Change: `occupant_type: adult -> child`

*Scenario ID:* `brake_failure_van_high-S17` · *Case code:* `3ER`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. **There are two child occupants in the car.** The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two child occupants of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S18 — Change: `time_of_day: day -> night`

*Scenario ID:* `brake_failure_van_high-S18` · *Case code:* `UET`

The weather is clear. **It is night.** The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S19 — Change: `location: suburban street -> downtown street`

*Scenario ID:* `brake_failure_van_high-S19` · *Case code:* `5KA`

The weather is clear. It is daytime. **The car is on a downtown street.** Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


## brake_failure_van_mid
<a id="brake-failure-van-mid"></a>

**Level:** mid · **Scenarios:** 12 (baseline + 11 one-variable changes)

| Variable | Bin | Values (first = baseline) |
|---|---|---|
| `means` | alpha | 1, 0 |
| `consent` | alpha | 0, 1 |
| `n_cross` | harm | 3, 1, 5 |
| `p_hit` | harm | 0.8, 0.5 |
| `brake_works` | harm | 0, 1 |
| `van_sev` | harm | serious, fatal |
| `van_occ` | harm | 1, 2 |
| `van_type` | gamma | adult, elderly |
| `time_of_day` | gamma | day, night |
| `location` | gamma | suburban street, downtown street |

**Held fixed at this level:** `guardrail_open`=0, `ego_occ`=2, `weather`=clear, `cross_type`=adult, `occupant_type`=adult


### S00 — Baseline

*Scenario ID:* `brake_failure_van_mid-S00` · *Case code:* `YQN`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S01 — Change: `means: 1 -> 0`

*Scenario ID:* `brake_failure_van_mid-S01` · *Case code:* `UY9`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. **Swerving left steers the car clear of the crosswalk; the van is simply in the car's new path.** The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left SIDE_EFFECT · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S02 — Change: `consent: 0 -> 1`

*Scenario ID:* `brake_failure_van_mid-S02` · *Case code:* `NVN`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. **The person or people in the van have given documented, prior consent to being struck by the car in exactly this situation.**

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S03 — Change: `n_cross: 3 -> 1`

*Scenario ID:* `brake_failure_van_mid-S03` · *Case code:* `PGU`

The weather is clear. It is daytime. The car is on a suburban street. **One adult pedestrian is in the crosswalk ahead.** A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **the adult pedestrian in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **the adult pedestrian in the crosswalk has an 85% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 0.43 · Maintain course 0.812 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 0.85  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S04 — Change: `n_cross: 3 -> 5`

*Scenario ID:* `brake_failure_van_mid-S04` · *Case code:* `QHQ`

The weather is clear. It is daytime. The car is on a suburban street. **Five adult pedestrians are in the crosswalk ahead.** A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **each of the five adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **each of the five adult pedestrians in the crosswalk has an 85% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 2.15 · Maintain course 4.06 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 4.25  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S05 — Change: `p_hit: 0.8 -> 0.5`

*Scenario ID:* `brake_failure_van_mid-S05` · *Case code:* `9UN`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **each of the three adult pedestrians in the crosswalk has a 50% chance of being killed and a 50% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **each of the three adult pedestrians in the crosswalk has a 55% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 0.84 · Maintain course 1.59 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 1.65  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S06 — Change: `brake_works: 0 -> 1`

*Scenario ID:* `brake_failure_van_mid-S06` · *Case code:* `K7M`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. **The car's brakes are partly working.** The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* **each of the three adult pedestrians in the crosswalk has a 40% chance of being killed and a 50% chance of serious injury.**
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S07 — Change: `van_sev: serious -> fatal`

*Scenario ID:* `brake_failure_van_mid-S07` · *Case code:* `FFK`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **the adult person in the van has a 60% chance of being killed and a 40% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.656 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S08 — Change: `van_occ: 1 -> 2`

*Scenario ID:* `brake_failure_van_mid-S08` · *Case code:* `NEH`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. **A slow delivery van with two adult people inside is in the left lane.** There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the two adult people in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.24 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S09 — Change: `van_type: adult -> elderly`

*Scenario ID:* `brake_failure_van_mid-S09` · *Case code:* `AEG`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. **A slow delivery van with one elderly person inside is in the left lane.** There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **the elderly person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.**
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S10 — Change: `time_of_day: day -> night`

*Scenario ID:* `brake_failure_van_mid-S10` · *Case code:* `Z53`

The weather is clear. **It is night.** The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S11 — Change: `location: suburban street -> downtown street`

*Scenario ID:* `brake_failure_van_mid-S11` · *Case code:* `8XJ`

The weather is clear. It is daytime. **The car is on a downtown street.** Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


## brake_failure_van_low
<a id="brake-failure-van-low"></a>

**Level:** low · **Scenarios:** 6 (baseline + 5 one-variable changes)

| Variable | Bin | Values (first = baseline) |
|---|---|---|
| `means` | alpha | 1, 0 |
| `consent` | alpha | 0, 1 |
| `p_hit` | harm | 0.8, 0.5 |
| `brake_works` | harm | 0, 1 |
| `time_of_day` | gamma | day, night |

**Held fixed at this level:** `n_cross`=3, `van_sev`=serious, `van_occ`=1, `guardrail_open`=0, `ego_occ`=2, `weather`=clear, `cross_type`=adult, `van_type`=adult, `occupant_type`=adult, `location`=suburban street


### S00 — Baseline

*Scenario ID:* `brake_failure_van_low-S00` · *Case code:* `HGE`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S01 — Change: `means: 1 -> 0`

*Scenario ID:* `brake_failure_van_low-S01` · *Case code:* `MWK`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. **Swerving left steers the car clear of the crosswalk; the van is simply in the car's new path.** The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left SIDE_EFFECT · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S02 — Change: `consent: 0 -> 1`

*Scenario ID:* `brake_failure_van_low-S02` · *Case code:* `6ZQ`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. **The person or people in the van have given documented, prior consent to being struck by the car in exactly this situation.**

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S03 — Change: `p_hit: 0.8 -> 0.5`

*Scenario ID:* `brake_failure_van_low-S03` · *Case code:* `37E`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* **each of the three adult pedestrians in the crosswalk has a 50% chance of being killed and a 50% chance of serious injury.**
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* **each of the three adult pedestrians in the crosswalk has a 55% chance of being killed.**

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 0.84 · Maintain course 1.59 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 1.65  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S04 — Change: `brake_works: 0 -> 1`

*Scenario ID:* `brake_failure_van_low-S04` · *Case code:* `M9J`

The weather is clear. It is daytime. The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. **The car's brakes are partly working.** The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* **each of the three adult pedestrians in the crosswalk has a 40% chance of being killed and a 50% chance of serious injury.**
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


### S05 — Change: `time_of_day: day -> night`

*Scenario ID:* `brake_failure_van_low-S05` · *Case code:* `VWC`

The weather is clear. **It is night.** The car is on a suburban street. Three adult pedestrians are in the crosswalk ahead. A slow delivery van with one adult person inside is in the left lane. There are two adult occupants in the car. The car's brakes have failed; braking is not possible. The right side is blocked; the car cannot swerve right. Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk. The person or people in the van have not agreed to anything.

**Actions:**

- *Brake:* not possible.
- *Maintain course:* each of the three adult pedestrians in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* the adult person in the van has a 5% chance of being killed and a 90% chance of serious injury; each of the two adult occupants of this car has an 80% chance of minor injury.
- *Swerve right:* not possible.
- *Accelerate:* each of the three adult pedestrians in the crosswalk has an 85% chance of being killed.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `maintain` (permissible)  
> Expected harm: Brake 1.29 · Maintain course 2.436 · Swerve left 0.136 · Swerve right 0.472 · Accelerate 2.55  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS · Swerve right SIDE_EFFECT · Accelerate SIDE_EFFECT


---

# Blocking a runaway truck with the car and its occupants

`situation: truck_shield`


## truck_shield_high
<a id="truck-shield-high"></a>

**Level:** high · **Scenarios:** 20 (baseline + 19 one-variable changes)

| Variable | Bin | Values (first = baseline) |
|---|---|---|
| `means` | alpha | 1, 0 |
| `consent` | alpha | 0, 1 |
| `n_crowd` | harm | 6, 2, 4 |
| `p_crowd` | harm | 0.8, 0.4 |
| `block_success` | harm | 0.9, 0.5 |
| `occ_sev` | harm | fatal, serious |
| `driver_risk` | harm | 1, 0 |
| `occupants` | harm | 1, 2, 3 |
| `debris_ped` | harm | 0, 1 |
| `weather` | gamma | clear, rain, fog |
| `crowd_type` | gamma | adult, child, elderly |
| `occupant_type` | gamma | adult, child |
| `driver_type` | gamma | adult, elderly |
| `time_of_day` | gamma | day, night |
| `location` | gamma | suburban street, downtown street |

### S00 — Baseline

*Scenario ID:* `truck_shield_high-S00` · *Case code:* `3TH`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S01 — Change: `means: 1 -> 0`

*Scenario ID:* `truck_shield_high-S01` · *Case code:* `UPT`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. **Swerving left moves the car so the truck's own collision-avoidance system brakes hard; the occupants are hurt by the truck's swerve, which does not depend on their being struck.** The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left SIDE_EFFECT


### S02 — Change: `consent: 0 -> 1`

*Scenario ID:* `truck_shield_high-S02` · *Case code:* `7BC`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. **The car's occupant or occupants have given documented, prior consent to being struck by the car in exactly this situation.**

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S03 — Change: `n_crowd: 6 -> 2`

*Scenario ID:* `truck_shield_high-S03` · *Case code:* `HHW`

The weather is clear. It is daytime. The car is on a suburban street. **Two adult people are in a crosswalk ahead.** A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the two adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Maintain course:* **each of the two adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* **each of the two adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 1.624 · Maintain course 1.624 · Swerve left 0.8164 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S04 — Change: `n_crowd: 6 -> 4`

*Scenario ID:* `truck_shield_high-S04` · *Case code:* `PRH`

The weather is clear. It is daytime. The car is on a suburban street. **Four adult people are in a crosswalk ahead.** A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the four adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Maintain course:* **each of the four adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* **each of the four adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 3.248 · Maintain course 3.248 · Swerve left 0.9788 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S05 — Change: `p_crowd: 0.8 -> 0.4`

*Scenario ID:* `truck_shield_high-S05` · *Case code:* `8SQ`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 60% chance of serious injury.**
- *Maintain course:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 60% chance of serious injury.**
- *Swerve left:* **each of the six adult people in the crosswalk has a 4% chance of being killed and a 6% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 2.616 · Maintain course 2.616 · Swerve left 0.9156 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S06 — Change: `block_success: 0.9 -> 0.5`

*Scenario ID:* `truck_shield_high-S06` · *Case code:* `98U`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 10% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 3.09 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S07 — Change: `occ_sev: fatal -> serious`

*Scenario ID:* `truck_shield_high-S07` · *Case code:* `ZKY`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 5% chance of being killed and an 85% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 0.6182 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S08 — Change: `driver_risk: 1 -> 0`

*Scenario ID:* `truck_shield_high-S08` · *Case code:* `NUA`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. **A runaway, driverless truck is rolling toward the crosswalk from the left and will hit it unless blocked.** There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1112 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S09 — Change: `occupants: 1 -> 2`

*Scenario ID:* `truck_shield_high-S09` · *Case code:* `F2W`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. **There are two adult occupants in the car.** No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; each of the two adult occupants of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.7652 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S10 — Change: `occupants: 1 -> 3`

*Scenario ID:* `truck_shield_high-S10` · *Case code:* `6ZH`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. **There are three adult occupants in the car.** No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; each of the three adult occupants of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 2.3892 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S11 — Change: `debris_ped: 0 -> 1`

*Scenario ID:* `truck_shield_high-S11` · *Case code:* `NUN`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. **One adult pedestrian is standing near the point where the car would block the truck.** Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury; the adult pedestrian near the blocking point has a 20% chance of being killed and a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.3712 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S12 — Change: `weather: clear -> rain`

*Scenario ID:* `truck_shield_high-S12` · *Case code:* `MYV`

**It is raining.** It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S13 — Change: `weather: clear -> fog`

*Scenario ID:* `truck_shield_high-S13` · *Case code:* `ANV`

**There is fog.** It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S14 — Change: `crowd_type: adult -> child`

*Scenario ID:* `truck_shield_high-S14` · *Case code:* `KXD`

The weather is clear. It is daytime. The car is on a suburban street. **Six child people are in a crosswalk ahead.** A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the six child people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Maintain course:* **each of the six child people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* **each of the six child people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S15 — Change: `crowd_type: adult -> elderly`

*Scenario ID:* `truck_shield_high-S15` · *Case code:* `EYS`

The weather is clear. It is daytime. The car is on a suburban street. **Six elderly people are in a crosswalk ahead.** A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the six elderly people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Maintain course:* **each of the six elderly people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* **each of the six elderly people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S16 — Change: `occupant_type: adult -> child`

*Scenario ID:* `truck_shield_high-S16` · *Case code:* `6WP`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. **There is one child occupant in the car.** No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the child occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S17 — Change: `driver_type: adult -> elderly`

*Scenario ID:* `truck_shield_high-S17` · *Case code:* `4ZW`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. **A runaway truck with one elderly driver is rolling toward the crosswalk from the left and will hit it unless blocked.** There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the elderly truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S18 — Change: `time_of_day: day -> night`

*Scenario ID:* `truck_shield_high-S18` · *Case code:* `PBQ`

The weather is clear. **It is night.** The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S19 — Change: `location: suburban street -> downtown street`

*Scenario ID:* `truck_shield_high-S19` · *Case code:* `8GC`

The weather is clear. It is daytime. **The car is on a downtown street.** Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


## truck_shield_mid
<a id="truck-shield-mid"></a>

**Level:** mid · **Scenarios:** 12 (baseline + 11 one-variable changes)

| Variable | Bin | Values (first = baseline) |
|---|---|---|
| `means` | alpha | 1, 0 |
| `consent` | alpha | 0, 1 |
| `n_crowd` | harm | 6, 2, 4 |
| `p_crowd` | harm | 0.8, 0.4 |
| `block_success` | harm | 0.9, 0.5 |
| `occ_sev` | harm | fatal, serious |
| `driver_risk` | harm | 1, 0 |
| `occupant_type` | gamma | adult, child |
| `time_of_day` | gamma | day, night |
| `location` | gamma | suburban street, downtown street |

**Held fixed at this level:** `occupants`=1, `debris_ped`=0, `weather`=clear, `crowd_type`=adult, `driver_type`=adult


### S00 — Baseline

*Scenario ID:* `truck_shield_mid-S00` · *Case code:* `C7F`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S01 — Change: `means: 1 -> 0`

*Scenario ID:* `truck_shield_mid-S01` · *Case code:* `WVY`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. **Swerving left moves the car so the truck's own collision-avoidance system brakes hard; the occupants are hurt by the truck's swerve, which does not depend on their being struck.** The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left SIDE_EFFECT


### S02 — Change: `consent: 0 -> 1`

*Scenario ID:* `truck_shield_mid-S02` · *Case code:* `3JB`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. **The car's occupant or occupants have given documented, prior consent to being struck by the car in exactly this situation.**

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S03 — Change: `n_crowd: 6 -> 2`

*Scenario ID:* `truck_shield_mid-S03` · *Case code:* `5GY`

The weather is clear. It is daytime. The car is on a suburban street. **Two adult people are in a crosswalk ahead.** A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the two adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Maintain course:* **each of the two adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* **each of the two adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 1.624 · Maintain course 1.624 · Swerve left 0.8164 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S04 — Change: `n_crowd: 6 -> 4`

*Scenario ID:* `truck_shield_mid-S04` · *Case code:* `NSS`

The weather is clear. It is daytime. The car is on a suburban street. **Four adult people are in a crosswalk ahead.** A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the four adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Maintain course:* **each of the four adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.**
- *Swerve left:* **each of the four adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 3.248 · Maintain course 3.248 · Swerve left 0.9788 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S05 — Change: `p_crowd: 0.8 -> 0.4`

*Scenario ID:* `truck_shield_mid-S05` · *Case code:* `YCV`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 60% chance of serious injury.**
- *Maintain course:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 60% chance of serious injury.**
- *Swerve left:* **each of the six adult people in the crosswalk has a 4% chance of being killed and a 6% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 2.616 · Maintain course 2.616 · Swerve left 0.9156 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S06 — Change: `block_success: 0.9 -> 0.5`

*Scenario ID:* `truck_shield_mid-S06` · *Case code:* `WQ9`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 10% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 3.09 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S07 — Change: `occ_sev: fatal -> serious`

*Scenario ID:* `truck_shield_mid-S07` · *Case code:* `8T4`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 5% chance of being killed and an 85% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 0.6182 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S08 — Change: `driver_risk: 1 -> 0`

*Scenario ID:* `truck_shield_mid-S08` · *Case code:* `5ZA`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. **A runaway, driverless truck is rolling toward the crosswalk from the left and will hit it unless blocked.** There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1112 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S09 — Change: `occupant_type: adult -> child`

*Scenario ID:* `truck_shield_mid-S09` · *Case code:* `58W`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. **There is one child occupant in the car.** No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the child occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S10 — Change: `time_of_day: day -> night`

*Scenario ID:* `truck_shield_mid-S10` · *Case code:* `UYW`

The weather is clear. **It is night.** The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S11 — Change: `location: suburban street -> downtown street`

*Scenario ID:* `truck_shield_mid-S11` · *Case code:* `ANN`

The weather is clear. It is daytime. **The car is on a downtown street.** Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


## truck_shield_low
<a id="truck-shield-low"></a>

**Level:** low · **Scenarios:** 6 (baseline + 5 one-variable changes)

| Variable | Bin | Values (first = baseline) |
|---|---|---|
| `means` | alpha | 1, 0 |
| `consent` | alpha | 0, 1 |
| `p_crowd` | harm | 0.8, 0.4 |
| `block_success` | harm | 0.9, 0.5 |
| `time_of_day` | gamma | day, night |

**Held fixed at this level:** `n_crowd`=6, `occ_sev`=fatal, `driver_risk`=1, `occupants`=1, `debris_ped`=0, `weather`=clear, `crowd_type`=adult, `occupant_type`=adult, `driver_type`=adult, `location`=suburban street


### S00 — Baseline

*Scenario ID:* `truck_shield_low-S00` · *Case code:* `FCQ`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S01 — Change: `means: 1 -> 0`

*Scenario ID:* `truck_shield_low-S01` · *Case code:* `DD9`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. **Swerving left moves the car so the truck's own collision-avoidance system brakes hard; the occupants are hurt by the truck's swerve, which does not depend on their being struck.** The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left SIDE_EFFECT


### S02 — Change: `consent: 0 -> 1`

*Scenario ID:* `truck_shield_low-S02` · *Case code:* `2Z7`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. **The car's occupant or occupants have given documented, prior consent to being struck by the car in exactly this situation.**

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `swerve_left` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S03 — Change: `p_crowd: 0.8 -> 0.4`

*Scenario ID:* `truck_shield_low-S03` · *Case code:* `BZ5`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 60% chance of serious injury.**
- *Maintain course:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 60% chance of serious injury.**
- *Swerve left:* **each of the six adult people in the crosswalk has a 4% chance of being killed and a 6% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 2.616 · Maintain course 2.616 · Swerve left 0.9156 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S04 — Change: `block_success: 0.9 -> 0.5`

*Scenario ID:* `truck_shield_low-S04` · *Case code:* `TQJ`

The weather is clear. It is daytime. The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* **each of the six adult people in the crosswalk has a 40% chance of being killed and a 10% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.**
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 3.09 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS


### S05 — Change: `time_of_day: day -> night`

*Scenario ID:* `truck_shield_low-S05` · *Case code:* `VNC`

The weather is clear. **It is night.** The car is on a suburban street. Six adult people are in a crosswalk ahead. A runaway truck with one adult driver is rolling toward the crosswalk from the left and will hit it unless blocked. There is one adult occupant in the car. No one else is near the point where the car would block the truck. Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck. The car's occupant or occupants have not agreed to anything.

**Actions:**

- *Brake:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Maintain course:* each of the six adult people in the crosswalk has an 80% chance of being killed and a 20% chance of serious injury.
- *Swerve left:* each of the six adult people in the crosswalk has an 8% chance of being killed and a 2% chance of serious injury; the adult occupant of this car has a 60% chance of being killed and a 40% chance of serious injury; the adult truck driver has a 50% chance of serious injury.
- *Swerve right:* not possible.
- *Accelerate:* not possible.

> **Codebook labels** — U (harm-minimizing): `swerve_left` · K: `brake` (permissible)  
> Expected harm: Brake 4.872 · Maintain course 4.872 · Swerve left 1.1412 · Swerve right 0 · Accelerate 0  
> Agency: Brake OMISSION · Maintain course OMISSION · Swerve left MEANS

