class MiClase:
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        # Metodos estaticos no pueden acceder a variables y metodos de instancia
        # No tiene relacion directa con la clase
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_instancia)
        print(self.variable_clase)


print(MiClase.variable_clase)
miClase = MiClase("Esta es una variable de instancia")
print(miClase.variable_instancia)
print(miClase.variable_clase)

print(miClase.metodo_estatico())
miClase.metodo_clase()

# Accediendo a metodos estaticos o de clase desde un objeto, el contexto dinamico accede al contexto estatico(clases)
miObjeto1 = MiClase('Valor de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()
