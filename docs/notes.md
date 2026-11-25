# Formulas and Mathematical Notes

Back to the [README](../README.md).

This document explains the mathematical models, constants, and clinical/sports classification thresholds implemented in `src/calculator.py`.

---

## 1. Body Mass Index (BMI)

**Functions:** `calculate_bmi(weight_kg, height_cm)` and `classify_bmi(bmi)`

### Formula
First, height is converted from centimeters to meters, and then weight is divided by the square of height:

$$\text{height}_m = \frac{\text{height}_{cm}}{100}$$

$$\text{BMI} = \frac{\text{weight}_{kg}}{(\text{height}_m)^2}$$

The final BMI value is rounded to **1 decimal place** (`round(bmi, 1)`).

### Classification Thresholds (WHO Standard)
| BMI Range ($\text{kg/m}^2$) | Category |
|---|---|
| $< 18.5$ | Underweight |
| $18.5 \le \text{BMI} < 25.0$ | Normal weight |
| $25.0 \le \text{BMI} < 30.0$ | Overweight |
| $\ge 30.0$ | Obesity |

---

## 2. Maximum Heart Rate & Training Zones

**Functions:** `max_heart_rate(age)` and `heart_rate_zone(age, heart_rate)`

### Maximum Heart Rate Formula (Tanaka Equation)
Instead of the traditional $220 - \text{age}$ rule, the program uses the **Tanaka formula**, which provides a more accurate age-predicted maximum heart rate ($\text{HR}_{\max}$) for adults:

$$\text{HR}_{\max} = 208 - (0.7 \times \text{age})$$

The result is rounded to the nearest integer (`round(heart_rate)`).

### Training Zone Calculation
Given a current heart rate ($\text{HR}$), where $1 \le \text{HR} \le \text{HR}_{\max}$, the relative intensity percentage is calculated as:

$$\%\text{HR}_{\max} = \left(\frac{\text{HR}}{\text{HR}_{\max}}\right) \times 100$$

| Zone | Intensity Range ($\%\text{HR}_{\max}$) | Description |
|---|---|---|
| **Zone 0** | $< 50\%$ | Rest |
| **Zone 1** | $50\% \le \% < 60\%$ | Recovery |
| **Zone 2** | $60\% \le \% < 70\%$ | Light |
| **Zone 3** | $70\% \le \% < 80\%$ | Moderate |
| **Zone 4** | $80\% \le \% < 90\%$ | Hard |
| **Zone 5** | $\ge 90\%$ | Max |

---

## 3. Basal Metabolic Rate (BMR) & Daily Calories

**Functions:** `calculate_bmr(sex, weight_kg, height_cm, age)` and `calculate_daily_calories(...)`

### Basal Metabolic Rate (Mifflin-St Jeor Equation)
The program estimates resting energy expenditure using the **Mifflin-St Jeor equation**:

$$\text{base} = (10 \times \text{weight}_{kg}) + (6.25 \times \text{height}_{cm}) - (5 \times \text{age})$$

- **Male:** $\text{BMR} = \text{base} + 5$
- **Female:** $\text{BMR} = \text{base} - 161$

### Total Daily Energy Expenditure (TDEE) & Goal Adjustment
To obtain daily maintenance calories, $\text{BMR}$ is multiplied by a weekly physical activity factor:

| Level | Activity Description | Multiplier |
|---|---|---|
| `1` | Sedentary | `1.2` |
| `2` | Light | `1.375` |
| `3` | Moderate | `1.55` |
| `4` | High | `1.725` |
| `5` | Very high | `1.9` |

Finally, a caloric offset is applied depending on the user's weight goal, and the result is rounded to the nearest whole calorie:

$$\text{Daily Calories} = \text{round}\big((\text{BMR} \times \text{multiplier}) + \text{goal\_offset}\big)$$

| Goal | Caloric Offset ($\text{kcal/day}$) |
|---|---|
| `"lose"` | `-500` |
| `"maintain"` | `0` |
| `"gain"` | `+300` |

---

## 4. Daily Water Intake

**Function:** `calculate_daily_water(weight_kg, exercise_minutes)`

### Formula
Daily hydration combines a resting baseline proportional to body weight ($35\text{ ml/kg}$) plus an additional allowance for physical exercise ($500\text{ ml}$ per hour of sport):

$$\text{Base Water (ml)} = \text{weight}_{kg} \times 35$$

$$\text{Exercise Extra (ml)} = \left(\frac{\text{exercise\_minutes}}{60}\right) \times 500$$

$$\text{Daily Water (ml)} = \text{round}(\text{Base Water} + \text{Exercise Extra})$$

The CLI interface displays this value both in **milliliters** (`ml`) and converted to **liters** ($\text{ml} / 1000$).