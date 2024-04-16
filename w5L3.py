def main():
    student = {}

    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        reg_num = input("Enter registration number: ")
        first_name = input("Enter first name: ")
        student[reg_num] = first_name

    print("Student dictionary:", student)

if __name__ == "__main__":
    main()
