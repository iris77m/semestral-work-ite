# Testing

Back to the [README](../README.md).

## Approach and rationale

The program has two clearly separated parts, so each one is tested in the most suitable way:

- **Unit tests for the formulas** (`tests/test_calculator.py`). The functions in `src/calculator.py` are pure logic (they receive numbers and return a result), so they are tested with known inputs and expected outputs. Each function is checked with:
  - A normal case
  - **Boundary values** (for example BMI 18.5 and 30, or the limits between heart rate zones)
  - **Invalid input**, which must raise `ValueError`.
- **Interface tests** (`tests/test_interface.py`). The menu uses `input()` and `print()`, so the user is simulated with `unittest.mock.patch`: the test supplies a list of typed answers and checks the printed text. This tests full flows (menu, questions, result), the retry after an invalid number or option, and the exit option.

**Why this strategy:** the program is small and deterministic, so automatic example-based tests are enough to verify that every formula is correct and that the interface does not break with wrong input. Separating logic from interface makes the formulas testable without typing anything.

**Framework:** `unittest` from the standard library (no extra dependencies).

**How to run all tests:**

```bash
python test_main.py
```

`test_main.py` discovers and runs every test in the `tests/` folder and exits with an error code if any test fails.

## Sample input/output pairs

### Formulas

| Function | Input | Expected output |
|---|---|---|
| `calculate_bmi` | 70 kg, 175 cm | 22.9 |
| `calculate_bmi` | 0 kg, 175 cm | `ValueError` |
| `classify_bmi` | 17.0 | Underweight |
| `classify_bmi` | 18.5 | Normal weight |
| `classify_bmi` | 27.0 | Overweight |
| `classify_bmi` | 30.0 | Obesity |
| `max_heart_rate` | age 30 | 187 bpm |
| `heart_rate_zone` | age 30, 80 bpm | Zone 0 (rest) |
| `heart_rate_zone` | age 30, 140 bpm | Zone 3 (Moderate),74.9% |
| `heart_rate_zone` | age 30, 187 bpm | Zone 5 |
| `heart_rate_zone` | age 30, 0 bpm | `ValueError` |
| `calculate_bmr` | male, 70 kg, 175 cm, 30 years | 1648.75 |
| `calculate_bmr` | female, 70 kg, 175 cm, 30 years | 1482.75 |
| `calculate_daily_calories` | male, 70, 175, 30, level 3, maintain | 2556 kcal |
| `calculate_daily_calories` | male, 70, 175, 30, level 3, lose | 2056 kcal |
| `calculate_daily_calories` | male, 70, 175, 30, level 3, gain | 2856 kcal |
| `calculate_daily_calories` | male, 70, 175, 30, level 9, lose | `ValueError` |
| `calculate_daily_water` | 70 kg, 0 min | 2450 ml |
| `calculate_daily_water` | 70 kg, 60 min | 2950 ml |
| `calculate_daily_water` | -5 kg, 10 min | `ValueError` |

### Interface (typed answers in order)

| Typed input | Expected printed output |
|---|---|
| `0` | Goodbye! |
| `1`, `70`, `175`, `0` | Your BMI is 22.9 (Normal weight). |
| `2`, `30`, `140`, `0` | Result: Zone 3: Moderate |
| `3`, `m`, `70`, `175`, `30`, `3`, `maintain`, `0` | Recommended daily calories: 2556 kcal |
| `4`, `70`, `60`, `0` | Recommended daily water: 2950 ml (2.95 L) |
| `9`, `0` | Invalid option message, then Goodbye! |
| `1`, `abc`, `70`, `175`, `0` | Invalid number message, then BMI 22.9 |
| `1`, `5`, `70`, `175`, `0` | "Value must be between 1 and 300" message, then BMI 22.9 |
| `2`, `30`, `190`, `0` | Error message about heart rate, then Goodbye! |

## Coverage explanation

- Every public function in `calculator.py` is tested with valid, boundary and invalid cases.
- All four menu options, the invalid-input retries and the exit option of `interface.py` are tested.
- Coverage was reviewed by hand against the list of functions; no coverage tool is used.
