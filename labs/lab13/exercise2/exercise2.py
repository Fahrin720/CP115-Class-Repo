# Efficient search - stops immediately after finding target

for number in range(100):
    print(f'Checking number: {number}')
    if (number % 7 == 0 and number % 13 == 0 and number != 0):
        print(f'Found number! {number}')
        break  # Exit loop immediately
    print(f'Checking next number...')  # This runs before break
print("Search Complete")




















