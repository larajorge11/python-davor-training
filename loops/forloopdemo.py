cars = ['mazda', 'renault', 'kia', 'chevrolet']

for car in cars:
    print(car)

pet = {
    "name": "davor",
    "age": 31,
    "country": "Colombia"
}

for key in pet:
    print(f"key: {key} value: {pet[key]}")

for key, value in pet.items():
    print(f"key: {key} value: {value}")

for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    if n <= 4:
        continue
    print(n)
