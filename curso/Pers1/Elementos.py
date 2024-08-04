class Elementos:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_elemento(self):
        print(self.nombre)
    def mostrar_elementos(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

elemento1 = Elementos('Alejandro', 'Pablo', '38')
elemento1.nombre = 'Alonso'
Elementos.mostrar_elementos(elemento1)

elemento2 = Elementos('Adriana', 'Gomez', 'Dìaz')
elemento2.mostrar_elemento()

print(elemento1.nombre)
print(elemento2.nombre)

