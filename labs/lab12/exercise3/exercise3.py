
age_input = (input("Enter age in range 1-120 (enter done to stop): "))
total_age = 0
age_count = 0
average_age = 0
total = 0

while (not age_input == "done") :
    total += int(age_input)
    total_age += total
    age_count += 1
    print(f"Current count: {age_count}")
    age_input = (input("Enter age (enter done to stop): "))

if age_count == 0:
    average_age = 0
else:
    average_age = total_age / age_count



print(f"The age count is: {age_count}")
print(f"The total age is: {total_age}")
print(f"The average age is: {average_age:.2f}")




