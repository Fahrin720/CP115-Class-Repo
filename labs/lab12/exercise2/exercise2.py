score = float(input("Enter score (from 0-100): "))
total = 0
count = 0
average = 0


while (not score < 0 and not score > 100):  # Part 2: Condition
    total += score
    count += 1
    print(f"Current count: {count}")
    score = float(input("Enter score (from 0-100): "))


if count == 0:
    average = 0
else:
    average = total / count

print(f"The count is: {count}")
print(f"The total is: {total:.2f}")
print(f"The average is: {average:.2f}")

