score = (input("Enter score (enter end to stop): "))
pass_rate = 0
count = 0
pass_count = 0
pass_score = 0
fail_count = 0
total_score = 0

while (score != "end") :
    count += 1
    total_score += int(score)
    if (score >= 60) :
        print("Pass")
        pass_count += count
        pass_score += score
    else :
        print("Fail")
        fail_count += count
    
    score = int(input("Enter score (enter end to stop): "))

pass_rate = (pass_score / total_score) * 100

print(f"The passing count is: {pass_count}")
print(f"The failing count is: {fail_count}")
print(f"The pass rate is: {pass_rate:.2f}")


