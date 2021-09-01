from monitor import Monitor
from mouse import Mouse
from teclado import Teclado


class Computadora:
    id_computadora = 0

    def __init__(self, nombre: str, monitor: Monitor, teclado: Teclado, mouse: Mouse):
        Computadora.id_computadora += 1
        self._id_computadora = Computadora.id_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def marca(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def marca(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def marca(self, teclado):
        self._teclado = teclado

    @property
    def mouse(self):
        return self._mouse

    @mouse.setter
    def mouse(self, mouse):
        self._mouse = mouse

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        {self.monitor}
        {self.teclado}
        {self.mouse}
        '''
        return f''
