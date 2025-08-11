# Introduction to the user
print("Change your name case.")

name = input("Enter your full name: ")

lower = name.lower()
upper = name.upper()

print("Uppercase: ", upper,"\nLowercase:", lower)
print("Name length:",len(name))

# Without \n - everything prints on one line
print("Hello World How are you?")

# With \n - creates line breaks
print("Hello\nWorld\nHow are you?")

# You can combine \n with regular text
message = "Name: Ali\nAge: 20\nGrade: A"
print(message)

# Without \t - no spacing
print("Name Age Grade")
print("Ali 20 A")

# With \t - creates neat columns
print("Name\tAge\tGrade")
print("Ali\t20\tA")
print("Sarah\t19\tB+")
print("\n")
# Creating a formatted table
student_data = "Student Information:\n\nName\tAge\tGrade\nAli\t20\tA\nSarah\t19\tB+"
print(student_data)