class Monitor:
    contador_monitor = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitor += 1
        self._contador_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamanio = tamanio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    def __str__(self):
        return f'Monitor: Id: {self._contador_monitor}, marca: {self.marca}, tamaño: {self.tamanio}'