class Vehiculo:
    def __init__(self, ruedas, color):
        self.__ruedas = ruedas
        self.__color = color

    def __str__(self):
        return f'Vehiculo: {self.color} {self.ruedas}'

    @property
    def ruedas(self):
        return self.__ruedas

    @property
    def color(self):
        return self.__color

    @ruedas.setter
    def ruedas(self, ruedas):
        self.__ruedas = ruedas

    @color.setter
    def color(self, color):
        self.__color = color


class Coche(Vehiculo):
    def __init__(self, velocidad, ruedas, color):
        super().__init__(ruedas, color)
        self.__velocidad = velocidad

    def __str__(self):
        return f'Coche: {self.__velocidad} {super().color} {super().ruedas}'

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self.__velocidad = velocidad


class Bicicleta(Vehiculo):
    def __init__(self, tipo, ruedas, color):
        super().__init__(ruedas, color)
        self.__tipo = tipo

    def __str__(self):
        return f'Bicicleta: {self.__tipo} {super().color} {super().ruedas}'

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo


if __name__ == '__main__':
    bici1 = Bicicleta('urbana', 2, 'azul')
    coche1 = Coche('50km/h', 4, 'rojo')

    print(bici1)
    print(coche1)
