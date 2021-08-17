from cuadrado import Cuadrado
from rectangulo import Rectangulo

print('Creacion de cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5, 'rojo')
print(f'El área del cuadrado es: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion de rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, 5, 'azul')
print(f'El área del rectangulo es: {rectangulo1.calcular_area()}')
print(rectangulo1)
rectangulo2 = Rectangulo(4,-5, 'morado')
print(f'El área del rectangulo es: {rectangulo2.calcular_area()}')
print(rectangulo2)
rectangulo2.ancho = -43
print(f'El área del rectangulo es: {rectangulo2.calcular_area()}')
print(rectangulo2)
rectangulo2.ancho = 6
print(f'El área del rectangulo es: {rectangulo2.calcular_area()}')
print(rectangulo2)

# Se modifica el Method Resolution Order al colocar la clase abstracta
print(Cuadrado.mro())

