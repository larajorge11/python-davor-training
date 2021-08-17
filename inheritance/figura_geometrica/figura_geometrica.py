class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if alto > 0:
            self.__alto = alto
        else:
            self.__alto = 0

        if ancho > 0:
            self.__ancho = ancho
        else:
            self.__ancho = 0

    def __str__(self):
        return f'Figura Geometrica Ancho:{self.__ancho} Alto:{self.__alto}'

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self.__alto = alto

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self.__ancho = ancho

    def _validar_valor(self, valor):
        return True if valor > 0 else False
