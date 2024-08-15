class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = 3.14 * self.radio * self.radio
        return area
    
    def imprimir_resultado(self, area):
        print("El area del circulo es: ", area)

radio = 5
circulo = Circulo(radio)
area_circulo = circulo.calcular_area()
circulo.imprimir_resultado(area_circulo)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("wanda", 26)
persona1.saludar()
print(type(persona1))

"""-------------------------------------------"""

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} esta estudiando en el grado {self.grado}")
    
    def saludar(self):
        print(f"Hola, soy{self.nombre} y soy estudiante del grado {self.grado}")


class Empleado():
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
    
    def saludar(self):
        print(f"Mi puesto es {self.puesto}")


class Profesor(Persona, Empleado):
    def __init__(self, nombre, puesto, antiguedad):
        Persona.__init__(self,nombre)
        Empleado.__init__(self,nombre,puesto)
        self.antiguedad = antiguedad
    
    def saludar(self):
        # Persona.saludar(self)
        # Empleado.saludar(self)
        print(f"Estoy en el puesto hace {self.antiguedad}")


estudiante1 = Estudiante("Informatorio", 12, "A")
estudiante1.saludar()


