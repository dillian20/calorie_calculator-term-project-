EXERCISE_MET_VALUES = {
    "walking": 3.8,      # Walking (flat, average speed)
    "running": 9.8,      # Running (average speed 9km/h)
    "cycling": 7.5,      # Bicycle riding (flat, 15-20km/h)
    "swimming": 8.0,     # Swim (medium speed)
    "yoga": 2.5,         #yoga
    "weightlifting": 6.0 # weight training
}

def get_met_value(exercise_name):
    """
    Enters an exercise name and returns the MET value for that exercise.
    """
    return EXERCISE_MET_VALUES.get(exercise_name.lower(), None)

def list_exercises():
    """
    Returns a list of supported exercises.
    """
    return list(EXERCISE_MET_VALUES.keys())
