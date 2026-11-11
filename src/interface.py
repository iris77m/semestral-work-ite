"""The interface:
it shows a menu, asks the user for the data needed by the chosen
calculation and prints the result.
"""

from src import calculators as calc


def ask_number(prompt, minimum, maximum):
    #ask for a number 
    while True:
        raw = input(prompt).strip().replace(",", ".") #elimina todo lo que no queremos como espacios y puntos
        try:
            value = float(raw) #si es texto da error
        except ValueError:
            print("Invalid number, try again.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Value must be between {minimum} and {maximum}.")


def ask_choice(prompt, valid_options):
    #asks for a str
    while True:
        answer = input(prompt).strip().lower()
        if answer in valid_options:
            return answer
        print(f"Invalid option. Choose one of: {', '.join(valid_options)}")


def run_bmi():
    #weight and height and print BMI and its category
    weight = ask_number("Weight (kg): ", 1, 300) #establishes limits of height and weight
    height = ask_number("Height (cm): ", 1, 300)
    bmi = calc.calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} ({calc.classify_bmi(bmi)}).")


def run_heart_zone():
    """Ask for age and current heart rate and print the training zone"""
    age = ask_number("Age (years): ", 1, 100)
    heart_rate = ask_number("Current heart rate (bpm): ", 30, 230)
    zone, description, percentage = calc.heart_rate_zone(age, heart_rate)
    print(f"Estimated max heart rate: {calc.max_heart_rate(age)} bpm")
    print(f"You are at {percentage}% of your maximum.")
    print(f"Result: {description}")


def run_calories():
    """Personal data, activity and goal; print daily calories."""
    sex_key = ask_choice("Sex (m/f): ", ["m", "f"])
    sex = "male" if sex_key == "m" else "female"
    weight = ask_number("Weight (kg): ", 1, 300)
    height = ask_number("Height (cm): ", 1, 300)
    age = ask_number("Age (years): ", 1, 100)
    print("Activity level: 1:sedentary, 2:light, 3:moderate, "
          "4:high, 5:very high")
    activity = int(ask_number("Activity level (1-5): ", 1, 5))
    goal_key = ask_choice("Goal (lose/maintain/gain): ",
                          ["lose", "maintain", "gain"])
    kcal = calc.calculate_daily_calories(sex, weight, height, age,
                                         activity, goal_key)
    print(f"Recommended daily calories: {kcal} kcal")


def run_water():
    """Ask for weight and exercise time; print daily water in litres."""
    weight = ask_number("Weight (kg): ", 1, 300)
    minutes = ask_number("Exercise minutes per day: ", 0, 1000)
    ml = calc.calculate_daily_water(weight, minutes)
    print(f"Recommended daily water: {ml} ml ({ml / 1000:.2f} L)")


MENU = """
---> Human Calculator <---
1) BMI calculator
2) Heart rate training zone
3) Daily calories
4) Daily water
0) Exit
"""

ACTIONS = {"1": run_bmi, "2": run_heart_zone, "3": run_calories,
           "4": run_water}

def main_menu():
    while True:
        print(MENU)
        choice = ask_choice("Choose an option: ", ["0", "1", "2", "3", "4"])
        if choice == "0":
            print("Goodbye!")
            return
        ACTIONS[choice]()