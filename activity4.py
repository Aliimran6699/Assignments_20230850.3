score = int(input("Enter the score (0-100): "))
while score < 0 or score > 100:
    score = int(input("Invalid input. Enter the score (0-100): "))
grade = ""
while True:
    if score >= 80:
        grade = "A"
        break
    elif score >= 60:
        grade = "B"
        break
    elif score >= 50:
        grade = "C"
        break
    else:
        grade = "Fail"
        break

print("Grade:",grade)