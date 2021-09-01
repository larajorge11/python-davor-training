from dispositivo_entrada import Dispositivo_Entrada


class Teclado(Dispositivo_Entrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        super().__init__(tipo_entrada=tipo_entrada, marca=marca)
        self._contador_teclados = Teclado.contador_teclados

    def __str__(self):
        return f'Teclado: Id:{self._contador_teclados}, {super().__str__()}'


if __name__ == '__main__':
    teclado1 = Teclado(tipo_entrada='USB', marca='HP')
    print(teclado1)
