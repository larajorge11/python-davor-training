from math import sqrt

# Iterator from tuples
fruits = ['banana', 'mango', 'strawberry']
fruits_iter = iter(fruits)

print(next(fruits_iter))
print(next(fruits_iter))
print(next(fruits_iter))

# Iterator from sequences
fruit_str = "Orange"
fruit_str_iter = iter(fruit_str)

print(next(fruit_str_iter))
print(next(fruit_str_iter))
print(next(fruit_str_iter))
print(next(fruit_str_iter))
print(next(fruit_str_iter))
print(next(fruit_str_iter))

# Looping through an iterator
# we can use the for loop
for i in fruits:
    print(i)


# Build an iterator
# iter() and next()

class NewNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 17:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


newNumber = NewNumber()
newNumber_iter = iter(newNumber)

print(next(newNumber_iter))
print(next(newNumber_iter))
print(next(newNumber_iter))
print(next(newNumber_iter))
print(next(newNumber_iter))

for i in newNumber_iter:
    print(i)