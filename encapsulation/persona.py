class Persona:
    '''
    _: Indica que la variable ya no es visible, sin embargo es posible modificarlo
    __:Indica que la variable ya no es visible, ya no es modificable
    property para crear get
    decorador @nombre_atributo.setter
    La variable de solo lectura es cuando no tiene el setter asociado
    '''

    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__args = args
        self.__kwargs = kwargs

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self.__nombre} {self.__apellido} {self.__edad} {self.__args} {self.__kwargs}")

    def __del__(self):
        print(f'Persona {self.__nombre} {self.__apellido} esta siendo eliminado')


if __name__ == '__main__':
    persona2 = Persona("Jorge", "Lara", 16, '345', 4, 3, 5, m='manzana', p='piña')
    persona2.edad = 40
    print(persona2.mostrar_detalle())
