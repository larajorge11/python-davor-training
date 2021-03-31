from decorators import debug
import math


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy! {name}"
    else:
        return f"Whoa! {name}! {age} already!, you are growing up!"


make_greeting("Davor")
make_greeting("Bianca", age=1)
make_greeting(name="Jacobo", age=0.0)
#######################
# Debug over a function already written
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


approximate_e(5)
