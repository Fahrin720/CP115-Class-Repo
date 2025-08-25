# Importing my own module and the data
import employee_data

basic = employee_data.basic_salary
overtime = employee_data.overtime_hours
rate = employee_data.overtime_rate

# Program for Salary Calculator

gross_salary = basic + (overtime * rate)
EPF = 0.11
SOCSO = 0.05
EIS = 0.02
medical_insurance =  50
parking_fee = 30 

total_deduction = (gross_salary * EPF) + (gross_salary * SOCSO) + (gross_salary * EIS) + medical_insurance + parking_fee

net_salary = gross_salary - total_deduction

print("The Salary payslip:\n")
print("EPF:", EPF,
"\nSOCSO:", SOCSO,
"\nEIS:", EIS,
"\nmedical_insurance:", medical_insurance,
"\nparking_fee:", parking_fee
)
print("\nTotal deduction:", total_deduction)
print("\nNet salary:\n", net_salary)


















