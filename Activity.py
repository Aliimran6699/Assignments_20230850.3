score= float(input("Enter the score"))
if score>=0 and score<=100:

    print("valid score")
    if score>=80:
        print("A")
    if score>=60 and score<80:
        print("B")
    if score>=50 and score<60:
        print("Pass")
    elif score<50 and score>0:
        print("Fail")
else:
    print("Invalid score")