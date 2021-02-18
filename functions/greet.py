def greet(name, age=0):
    print(f"Hello {name} how are you?")
    if not age <= 0:
        print(f"I know your age: {age}")


greet("Davor", 31)
greet("Test")

