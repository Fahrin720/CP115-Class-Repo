position = input("Enter your position: ")
overtime_hours = int(input("Enter overtime hours: "))
is_weekend = input("Is it weeekend (True or False): ")

hourly_rate = 0
weekend_bonus = 0
overtime_rate = 1.5

if (position == "Manager") :
    hourly_rate = 35
elif position == "Supervisor" :
    hourly_rate = 25
elif position == "Staff" :
    hourly_rate = 18

if is_weekend == "True" :
    weekend_bonus = 5
elif is_weekend == "False" :
    weekend_bonus = 0

overtime_pay = overtime_hours * hourly_rate
total_pay = overtime_pay + (overtime_hours * weekend_bonus)



print(f"Hourly rate: {hourly_rate}")
print(f"Overtime pay is: {overtime_pay}")
print(f"Total pay is : {total_pay}")