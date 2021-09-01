from dispositivo_entrada import Dispositivo_Entrada


class Mouse(Dispositivo_Entrada):
    contador_mouse = 0

    def __init__(self, tipo_entrada, marca):
        Mouse.contador_mouse += 1
        super().__init__(tipo_entrada=tipo_entrada, marca=marca)
        self._contador_mouse = Mouse.contador_mouse

    def __str__(self):
        return f'Mouse: Id:{self._contador_mouse}, {super().__str__()}'


if __name__ == '__main__':
    mouse1 = Mouse(tipo_entrada='Bluetooth', marca='Logitech')
    print(mouse1)
