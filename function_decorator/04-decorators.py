def sayHello(name):
    return f"Hi, {name}"


def sayAnotherGreeting(name):
    return f"How's it going {name}"


def greet_bob(func):
    return func("Bob")


print(greet_bob(sayHello))
print(greet_bob(sayAnotherGreeting))
print("##############################")


#####################################
## Inner functions
def parent(value):
    print("Hello I am the father")

    def first_child():
        print("Hello I am the 1st child")

    def second_child():
        print("Hello I am the 2nd child")

    if value:
        return second_child()
    else:
        return first_child()


first = parent(False)
second = parent(True)

#####################################
# Calling oor decorator
print("************************")
from decorators import print_twice, print_twice_arguments


@print_twice
def say_hello():
    print('Hello')


say_hello()


@print_twice_arguments
def say_whee(name):
    print(f"Whee {name}")


say_whee("Jorge")
