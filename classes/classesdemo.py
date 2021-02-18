class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self) -> str:
        return f"{self.name} is walking"

    def bark(self) -> str:
        return f"Hello I am {self.name} I am barking"

    def __str__(self) -> str:
        return f"Hello you are {self.name} and you are {str(self.age)}"


# Attributes
davor = Pet('Davor', 31)
bianca = Pet('Bianca', 1)

print(davor)
print(bianca)

# Behavior
print(davor.name + ' ' + str(davor.age))
print(davor.walk())
print(davor.bark())

print(bianca.name + ' ' + str(bianca.age))
print(bianca.bark())
print(bianca.walk())
