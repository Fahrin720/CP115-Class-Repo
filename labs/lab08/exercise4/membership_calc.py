# Programs for calculating Fitness Membership Calculator
membership = 120
personal_training = 80
locker_rental = 25
towel_service = 15
first_time_register = 50

book_sessions = 6 * personal_training

total_first_month = membership + book_sessions + locker_rental + towel_service + first_time_register
total_next_month = total_first_month - first_time_register - book_sessions + personal_training
annual_cost = total_first_month + (total_next_month * 11)


print(total_first_month)
print(total_next_month)
print(annual_cost)


