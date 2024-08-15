# class Coche:
#     pass

# mi_coche = Coche()
# otro_coche = Coche()

# class Coche:

#     #Constructor

#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#Esta es una clase con atributos de instancia

class Coche:
    ruedas = 4

    #Constructor

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    #Metodo
    def acelerar(self):
        print(f"El {self.marca}{self.modelo} esta acelerando.")
    
    #Metodo
    def frenar(self):
        print(f"El {self.marca} {self.modelo} esta frenando")
    
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas += 1

    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        return velocidad * tiempo

#Crear un objeto de la clase Coche

mi_coche = Coche("Toyota", "Corolla", "Rojo")
otro_coche = Coche("FOrd", "Range", "Azul")

# Acceder al estado de los atributos directamente

print('Atributos del primer coche:')
print(mi_coche.marca)
print(mi_coche.modelo)
print(mi_coche.color)
print(mi_coche.ruedas)

print('Atributos del segundo coche:')
print(otro_coche.marca)
print(otro_coche.modelo)
print(otro_coche.color)
print(otro_coche.ruedas)

mi_coche.acelerar()
mi_coche.frenar()

otro_coche.acelerar()
otro_coche.frenar()

Coche.incrementar_ruedas()
print(mi_coche.ruedas)

print(Coche.calcular_distancia(80,2))

class Perro():
    def __init__(self, nombre, raza, poder):
        self.nombre = nombre
        self.raza = raza
        self.poder = poder

catdog = Perro('CatDog','Teckel','Super elasticidad')
print(catdog.nombre)
print(catdog.raza)
print(catdog.poder)

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_info(self):
        print(f"Usuario: {self.nombre}, Email:{self.email}")

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def  mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}")