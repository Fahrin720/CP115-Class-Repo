# Mohamed Fahrin Bin Mohamed Muneer C02
# Program to calculate the amount of bill with discount for PASU Telecomunication Company

monthly_usage = float(input("Enter monthly usage: "))

discount_rate = 0

# Testing condition from the highest
if monthly_usage > 100 :
    discount_rate = 0.2
elif monthly_usage >= 50 :
    discount_rate = 0.05
else :
    discount_rate = 0


discount = discount_rate * monthly_usage
bill_amount = monthly_usage - discount

print(f"Total bill to be paid with discount: {bill_amount}")





























