employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

salary_total = base_salary + (overtime_hours * 35)


# TODO your code here
if (tax_status == "Single") :
    if salary_total >= 5000:
        
elif (tax_status >= "Single") or (salary_total >= 6000):
    classification = 0.18
elif (gpa >= 2.0) :
    classification = "Head"


print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")