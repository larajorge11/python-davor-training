cars = ['mazda', 'renault', 'kia', 'chevrolet']

print(len(cars))
print(cars[0])
print(cars[1])
print(cars[2])
# var = cars[4]  # IndexError: list index out of range

print('inside a for loop')
for car in cars:
    if car == 'mazda':
        print('Great car: ' + car.capitalize())
    else:
        print('Normal car: ' + car.capitalize())

numbers = [1, 2, 3, 4, 5, -76, 0]
print(numbers[5])
numbers.reverse()
print(numbers)
numbers.append(650)
numbers.sort()
# List methods
print('Lenght: ' + str(len(numbers)))
print(5 in numbers)
numbers.remove(4)
print(numbers)
numbers.pop()  # Remove the last element
print(numbers)
del numbers[0]
del numbers[0:3]
print(numbers)


test = []
test.append(1)
test.append(2)

print(test)