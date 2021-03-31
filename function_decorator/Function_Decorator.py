# Modify or enhance an existing function in a non-intrusive and maintainable way
# Implemented as a callable that accepts a callable and returns a callable
# Decorators allow you to modify existing functions without changing their definition
# Classes are callable objects

# Python calls an instance's __call__() when it's used as a decorator
class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print(f"Hello {name}")


hello('Jorge')
hello('Bianca')
hello('Davor')

print(hello.count)
