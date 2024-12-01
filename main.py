from calorie_calculator.calorie_burn import calculate_calories_to_burn, calculate_exercise_calories
from calorie_calculator.calorie_intake import calculate_bmr, calculate_tdee
from calorie_calculator.exercise_data import get_met_value, list_exercises

def main():
    print("=== calorie_calculator ===")
    
    # user
    current_weight = float(input("current weight(kg): "))
    target_weight = float(input("current weight(kg): "))
    height = float(input("length(cm): "))
    age = int(input("age: "))
    gender = input("gender(male/female): ").strip().lower()
    activity_level = input("activate (low/moderate/high/very high): ").strip().lower()
    
    # total calorie
    try:
        total_calories = calculate_calories_to_burn(current_weight, target_weight)
        print(f"\nTotal calories needed to lose your target weight: {total_calories:.2f} kcal")
    except ValueError as e:
        print(f"¿À·ù: {e}")
        return
    
    # Calculate Recommended Daily Intake
    try:
        bmr = calculate_bmr(current_weight, height, age, gender)
        tdee = calculate_tdee(bmr, activity_level)
        print(f"Recommended Daily Intake (TDEE): {tdee:.2f} kcal")
    except ValueError as e:
        print(f"error: {e}")
        return

    # Calculate calories burned by exercise
    print("\nList of supported exercises:")
    for exercise in list_exercises():
        print(f"- {exercise}")
    
    selected_exercise = input("\nChoose a exerise name: ").strip().lower()
    met_value = get_met_value(selected_exercise)
    if met_value is None:
        print("Selected exercise is not supported.")
        return

    duration_minutes = float(input("exercise times (ºÐ): "))
    exercise_calories = calculate_exercise_calories(current_weight, met_value, duration_minutes)
    print(f"\nDoing {selected_exercise} for {duration_minutes} minutes burns approximately {exercise_calories:.2f} kcal.")

if __name__ == "__main__":
    main()
