#necesary parameters
activity_multiplicator_list=[1.2,1.375,1.55,1.725,1.9]
    #each number corresponds to BMR depending on the physical activity WEEKLY (sedentary,light,moderate,high, very high)
goal_loose_weight={"lose":-500,"maintain":0,"gain":300}
    #this is a dictionary, contains the aim of the calories wanted to be loosed or gained
water_ml_per_kg=35
water_ml_per_kg_sporthours=500
heart_rate_zones={0:"Rest",1:"Zone 1: recovery",2:"Zone 2: light",3:"Zone 3: Moderate",4:"Zone 4:Hard",5:"Zone 5: Max"}

#BODY MASS INDEX--------------
def calculate_bmi(weight_kg, height_cm):
    #Body Mass Index calculation. Do not insert negative values, it will return a ValueError
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive values.")
    height_to_m = height_cm / 100
    bmi=weight_kg / (height_to_m ** 2)
    return round(bmi, 1) 
        #we round the final result to 1 decimal

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

#HEART RATE ZONES----------------
def max_heart_rate(age):
    #Maximum heart rate calculation based on age
    if age <= 0:
        raise ValueError("Age must be a positive value.")
    heart_rate = 208-0.7*age
    return round(heart_rate)

def heart_rate_zone(age, heart_rate):
    max_hr = max_heart_rate(age)
    if heart_rate < 0 or heart_rate > max_hr:
        raise ValueError("Heart rate must be between 0 and the maximum heart rate.")
    percentage = (heart_rate / max_hr) * 100
    if percentage < 50:
        zone =0
    elif 50 <= percentage < 60:
        zone = 1
    elif 60 <= percentage < 70:
        zone = 2
    elif 70 <= percentage < 80:
        zone = 3
    elif 80 <= percentage < 90:
        zone = 4
    else:
        zone = 5
    return zone, heart_rate_zones[zone], round(percentage,1)

#BODY METHABOLIC RATE----------------
def calculate_bmr(sex, weight_kg, height_cm, age):
    if sex not in ("male", "female"):
        raise ValueError("Sex must be 'male' or 'female'.")
    if weight_kg <= 0 or height_cm <= 0 or age <= 0:
        raise ValueError("Weight, height and age must be positive.")
    base = 10 * weight_kg + 6.25 * height_cm - 5 * age
    if sex=="male":
        return base + 5
    else:
        return base - 161
    #differences male and female because the eq is different
 
#DAILY CALORIES----------------will determinate how many cal based on your aim
def calculate_daily_calories(sex, weight_kg, height_cm, age,activity_level, goal):
    if activity_level not in activity_multiplicator_list:
        raise ValueError("Invalid activity level.")
    if goal not in goal_loose_weight:
        raise ValueError("Invalid goal.")
    bmr = calculate_bmr(sex, weight_kg, height_cm, age)
    maintenance = bmr * activity_level
    return round(maintenance + goal_loose_weight[goal])

#DAILY WATER-------------------------
def calculate_daily_water(weight_kg, exercise_minutes):
    if weight_kg <= 0:
        raise ValueError("Weight must be positive.")
    if exercise_minutes < 0:
        raise ValueError("Exercise minutes cannot be negative.")
    base = weight_kg * water_ml_per_kg
    extra = (exercise_minutes / 60) * water_ml_per_kg_sporthours
    return round(base + extra)

