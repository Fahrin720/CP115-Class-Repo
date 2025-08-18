# New way using f-strings
student_name = "Ali"
age = 20
grade = 85.5

print(f"\nStudent: {student_name}")
print(f"Age: {age}")
print(f"Grade: {grade}%")

name = "Sarah"
score = 92

# The f tells Python this is an f-string
# The {} tells Python to put the variable value here
message = f"\n\nHello {name}, your score is {score}"
print(message)