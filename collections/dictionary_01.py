dictionary = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DMBS': 'Database Management System'
}

print(dictionary)
# Longitud
print(len(dictionary))

# No existen indices, se parece a un set
# Accediendo a elementos
print(dictionary['IDE'])
# Otra manera de recuperar el valor
print(dictionary.get('OOP'))
# Modificando elementos
dictionary['IDE'] = 'integrated development environment'
print(dictionary)
# Recorrer elementos del dictionary
for termino, valor in dictionary.items():
    print(termino, '=>', valor)

for termino in dictionary.keys():
    print(termino)

for valor in dictionary.values():
    print(valor)

# comprobar existencia de elementos
print('IDES' in dictionary)

# agregando elementos
dictionary['PK'] = 'Primary Key'
print(dictionary)

# Remover elementos
dictionary.pop('PK')
print(dictionary)

# Limpiando el diccionario
dictionary.clear()
print(dictionary)

# Eliminando variable
del dictionary
print(dictionary)