def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

resultado = factorial(5)
print(resultado)

def imprimir_lista(num):
    if num <= 0:
        return 1
    else:
        print(num)
        imprimir_lista(num - 1)


imprimir_lista(-4)