# Sets no mantienen un orden ni tampoco duplicados: No hay indices

planetas = {'Marte', 'Jupiter', 'Tierra'}
print(planetas)
print(len(planetas))
# Saber si un elemento se encuentra
print("Tierra" in planetas)
#Adicionando un nuevo elemento
planetas.add('Saturno')
print(planetas)
# No acepta duplicados
planetas.add('Tierra')
print(planetas)
# Eliminar elemento sin arrojar error
planetas.discard("Tierra")
print(planetas)