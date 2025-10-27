correct_password = "python123"

# Password validation with break
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted!")
        break  # Exit immediately

    print(f"Wrong password. {3 - attempts} attempts remaining.")
