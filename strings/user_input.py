import math
phrase1 = 'Hi I am '
phrase2 = 'Davor and Bianca'
phrase3 = phrase1 + ' ' + phrase2
print(phrase3)
user_input = input('How many apples do you have?\n >>> ')
print(user_input)

# Exercise 1: print the area of circle
radius = float(input('Please submmit the radious\n >>> '))

# Area circle formula Pi * r^2
area_circle = math.pi * math.pow(radius, 2)
print('You entered: ' + str(radius) + ' the area of your circle is: ' + str(area_circle))

# Convert Farenheit to Celcius
# Formula: ((F - 32)*5)/9 = C

farenheit_value = float(input('Please submmit the farenheit degrees \n >>> '))
celcius = ((farenheit_value - 32)*5)/9
print('Farenheit: ' + str(farenheit_value) + ' to Celcius= ' + str(celcius))