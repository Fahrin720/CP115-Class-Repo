price = float(input("Enter item price (-1 to stop): "))
total_cost = 0
item_count = 0

while price != -1:  # Part 2: Condition
    print(f"Item price: {price}")
    price = float(input("Enter next item price (-1 to stop): "))
    total_cost += price
    item_count += 1

print(f"Item count is: {item_count}")
print(f"Total cost is: {total_cost:.2f}")
