class Rectangulo:
    '''
    Esta es una clase rectangulo de base y altura
    '''

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


altura = int(input("Proporcione la altura >>> "))
base = int(input("Proporcione la base >>> "))
rectangulo = Rectangulo(altura=altura, base=base)
print(f"El area del rectangulo es: {rectangulo.calcular_area()}")
