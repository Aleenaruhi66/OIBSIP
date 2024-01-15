def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.

    Formula: BMI = weight / (height^2)

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        float: BMI value.
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values.")

    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value and provide a basic categorization.

    Args:
        bmi (float): BMI value.

    Returns:
        str: Interpretation category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    try:
        # Get user input for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Interpret BMI
        interpretation = interpret_bmi(bmi)

        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Interpretation: {interpretation}")

    except ValueError as e:
        print(f"Error: {e}")