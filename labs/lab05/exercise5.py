print("Welcome to the Average Score Calculator!")
print("This program will calculate your scores,total and average.")

first_test = float(input("Enter your first exam score: "))
second_test = float(input("Enter your second exam score: "))
third_test = float(input("Enter the third exam score: "))

total_score = first_test + second_test + third_test
average_score = total_score / 3 


print()
print("Your individual score for first test is: ", first_test, "%")
print("Your individual score for second test is: ", second_test, "%")
print("Your individual score for third test is: ", third_test)
print("Your total score: ", total_score, "%" )
print("Your average score: ", average_score, "%")