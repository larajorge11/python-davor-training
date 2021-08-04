def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

resultado = factorial(5)
print(resultado)