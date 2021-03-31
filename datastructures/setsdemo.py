numbersList = [0, 1, 2, 5, 7, -43, 56, 100, 0]
numbersSet = {0, 1, 2, 5, 7, -43, 56, 0, 100}  # Duplicates are not allowed, not guaranteed the order

print(numbersList)
print(numbersSet)

petsSet = {"bianca", "davor", "danger", "lu", "davor"}
print(petsSet)


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


factorial(5)
