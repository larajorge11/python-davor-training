pet = {
    "name": "davor",
    "age": 31,
    "country": "Colombia"
}

print(f"pet name: {pet['name']}")
print(f"pet name using get: {pet.get('name')}")
print(f"pet name: {pet['age']}")
print(f"pet name: {pet['country']}")
pet["country"] = "USA"
print(pet.keys())
print(pet.values())
