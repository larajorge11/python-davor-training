# Local functions
# Enclosing namespace
# Returning local functions

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]

    print(last_letter)
    return sorted(strings, key=last_letter)


my_string = ["hello", "from", "a", "local", "function"]
print(sort_by_last_letter(my_string))


def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func

lf = enclosing()
lf()
print(lf.__closure__) 