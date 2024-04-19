M1 = float(input("Enter M1: "))
M2 = float(input("Enter M2: "))
M3 = float(input("Enter M3: "))
M4 = float(input("Enter M4: "))

Grade = (M1 + M2 + M3 + M4) / 4

if Grade < 50:
    print("Fail")
else:
    print("Pass")
