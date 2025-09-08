# use_my_data.py
import labs.lab07.exercise3.shopping_data as shopping_data

# Use variables from my own module
print("=== Using My Own Module ===")
print(f"Name: {shopping_data.name}")
print(f"Price: ${shopping_data.price}")
print(f"Quantity: {shopping_data.quantity}")
print(f"Total Cost: ${shopping_data.total_cost}")
print(f"Name in UPPERCASE: {shopping_data.name_upper}")
print(f"Name length: {shopping_data.name_length} characters")