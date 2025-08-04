import random

# Basic input and output
print("Welcome to the Random Student Selector.")
print("This program will Generates a random number and displays class information.")

# Getting user input (always returns a string)
class_name = input("Enter your class name: ")

# Calculations Group
class_number = random.randint(1,100)

# Formatted output using string concatenation
print()
print("Your class number is:", class_number)
print("Your class name is: " + class_name)