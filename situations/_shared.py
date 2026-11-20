"""Definitions shared by several situations."""

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


# braking sentence shared by lane_edge and two_means
BRAKE_FACTS = {1.0: "The car is too close for braking to slow it before it reaches the people ahead.",
               0.5: "Braking can slow the car before it reaches the people ahead, but not stop it."}
