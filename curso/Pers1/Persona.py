class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    """
    def __del__(self):
        print(f'Persona: {self.nombre} {self.apellido}')
    """
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.edad}'
    def mostrar_detalles(self):
        print(f'Persona = [ Nombre:{self.nombre}, Apellido:{self.apellido}, Edad:{self.edad} ]')
class Empleado(Persona):
    def __init__(self,  nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
    def __str__(self):
        return f'{super().__str__()} {self.sueldo}'
    def mostrar_detalle_Emp(self):
        print(f'Persona = [ Nombre:{self.nombre}, Apellido:{self.apellido}, Edad:{self.edad}, Sueldo:{self.sueldo} ]')


if __name__ == '__main__':
    persona1 = Persona('Alejandro', 'Pablo', '36')
    persona1.nombre = 'Ari'
    persona1.apellido = 'Pab'
    persona1.edad = '35'
    persona1.mostrar_detalles()
    empleado1 = Empleado('Edgard', 'Melgarejo', '40', '5000')
    empleado1.mostrar_detalle_Emp()
    print(__name__)








