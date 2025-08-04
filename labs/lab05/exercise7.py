import math

from math import sqrt, pow, sin, cos

print("Welcome to the Advanced Math Operations.")
print("This program will calculate number being square root, squared and cubed.")


number1 = float(input("Enter your number: "))

square_root = sqrt(number1)
squared = pow(number1, 2)
cubed = pow(number1, 3)

print("The number after square root:", square_root)
print("The number after squared:", squared)
print("The number after cubed:", cubed)