# Password validation with break
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    attempts += 1

    if password == "secret123":
        print("Access granted!\n\n")
        break  # Exit immediately

    print(f"Wrong password. {3 - attempts} attempts remaining.\n\n")


# Solution: Skip number 3 with continue
total = 0

for number in range(5):
    print(f'Processing: {number}')

    if number == 3:
        print('Skipping 3!')
        continue  # Skip to next iteration

    total += number  # This line skipped when continue executes
    print(f'Added {number}. Current total: {total}')  # This too

print(f'Final total: {total}\n\n')  # Python continues here after each iteration

# Using continue - processes all, reports only numbers > 7
for number in range(10):
    if number <= 7:
        continue  # Skip numbers <= 7
    print(f'Number greater than 7: {number}')  # Reports 8 and 9

print('Processing complete')
























