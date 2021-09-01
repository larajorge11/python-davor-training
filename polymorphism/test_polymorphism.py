from empleado import Empleado
from gerente import Gerente


def imprimir_detalle(objeto):
    print(objeto)
    print(type(objeto))


empleado1 = Empleado('Juan', 5000)
imprimir_detalle(empleado1)
print(''.center(50, '-'))
gerente = Gerente('Carla', 6000, 'Software')
imprimir_detalle(gerente)


print(218550000 + 3568000 + 17140000)
print(2183000 + 2644000 - 59000)