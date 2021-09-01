from orden import Orden
from computadora import Computadora
from monitor import Monitor
from mouse import Mouse
from teclado import Teclado

# Orden #1
# computador 1
monitor1 = Monitor(marca='Hp', tamanio='15 pulgadas')
teclado1 = Teclado(tipo_entrada='usb', marca='Hp')
mouse1 = Mouse(tipo_entrada='usb', marca='Hp')
computador1 = Computadora(nombre='Hp', monitor=monitor1, teclado=teclado1, mouse=mouse1)

# computador 2
monitor2 = Monitor(marca='Acer', tamanio='27 pulgadas')
teclado2 = Teclado(tipo_entrada='bluetooth', marca='Acer')
mouse2 = Mouse(tipo_entrada='bluetooth', marca='Acer')
computador2 = Computadora(nombre='Acer', monitor=monitor2, teclado=teclado2, mouse=mouse2)

lista_computadoras_1 = [computador1, computador2]

orden1 = Orden(lista_computadoras_1)

# Orden #2
# computador 1
monitor3 = Monitor(marca='Hp', tamanio='15 pulgadas')
teclado3 = Teclado(tipo_entrada='usb', marca='Hp')
mouse3 = Mouse(tipo_entrada='usb', marca='Hp')
computador3 = Computadora(nombre='Hp', monitor=monitor3, teclado=teclado3, mouse=mouse3)

# computador 2
monitor4 = Monitor(marca='Gamer', tamanio='32 pulgadas')
teclado4 = Teclado(tipo_entrada='bluetooth', marca='Acer')
mouse4 = Mouse(tipo_entrada='bluetooth', marca='Acer')
computador4 = Computadora(nombre='Acer', monitor=monitor4, teclado=teclado4, mouse=mouse4)

lista_computadoras_1 = [computador1, computador2]
lista_computadoras_2 = [computador3, computador4]

orden1 = Orden(lista_computadoras_1)
print(orden1)

orden2 = Orden(lista_computadoras_2)
# Agregando nuevo computador
monitor5 = Monitor(marca='Huawei', tamanio='32 pulgadas')
teclado5 = Teclado(tipo_entrada='bluetooth', marca='Acer')
mouse5 = Mouse(tipo_entrada='bluetooth', marca='Acer')
computador5 = Computadora(nombre='Huawei', monitor=monitor5, teclado=teclado5, mouse=mouse5)

orden2.agregar_computadora(computador5)
print(orden2)