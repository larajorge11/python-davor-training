'''
Creacion de modulos en python
'''
from persona import Persona

persona1 = Persona("Jorge", "Lara", 32, '5678', 4, 2, 5, m='manzana', p='pera')
persona1.nombre = "Davor"
persona1.apellido = "Espitia"
print(persona1.nombre, persona1.apellido)