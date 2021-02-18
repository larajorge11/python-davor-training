number = input("Type a number: ")

try:
    number = float(number)
    print("This is your number: " + str(number))
except ValueError:
    print("Invalid number")


def calculate_student_grade():
    while True:
        try:
            data = float(input("Type the grade: "))
            if data < 0.0 or data > 5.0:
                print("Grade is not in the correct range [0 - 5]")
            else:
                return data
        except ValueError:
            print("Grade is not a correct value")


print(f"Your grade is: {calculate_student_grade()}")
