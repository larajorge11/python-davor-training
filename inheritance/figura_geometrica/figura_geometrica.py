class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

    def __str__(self):
        return f'Figura Geometrica Ancho:{self.__ancho} Alto:{self.__alto}'

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        self.__alto = alto

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho