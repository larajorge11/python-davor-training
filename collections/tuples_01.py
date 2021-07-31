# Las tuplas son immutables
# Se respeta el orden en que se adicionan los elementos
frutas = ('Banano', 'Pera', 'Manzana')
# Longitud de tupla
print(f'Longitud de tupla {len(frutas)}')
print(frutas)
# Acceder a un elemento
print(frutas[1])
# Recorrer una tupla
for fruta in frutas:
    print(fruta, end=' ')

# frutas[0] = 'Arandano' NO ES MODIFICABLE
# Podemos hacer modificaciones de una manera indirecta: crear una lista desde una tupla
frutas_lista = list(frutas)
frutas_lista[1] = 'Arandano'
frutas = tuple(frutas_lista)
print('\n', frutas)