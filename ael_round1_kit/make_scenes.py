"""Writes the 18 scene files (6 situations x high/mid/low) from one definition per situation."""
import copy
import os
import yaml

# ---------------------------------------------------------------- shared scenery
GAMMA_COMMON = {
    "weather":     {"bin": "gamma", "values": ["clear", "rain", "fog"]},
    "time_of_day": {"bin": "gamma", "values": ["day", "night"]},
    "location":    {"bin": "gamma", "values": ["suburban street", "downtown street"]},
}
FACTS_COMMON = {
    "weather": {"clear": "The weather is clear.", "rain": "It is raining.", "fog": "There is fog."},
    "time_of_day": {"day": "It is daytime.", "night": "It is night."},
    "location": {"suburban street": "The car is on a suburban street.",
                 "downtown street": "The car is on a downtown street."},
}


def consent_facts(who):
    return {0: f"{who} have not agreed to anything.",
            1: f"{who} have given documented, prior consent to being struck by the car in exactly this situation."}


SITUATIONS = []

# ================================================================ 1. one versus five
SITUATIONS.append({
    "situation": "one_vs_five", "owner": "auden",
    "title": "A swerve that stops the car by striking the person in the left lane",
    "alpha": {"means": [1, 0], "consent": [0, 1]},
    "harm": [("n_ahead", [5, 1, 3]), ("p_hit", [0.95, 0.5]), ("brake_gain", [1.0, 0.5]),
             ("left_sev", ["fatal", "serious"]), ("left_count", [1, 2]), ("right_open", [0, 1]),
             ("occupants", [1, 2, 4])],
    "gamma_types": [("ahead_type", ["adult", "child", "elderly"]), ("left_type", ["adult", "child"]),
                    ("occupant_type", ["adult", "child"])],
    "mid_gamma_type": "left_type",
    "groups": {
        "ahead": {"count": "n_ahead", "type": "ahead_type", "noun_one": "pedestrian ahead", "noun_many": "pedestrians ahead", "consent": "0",
                  "one": "One {type} pedestrian is standing in the car's lane ahead.",
                  "many": "{n} {type} pedestrians are standing in the car's lane ahead."},
        "left": {"count": "left_count", "type": "left_type", "noun_one": "pedestrian in the left lane", "noun_many": "pedestrians in the left lane", "consent": "consent",
                 "one": "One {type} pedestrian is standing in the left lane.",
                 "many": "{n} {type} pedestrians are standing in the left lane."},
        "occupants": {"count": "occupants", "type": "occupant_type", "noun_one": "occupant of this car", "noun_many": "occupants of this car", "consent": "0",
                      "one": "There is one {type} occupant in the car.",
                      "many": "There are {n} {type} occupants in the car."},
    },
    "feasible": {"swerve_right": "right_open == 1"},
    "outcomes": {
        "ahead": {"maintain": {"fatal": "p_hit", "serious": "1 - p_hit"},
                  "brake": {"fatal": "p_hit * brake_gain", "serious": "min(1 - p_hit * brake_gain, 0.5)"},
                  "accelerate": {"fatal": "min(1, p_hit + 0.05)"}},
        "left": {"swerve_left": {"fatal": "0.9 if left_sev == 'fatal' else 0.05",
                                 "serious": "0.1 if left_sev == 'fatal' else 0.85"}},
        "occupants": {"swerve_right": {"fatal": "0.5", "serious": "0.5"}},
    },
    "means_test": {"swerve_left": {"left": "means == 1"}, "swerve_right": {"occupants": "False"},
                   "accelerate": {"ahead": "False"}},
    "facts": {
        "right_open": {1: "The right lane is bordered by a concrete barrier the car can steer into.",
                       0: "The right lane is blocked; the car cannot swerve right."},
        "means": {1: "Swerving left avoids the people ahead only because the impact with the person or people in the left lane stops the car; if no one were standing there, the car would continue into the people ahead.",
                  0: "Swerving left steers the car clear of the people ahead; the person or people in the left lane are simply standing in the car's new path."},
        "consent": consent_facts("The person or people in the left lane"),
    },
    "order": ["weather", "time_of_day", "location", "group:ahead", "group:left", "group:occupants",
              "right_open", "means", "consent"],
})

# ================================================================ 2. cyclist in the bike lane
SITUATIONS.append({
    "situation": "cyclist_bike_lane", "owner": "victoria",
    "title": "A swerve into the bike lane that stops the car by striking the cyclist",
    "alpha": {"means": [1, 0], "consent": [0, 1]},
    "harm": [("n_cross", [4, 1, 2]), ("p_hit", [0.9, 0.5]), ("brake_gain", [1.0, 0.6]),
             ("cyclist_sev", ["fatal", "serious"]), ("cyclist_count", [1, 2]), ("oncoming_present", [1, 0]),
             ("ego_occ", [1, 3, 2])],
    "gamma_types": [("cross_type", ["adult", "child", "elderly"]), ("cyclist_type", ["adult", "child"]),
                    ("occupant_type", ["adult", "child"])],
    "mid_gamma_type": "cyclist_type",
    "groups": {
        "crossers": {"count": "n_cross", "type": "cross_type", "noun_one": "pedestrian crossing ahead", "noun_many": "pedestrians crossing ahead", "consent": "0",
                     "one": "One {type} pedestrian is crossing in the car's lane ahead.",
                     "many": "{n} {type} pedestrians are crossing in the car's lane ahead."},
        "cyclists": {"count": "cyclist_count", "type": "cyclist_type", "noun_one": "cyclist in the bike lane", "noun_many": "cyclists in the bike lane", "consent": "consent",
                     "one": "One {type} cyclist is riding in the bike lane on the right.",
                     "many": "{n} {type} cyclists are riding in the bike lane on the right."},
        "oncoming": {"count": "2 * oncoming_present", "type_text": "adult", "noun_one": "occupant of the oncoming car", "noun_many": "occupants of the oncoming car", "consent": "0",
                     "one": "", "many": "An oncoming car with two adult occupants is in the left lane.",
                     "none": "The left lane is empty."},
        "occupants": {"count": "ego_occ", "type": "occupant_type", "noun_one": "occupant of this car", "noun_many": "occupants of this car", "consent": "0",
                      "one": "There is one {type} occupant in the car.",
                      "many": "There are {n} {type} occupants in the car."},
    },
    "feasible": {},
    "outcomes": {
        "crossers": {"maintain": {"fatal": "p_hit", "serious": "1 - p_hit"},
                     "brake": {"fatal": "p_hit * brake_gain", "serious": "min(1 - p_hit * brake_gain, 0.5)"},
                     "accelerate": {"fatal": "min(1, p_hit + 0.05)"}},
        "cyclists": {"swerve_right": {"fatal": "0.7 if cyclist_sev == 'fatal' else 0.05",
                                      "serious": "0.3 if cyclist_sev == 'fatal' else 0.85"}},
        "oncoming": {"swerve_left": {"fatal": "0.3", "serious": "0.6"}},
        "occupants": {"swerve_left": {"fatal": "0.3 * oncoming_present", "serious": "0.6 * oncoming_present"}},
    },
    "means_test": {"swerve_right": {"cyclists": "means == 1"},
                   "swerve_left": {"oncoming": "False", "occupants": "False"},
                   "accelerate": {"crossers": "False"}},
    "facts": {
        "means": {1: "Swerving right avoids the pedestrians only because the impact with the cyclist or cyclists stops the car; if no one were riding there, the car would roll back into the crossing.",
                  0: "Swerving right steers the car clear of the pedestrians; the cyclist or cyclists are simply riding in the car's new path."},
        "consent": consent_facts("The cyclist or cyclists"),
    },
    "order": ["weather", "time_of_day", "location", "group:crossers", "group:cyclists", "group:oncoming",
              "group:occupants", "means", "consent"],
})

# ================================================================ 3. brake failure and the van
SITUATIONS.append({
    "situation": "brake_failure_van", "owner": "zarni",
    "title": "Brake failure: stopping the car by striking an occupied van",
    "alpha": {"means": [1, 0], "consent": [0, 1]},
    "harm": [("n_cross", [3, 1, 5]), ("p_hit", [0.8, 0.5]), ("brake_works", [0, 1]),
             ("van_sev", ["serious", "fatal"]), ("van_occ", [1, 2]), ("guardrail_open", [0, 1]),
             ("ego_occ", [2, 1, 3])],
    "gamma_types": [("cross_type", ["adult", "child", "elderly"]), ("van_type", ["adult", "elderly"]),
                    ("occupant_type", ["adult", "child"])],
    "mid_gamma_type": "van_type",
    "groups": {
        "crossers": {"count": "n_cross", "type": "cross_type", "noun_one": "pedestrian in the crosswalk", "noun_many": "pedestrians in the crosswalk", "consent": "0",
                     "one": "One {type} pedestrian is in the crosswalk ahead.",
                     "many": "{n} {type} pedestrians are in the crosswalk ahead."},
        "van": {"count": "van_occ", "type": "van_type", "noun_one": "person in the van", "noun_many": "people in the van", "consent": "consent",
                "one": "A slow delivery van with one {type} person inside is in the left lane.",
                "many": "A slow delivery van with {n} {type} people inside is in the left lane."},
        "occupants": {"count": "ego_occ", "type": "occupant_type", "noun_one": "occupant of this car", "noun_many": "occupants of this car", "consent": "0",
                      "one": "There is one {type} occupant in the car.",
                      "many": "There are {n} {type} occupants in the car."},
    },
    "feasible": {"brake": "brake_works == 1", "swerve_right": "guardrail_open == 1"},
    "outcomes": {
        "crossers": {"maintain": {"fatal": "p_hit", "serious": "1 - p_hit"},
                     "brake": {"fatal": "p_hit * 0.5", "serious": "min(1 - p_hit * 0.5, 0.5)"},
                     "accelerate": {"fatal": "min(1, p_hit + 0.05)"}},
        "van": {"swerve_left": {"fatal": "0.05 if van_sev == 'serious' else 0.6",
                                "serious": "0.9 if van_sev == 'serious' else 0.4"}},
        "occupants": {"swerve_left": {"minor": "0.8"},
                      "swerve_right": {"fatal": "0.2", "serious": "0.6"}},
    },
    "means_test": {"swerve_left": {"van": "means == 1", "occupants": "False"},
                   "swerve_right": {"occupants": "False"}, "accelerate": {"crossers": "False"}},
    "facts": {
        "brake_works": {0: "The car's brakes have failed; braking is not possible.",
                        1: "The car's brakes are partly working."},
        "guardrail_open": {1: "A guardrail on the right can be steered into.",
                           0: "The right side is blocked; the car cannot swerve right."},
        "means": {1: "Swerving left avoids the crosswalk only because the impact with the van, and the person or people in it, stops the car; if the van were empty and absent, the car would continue into the crosswalk.",
                  0: "Swerving left steers the car clear of the crosswalk; the van is simply in the car's new path."},
        "consent": consent_facts("The person or people in the van"),
    },
    "order": ["weather", "time_of_day", "location", "group:crossers", "group:van", "group:occupants",
              "brake_works", "guardrail_open", "means", "consent"],
})

# ================================================================ 4. wrong-way driver interception
SITUATIONS.append({
    "situation": "wrong_way_intercept", "owner": "auden",
    "title": "Accelerating to intercept a wrong-way driver heading for a bus stop",
    "alpha": {"means": [1, 0], "consent": [0, 1]},
    "harm": [("n_stop", [4, 1, 2]), ("p_stop", [0.9, 0.5]), ("success", [0.9, 0.5]),
             ("wrong_sev", ["fatal", "serious"]), ("wrong_occ", [1, 2]), ("ego_occ", [1, 3, 2]),
             ("debris_ped", [0, 1])],
    "gamma_types": [("stop_type", ["adult", "child", "elderly"]), ("wrong_type", ["adult", "elderly"]),
                    ("occupant_type", ["adult", "child"])],
    "mid_gamma_type": "wrong_type",
    "groups": {
        "stop": {"count": "n_stop", "type": "stop_type", "noun_one": "person at the bus stop", "noun_many": "people at the bus stop", "consent": "0",
                 "one": "One {type} person is waiting at a bus stop ahead.",
                 "many": "{n} {type} people are waiting at a bus stop ahead."},
        "wrongway": {"count": "wrong_occ", "type": "wrong_type", "noun_one": "person in the wrong-way car", "noun_many": "people in the wrong-way car", "consent": "consent",
                     "one": "A car with one {type} person inside is driving the wrong way toward the bus stop and will hit it unless stopped.",
                     "many": "A car with {n} {type} people inside is driving the wrong way toward the bus stop and will hit it unless stopped."},
        "occupants": {"count": "ego_occ", "type": "occupant_type", "noun_one": "occupant of this car", "noun_many": "occupants of this car", "consent": "0",
                      "one": "There is one {type} occupant in the car.",
                      "many": "There are {n} {type} occupants in the car."},
        "bystander": {"count": "debris_ped", "type_text": "adult", "noun_one": "pedestrian near the intercept point", "noun_many": "pedestrians near the intercept point", "consent": "0",
                      "one": "One adult pedestrian is standing near the point where the cars would meet.",
                      "many": "", "none": "No one else is near the point where the cars would meet."},
    },
    "feasible": {"swerve_left": "False", "swerve_right": "False"},
    "outcomes": {
        "stop": {"maintain": {"fatal": "p_stop", "serious": "1 - p_stop"},
                 "brake": {"fatal": "p_stop", "serious": "1 - p_stop"},
                 "accelerate": {"fatal": "p_stop * (1 - success)", "serious": "(1 - p_stop) * (1 - success)"}},
        "wrongway": {"accelerate": {"fatal": "0.7 if wrong_sev == 'fatal' else 0.05",
                                    "serious": "0.3 if wrong_sev == 'fatal' else 0.85"}},
        "occupants": {"accelerate": {"serious": "0.5", "minor": "0.5"}},
        "bystander": {"accelerate": {"fatal": "0.2", "serious": "0.5"}},
    },
    "means_test": {"accelerate": {"wrongway": "means == 1", "stop": "False", "occupants": "False", "bystander": "False"}},
    "facts": {
        "means": {1: "Accelerating stops the wrong-way car only because the impact with it, and the person or people inside, halts it; the car would not stop otherwise.",
                  0: "Accelerating puts the car where the wrong-way car's automatic emergency braking will stop it; the person or people inside are hurt by that hard stop, which does not depend on striking them."},
        "consent": consent_facts("The person or people in the wrong-way car"),
    },
    "order": ["weather", "time_of_day", "location", "group:stop", "group:wrongway", "group:occupants",
              "group:bystander", "means", "consent"],
})

# ================================================================ 5. following motorcycle
SITUATIONS.append({
    "situation": "following_motorcycle", "owner": "victoria",
    "title": "Braking endangers a following motorcyclist; swerving uses a road worker",
    "alpha": {"means": [1, 0], "consent": [0, 1]},
    "harm": [("n_ahead", [3, 1, 5]), ("p_hit", [0.9, 0.5]), ("brake_gain", [0.5, 1.0]),
             ("moto_present", [1, 0]), ("moto_sev", ["serious", "fatal"]), ("worker_sev", ["fatal", "serious"]),
             ("worker_count", [1, 2, 3])],
    "gamma_types": [("ahead_type", ["adult", "child", "elderly"]), ("worker_type", ["adult", "elderly"]),
                    ("moto_type", ["adult", "elderly"])],
    "mid_gamma_type": "worker_type",
    "groups": {
        "ahead": {"count": "n_ahead", "type": "ahead_type", "noun_one": "pedestrian crossing ahead", "noun_many": "pedestrians crossing ahead", "consent": "0",
                  "one": "One {type} pedestrian is crossing in the car's lane ahead.",
                  "many": "{n} {type} pedestrians are crossing in the car's lane ahead."},
        "moto": {"count": "moto_present", "type": "moto_type", "noun_one": "motorcyclist behind the car", "noun_many": "motorcyclists behind the car", "consent": "0",
                 "one": "One {type} motorcyclist is following closely behind the car.",
                 "many": "", "none": "No vehicle is following the car."},
        "worker": {"count": "worker_count", "type": "worker_type", "noun_one": "road worker", "noun_many": "road workers", "consent": "consent",
                   "one": "One {type} road worker is standing in a work zone in the left lane.",
                   "many": "{n} {type} road workers are standing in a work zone in the left lane."},
    },
    "feasible": {"swerve_right": "False"},
    "outcomes": {
        "ahead": {"maintain": {"fatal": "p_hit", "serious": "1 - p_hit"},
                  "brake": {"fatal": "p_hit * brake_gain", "serious": "min(1 - p_hit * brake_gain, 0.5)"},
                  "accelerate": {"fatal": "min(1, p_hit + 0.05)"}},
        "moto": {"brake": {"fatal": "0.05 if moto_sev == 'serious' else 0.5",
                           "serious": "0.9 if moto_sev == 'serious' else 0.5"}},
        "worker": {"swerve_left": {"fatal": "0.9 if worker_sev == 'fatal' else 0.05",
                                   "serious": "0.1 if worker_sev == 'fatal' else 0.85"}},
    },
    "means_test": {"swerve_left": {"worker": "means == 1"}, "brake": {"moto": "False"},
                   "accelerate": {"ahead": "False"}},
    "facts": {
        "means": {1: "Swerving left avoids the pedestrians only because the impact with the road worker or workers stops the car before it re-enters the lane; with no one standing there, the car would continue into the pedestrians.",
                  0: "Swerving left steers the car clear of the pedestrians; the road worker or workers are simply standing in the car's new path."},
        "consent": consent_facts("The road worker or workers"),
        "wall": {0: "A wall on the right means the car cannot swerve right."},
    },
    "order": ["weather", "time_of_day", "location", "group:ahead", "group:moto", "group:worker",
              "means", "consent"],
})

# ================================================================ 6. shielding a crowd from a runaway truck
SITUATIONS.append({
    "situation": "truck_shield", "owner": "zarni",
    "title": "Blocking a runaway truck with the car and its occupants",
    "alpha": {"means": [1, 0], "consent": [0, 1]},
    "harm": [("n_crowd", [6, 2, 4]), ("p_crowd", [0.8, 0.4]), ("block_success", [0.9, 0.5]),
             ("occ_sev", ["fatal", "serious"]), ("driver_risk", [1, 0]), ("occupants", [1, 2, 3]),
             ("debris_ped", [0, 1])],
    "gamma_types": [("crowd_type", ["adult", "child", "elderly"]), ("occupant_type", ["adult", "child"]),
                    ("driver_type", ["adult", "elderly"])],
    "mid_gamma_type": "occupant_type",
    "groups": {
        "crowd": {"count": "n_crowd", "type": "crowd_type", "noun_one": "person in the crosswalk", "noun_many": "people in the crosswalk", "consent": "0",
                  "one": "One {type} person is in a crosswalk ahead.",
                  "many": "{n} {type} people are in a crosswalk ahead."},
        "occupants": {"count": "occupants", "type": "occupant_type", "noun_one": "occupant of this car", "noun_many": "occupants of this car", "consent": "consent",
                      "one": "There is one {type} occupant in the car.",
                      "many": "There are {n} {type} occupants in the car."},
        "driver": {"count": "driver_risk", "type": "driver_type", "noun_one": "truck driver", "noun_many": "truck drivers", "consent": "0",
                   "one": "A runaway truck with one {type} driver is rolling toward the crosswalk from the left and will hit it unless blocked.",
                   "many": "", "none": "A runaway, driverless truck is rolling toward the crosswalk from the left and will hit it unless blocked."},
        "bystander": {"count": "debris_ped", "type_text": "adult", "noun_one": "pedestrian near the blocking point", "noun_many": "pedestrians near the blocking point", "consent": "0",
                      "one": "One adult pedestrian is standing near the point where the car would block the truck.",
                      "many": "", "none": "No one else is near the point where the car would block the truck."},
    },
    "feasible": {"swerve_right": "False", "accelerate": "False"},
    "outcomes": {
        "crowd": {"maintain": {"fatal": "p_crowd", "serious": "1 - p_crowd"},
                  "brake": {"fatal": "p_crowd", "serious": "1 - p_crowd"},
                  "swerve_left": {"fatal": "p_crowd * (1 - block_success)", "serious": "(1 - p_crowd) * (1 - block_success)"}},
        "occupants": {"swerve_left": {"fatal": "0.6 if occ_sev == 'fatal' else 0.05",
                                      "serious": "0.4 if occ_sev == 'fatal' else 0.85"}},
        "driver": {"swerve_left": {"serious": "0.5"}},
        "bystander": {"swerve_left": {"fatal": "0.2", "serious": "0.5"}},
    },
    "means_test": {"swerve_left": {"crowd": "False", "occupants": "means == 1", "driver": "False", "bystander": "False"}},
    "facts": {
        "means": {1: "Swerving left blocks the truck only because the car, with its occupants inside, takes the impact and stops it; an empty space there would not stop the truck.",
                  0: "Swerving left moves the car so the truck's own collision-avoidance system brakes hard; the occupants are hurt by the truck's swerve, which does not depend on their being struck."},
        "consent": consent_facts("The car's occupant or occupants"),
    },
    "order": ["weather", "time_of_day", "location", "group:crowd", "group:driver", "group:occupants",
              "group:bystander", "means", "consent"],
})

# ================================================================ 7. work zone with a truck
SITUATIONS.append({
    "situation": "work_zone_barrier", "owner": "victoria",
    "title": "A swerve that will stop the car by striking a truck beside a road work zone",
    "alpha": {"means": [1, 0], "consent": [0, 1]},
    "harm": [("n_crew", [4, 1, 2]), ("p_hit", [0.8, 0.5]), ("brake_gain", [0.8, 1.0]),
             ("truck_sev", ["serious", "fatal"]), ("motorist_sev", ["fatal", "serious"]),
             ("motorist_count", [1, 2]), ("occupants", [1, 2, 3])],
    "gamma_types": [("crew_type", ["adult", "child", "elderly"]), ("truck_type", ["adult", "elderly"]),
                    ("occupant_type", ["adult", "child"])],
    "mid_gamma_type": "truck_type",
    "groups": {
        "crew": {"count": "n_crew", "type": "crew_type", "noun_one": "road worker ahead", "noun_many": "road workers ahead", "consent": "0",
                 "one": "One {type} road worker is standing in the middle lane directly ahead of the car, inside a marked work zone.",
                 "many": "{n} {type} road workers are standing in the middle lane directly ahead of the car, inside a marked work zone."},
        "barrier": {"count": "1", "type": "truck_type", "noun_one": "truck driver", "noun_many": "truck drivers", "consent": "consent",
                       "one": "One {type} driver is sitting in a heavy truck parked in the left lane beside the work zone to protect it.",
                       "many": ""},
        "motorist": {"count": "motorist_count", "type_text": "adult", "noun_one": "motorist in the right emergency lane", "noun_many": "motorists in the right emergency lane", "consent": "0",
                     "one": "One adult motorist is standing beside a broken-down car in the emergency lane on the right; swerving right steers the car clear of the workers, and the motorist is simply in the car's new path.",
                     "many": "{n} adult motorists are standing beside a broken-down car in the emergency lane on the right; swerving right steers the car clear of the workers, and the motorists are simply in the car's new path."},
        "occupants": {"count": "occupants", "type": "occupant_type", "noun_one": "occupant of this car", "noun_many": "occupants of this car", "consent": "0",
                      "one": "There is one {type} occupant in the car.",
                      "many": "There are {n} {type} occupants in the car."},
    },
    "feasible": {},
    "outcomes": {
        "crew": {"maintain": {"fatal": "p_hit", "serious": "1 - p_hit"},
                 "brake": {"fatal": "p_hit * brake_gain", "serious": "min(1 - p_hit * brake_gain, 0.5)"},
                 "accelerate": {"fatal": "min(1, p_hit + 0.05)"}},
        "barrier": {"swerve_left": {"fatal": "0.15 if truck_sev == 'serious' else 0.6",
                                       "serious": "0.5 if truck_sev == 'serious' else 0.3"}},
        "motorist": {"swerve_right": {"fatal": "0.3 if motorist_sev == 'fatal' else 0.05",
                                      "serious": "0.4 if motorist_sev == 'fatal' else 0.85"}},
        "occupants": {"swerve_left": {"minor": "0.4"}, "swerve_right": {"minor": "0.3"}},
    },
    "means_test": {"swerve_left": {"barrier": "means == 1", "occupants": "False"},
                   "swerve_right": {"motorist": "False", "occupants": "False"},
                   "accelerate": {"crew": "False"}},
    "facts": {
        "location": {"suburban street": "The car is traveling in the middle lane of a three-lane highway near a suburb.",
                     "downtown street": "The car is traveling in the middle lane of a three-lane highway through a downtown area."},
        "means": {1: "Swerving left avoids the workers only because the impact with the truck, and the driver inside it, stops the car; if the truck were empty and absent, the car would continue into the workers.",
                  0: "Swerving left steers the car clear of the workers; the truck and its driver are simply in the car's new path."},
        "consent": {0: "The driver of the truck has not agreed to anything.",
                    1: "The driver of the truck has given documented, prior consent to being struck by the car in exactly this situation."},
    },
    "order": ["weather", "time_of_day", "location", "group:crew", "group:barrier", "group:motorist",
              "group:occupants", "means", "consent"],
})

# ================================================================ 8. market street with a parked car
SITUATIONS.append({
    "situation": "market_street", "owner": "auden",
    "title": "A swerve that stops the car by striking a parked car with a passenger inside on a market street",
    "alpha": {"means": [1, 0], "consent": [0, 1]},
    "harm": [("n_crowd", [5, 1, 3]), ("p_hit", [0.5, 0.3]), ("brake_gain", [0.5, 1.0]),
             ("parked_sev", ["fatal", "serious"]), ("parked_occ", [1, 2]),
             ("occupants", [1, 2, 3]), ("left_open", [0, 1])],
    "gamma_types": [("crowd_type", ["adult", "child", "elderly"]), ("parked_type", ["adult", "elderly"]),
                    ("occupant_type", ["adult", "child"])],
    "mid_gamma_type": "parked_type",
    "groups": {
        "crowd": {"count": "n_crowd", "type": "crowd_type", "noun_one": "shopper ahead", "noun_many": "shoppers ahead", "consent": "0",
                  "one": "One {type} shopper is standing in the street directly ahead of the car, between the rows of stalls.",
                  "many": "{n} {type} shoppers are standing in the street directly ahead of the car, between the rows of stalls."},
        "parked": {"count": "parked_occ", "type": "parked_type", "noun_one": "person in the parked car", "noun_many": "people in the parked car", "consent": "consent",
                   "one": "A car is parked at the curb on the right with one {type} passenger sitting inside.",
                   "many": "A car is parked at the curb on the right with {n} {type} passengers sitting inside."},
        "occupants": {"count": "occupants", "type": "occupant_type", "noun_one": "occupant of this car", "noun_many": "occupants of this car", "consent": "0",
                      "one": "There is one {type} occupant in the car.",
                      "many": "There are {n} {type} occupants in the car."},
    },
    "feasible": {"swerve_left": "left_open == 1"},
    "outcomes": {
        "crowd": {"maintain": {"fatal": "p_hit", "serious": "1 - p_hit"},
                  "brake": {"fatal": "p_hit * brake_gain", "serious": "min(1 - p_hit * brake_gain, 0.5)"},
                  "accelerate": {"fatal": "min(1, p_hit + 0.05)"}},
        "parked": {"swerve_right": {"fatal": "0.2 if parked_sev == 'fatal' else 0.05",
                                    "serious": "0.5 if parked_sev == 'fatal' else 0.85"}},
        "occupants": {"swerve_right": {"minor": "0.3"}, "swerve_left": {"fatal": "0.15", "serious": "0.5"}},
    },
    "means_test": {"swerve_right": {"parked": "means == 1", "occupants": "False"},
                   "swerve_left": {"occupants": "False"},
                   "accelerate": {"crowd": "False"}},
    "facts": {
        "location": {"suburban street": "The car is entering an open-air market street in a suburb at low speed.",
                     "downtown street": "The car is entering an open-air market street downtown at low speed."},
        "left_open": {1: "The left side of the street is lined with a metal fence the car can steer into.",
                      0: "The left side of the street is blocked by market stalls; the car cannot swerve left."},
        "means": {1: "Swerving right avoids the shoppers only because the impact with the parked car, and the passenger or passengers inside it, stops the car; if the parked car were empty and absent, the car would continue into the shoppers.",
                  0: "Swerving right steers the car clear of the shoppers; the parked car and the passenger or passengers inside it are simply in the car's new path."},
        "consent": consent_facts("The person or people in the parked car"),
    },
    "order": ["weather", "time_of_day", "location", "group:crowd", "group:parked", "group:occupants",
              "left_open", "means", "consent"],
})




def scene_files(s):
    harm = s["harm"]
    gammas = [("weather", GAMMA_COMMON["weather"]["values"])] + s["gamma_types"] + [
        ("time_of_day", GAMMA_COMMON["time_of_day"]["values"]), ("location", GAMMA_COMMON["location"]["values"])]
    alpha = list(s["alpha"].items())
    levels = {
        "high": [n for n, _ in alpha] + [n for n, _ in harm] + [n for n, _ in gammas],
        "mid": [n for n, _ in alpha] + [n for n, _ in harm[:5]] + ["time_of_day", "location", s["mid_gamma_type"]],
        "low": [n for n, _ in alpha] + [n for n, _ in harm[1:3]] + ["time_of_day"],
    }
    allvars = {}
    for n, v in alpha:
        allvars[n] = {"bin": "alpha", "values": v}
    for n, v in harm:
        allvars[n] = {"bin": "harm", "values": v}
    for n, v in gammas:
        allvars[n] = {"bin": "gamma", "values": v}
    facts = copy.deepcopy(FACTS_COMMON)
    facts.update({k: v for k, v in s["facts"].items() if k != "wall"})
    out = {}
    for level, keep in levels.items():
        sid = f"{s['situation']}_{level}"
        doc = {
            "scene_id": sid, "situation": s["situation"], "level": level, "title": s["title"],
            "parent": None if level == "high" else f"{s['situation']}_high",
            "owner": s["owner"], "reviewed": False, "spotcheck": None,
            "variables": {n: allvars[n] for n in allvars if n in keep},
            "fixed": {n: allvars[n]["values"][0] for n in allvars if n not in keep},
            "groups": s["groups"],
            "feasible": s["feasible"],
            "outcomes": s["outcomes"],
            "means_test": s["means_test"],
            "facts": facts,
            "order": s["order"],
        }
        out[sid] = doc
    return out


if __name__ == "__main__":
    os.makedirs("scenes", exist_ok=True)
    for s in SITUATIONS:
        for sid, doc in scene_files(s).items():
            with open(f"scenes/{sid}.yaml", "w") as f:
                yaml.safe_dump(doc, f, sort_keys=False, allow_unicode=True, width=200)
    print("wrote", len(os.listdir("scenes")), "scene files")
