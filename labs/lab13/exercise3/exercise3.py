mark = float(input("Enter mark: "))
valid_count = 0
invalid_count = 0
sum_mark = 0

while mark > 0:
    if mark > 100:
        print('Invalid mark entered, skipped.')
        invalid_count += 1
        continue
    sum_mark += mark
    valid_count += 1
    mark = input("Enter mark: ")
    average = sum_mark / valid_count


print(f'Valid number entered: {valid_count}')
print(f"The average is: {average:.2f}")









