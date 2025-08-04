import math

# Basic input and output
print("Welcome to the Shopping Cost Calculator.")
print("This program will calculate your goods total.")

# Getting user input (always returns a string)
item1 = input("Enter your first item name: ")
item1_price = float(input("Enter your first item price: "))
item2 = input("Enter your second item name: ")
item2_price = float(input("Enter your second item price: "))
item3 = input("Enter your third item name: ")
item3_price = float(input("Enter your third item price: "))

quantity = 3
tax_rate = 0.06

# Calculations Group
subtotal = item1_price + item2_price + item3_price
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

# Formatted output using string concatenation
print("You've bought: " + item1 +","+ item2 +" and "+ item3)
print("Your subtotal is:", subtotal)
print("Your charged tax amount is:", tax_amount)
print("Your total cost is:", total_cost)