import math

# Basic input and output
print("Welcome to the Students Circle Calculator.")
print("This program will calculate your circle area and circumference.")

# Getting user input (always returns a string)
circle_radius = float(input("Enter your circle radius: "))

# Calculations Group
circle_circumference = (2.0 * math.pi) * (circle_radius)
circle_area = math.pi * pow(circle_radius, 2)

# Formatted output using string concatenation
print("Your circle area is:", circle_area)
print("Your circle circumference is:", circle_circumference)