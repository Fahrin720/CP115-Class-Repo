# Creating a formatted table
student_data = """========== RECEIPT ==========\n\nItem\tPrice\tQty\tTotal
\nCoffee\t$3.50\t2\t$7.00\n\n============================"""
print(student_data)
print("\n\n")

# This is a comment - it won't run
print("Hello World")  # This comment explains what the print does

# You can use comments to explain variables
student_name = "Ali"  # Store the student's name
age = 20             # Student's age in years

# Comments can temporarily disable code
# print("This line won't execute")
print("This line will execute\n")

# This is a multi-line comment
# that spans several lines.
# Each line needs its own # symbol.
# This is the most common way.

print("Code after comments\n")

"""
This is a multi-line comment using triple quotes.
You can write multiple lines without using # on each line.
This is technically a string, but if it's not assigned to a variable,
Python ignores it, making it act like a comment.
"""

print("Code after triple quote comment\n\n")

'''
You can also use triple single quotes
for multi-line comments.
Both work the same way.
'''