print(10 < 10)
print(10 <= 10)
print(0 == 0)
print(18 > 5)
print('Davor'.endswith('r'))
print('Davor'.endswith('s'))

is_adult = True
is_teenager = False
age = 31

if is_adult:
    print("Is adult")

if age >= 60:
    print('Adult')
else:
    print('No Adult')

# No es necesario siempre que la condicion sea un boolean, si es vacio este marca false, pero si no lo marca True
condition = 10
if condition:
    print('True condition')
else:
    print('False condition')