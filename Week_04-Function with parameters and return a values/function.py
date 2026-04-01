def fahrenheit_to_kelvin(fahrenheit):
    """
    Calculates Kelvin from a Fahrenheit input.
    Args: fahrenheit (float)
    Returns: kelvin (float)
    """
    kelvin = (fahrenheit - 32) * (5/9) + 273.15
    return kelvin


try:
    f_input = float(input("Enter temperature in Fahrenheit: "))

    k_result = fahrenheit_to_kelvin(f_input)

    print(f"Temperature in Kelvin: {k_result:.2f}")

except ValueError:
    print("Invalid input! Please enter a numerical value.")