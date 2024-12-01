def calculate_bmr(weight, height, age, gender):
    """
    Calculate your basal metabolic rate (BMR) using the Mifflin-St Jeor formula.
    """
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == "female":
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Gender must be entered as 'male' or 'female'.")

def calculate_tdee(bmr, activity_level):
    """
    Calculate your Total Daily Energy Expenditure (TDEE) by taking into account your activity level.
    """
    activity_multipliers = {
        "low": 1.2,"moderate": 1.375,"high": 1.55,"very high": 1.725
    }
    if activity_level not in activity_multipliers:
        raise ValueError("Activity level must be one of 'low', 'moderate', 'high', or 'very high'.")
    return bmr * activity_multipliers[activity_level]
