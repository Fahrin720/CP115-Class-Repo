age = int(input("Enter age: "))
accident_count = int(input("Enter accident count: "))

good_driver_discount = 0
base_premium = 0
accident_penalty = 0

if age > 50 :
    base_premium = 2000
elif age >= 25 :
    base_premium = 1800
else :
    base_premium = 2400

if accident_count >= 3 :
    accident_penalty = 600
elif accident_count >= 1 :
    accident_penalty = 300
else :
    accident_penalty = 0

if accident_count < 1 :
    good_driver_discount = 0.1

final_premium = base_premium + accident_penalty
discount_amount = good_driver_discount * final_premium

print(f"Base premium = {base_premium}")
print(f"Final premium = {final_premium}")
print(f"Discount amount = {discount_amount}")