class Persona:
    contador_persona = 0

    @classmethod
    def _increment_id(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        self.increment_id()
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'[{self.id} {self.nombre} {self.edad}]'


persona1 = Persona(nombre='Jorge', edad=32)
print(persona1)
persona2 = Persona(nombre='Jacobo', edad=0.1)
print(persona2)
