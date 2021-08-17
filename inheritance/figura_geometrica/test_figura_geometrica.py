from cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 'rojo')
print(f'El área del cuadrado es: {cuadrado1.calcular_area()}')
print(cuadrado1)

rectangulo1 = Rectangulo(3, 5, 'azul')
print(f'El área del rectangulo es: {rectangulo1.calcular_area()}')
print(rectangulo1)
