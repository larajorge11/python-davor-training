# Las listas son mutables
nombres = ['Juan', 'Carla', 'Stefani', 'Jacobo', 'Bianca']
# Imprimir la lista de nombres
print(nombres)
# Accediendo a los elementos
print(nombres[0])
print(nombres[-1]) # Ultimo elemento de la lista

# Imprimir un rango
print(nombres[0:2])
print(nombres[:3])
print(nombres[2:])

nombres[1] = 'Davor'

for nombre in nombres:
    print(nombre)

# Preguntar el largo de una lista
print(f'elementos de la lista {len(nombres)}')

# Adicionar nuevo elemento
nombres.append('Brandon')
print(nombres)

# Insertar con un indice especifico
nombres.insert(1, 'Octavio')
print(nombres)

# Eliminar un elemento
nombres.remove('Octavio')
print(nombres)

# Remover ultimo elemento de lista
nombres.pop()
print(nombres)

# Remover un elemento especifico
del nombres[0]
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Remover la lista en memoria
del nombres
print(nombres)