class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = list(computadoras)

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def __str__(self):
        computadoras_str = ''
        for computador in self._computadoras:
            computadoras_str += computador.__str__() + '\n'
        return f'''
        Orden: {self._id_orden}, computadoras:
        {computadoras_str}
        '''