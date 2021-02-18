number = input("Type a number: ")

try:
    number = float(number)
    print("This is your number: " + str(number))
except:
    print("Invalid number")
