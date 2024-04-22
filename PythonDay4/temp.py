# Constant conversion factor
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0

# Get temperature in Fahrenheit from user input
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Print the result
print("Temperature in Celsius:", celsius)
