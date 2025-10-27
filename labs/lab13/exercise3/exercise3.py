mark = int(input("Enter mark: "))
valid_count = sum_mark = 0


while mark > 0:
    if mark > 100:
        print('Invalid mark entered, skipped.')
        continue
    else :
        valid_count += 1
    sum_mark += mark
    mark = input("Enter mark: ")

if valid_count == 0:
    average = 0
else:
    average = sum_mark / valid_count


print(f'Valid number entered: {valid_count}')
print(f"The average is: {average:.2f}")









