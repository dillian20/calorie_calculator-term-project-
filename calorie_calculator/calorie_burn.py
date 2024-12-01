def calculate_calories_to_burn(current_weight, target_weight):
    """
    Enter your current weight and target weight and calculate the total calories needed for weight loss.
    """
    calories_per_kg = 7700  # Calories needed per kg lost
    weight_loss = current_weight - target_weight
    if weight_loss <= 0:
        raise ValueError("Your goal weight is higher than your current weight.")
    return weight_loss * calories_per_kg

def calculate_exercise_calories(weight, exercise_met, duration_minutes):
    """
    Calculates calories burned by inputting body weight, MET value, and exercise time.
    """
    duration_hours = duration_minutes / 60
    return exercise_met * weight * duration_hours
