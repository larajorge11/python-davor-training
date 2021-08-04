# El valor argumento se convierte en una tupla
def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)


listar_nombres('Jorge', 'Lara', 'Espitia')


def multiplicar_numeros(*args):
    acumulador = 1
    for arg in args:
        acumulador *= arg
    return acumulador

print(multiplicar_numeros(1,2,3))

# Se reciben elementos de llave/valor
# Se pueden entonces pasar valores fijos, tuplas y dictionary
def listar_terminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')

listar_terminos(IDE='Integrated Development Environment', PK='Primary Key')

