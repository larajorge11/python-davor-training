class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad


ancho = int(input('Proporciona el ancho >>> '))
alto = int(input('Proporciona el alto >>> '))
profundiad = int(input('Proporciona la profundidad >>> '))

cubo1 = Cubo(ancho, alto, profundiad)
print(cubo1.calcular_volumen())
