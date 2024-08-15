class Abuelo():
    # def __init__(self, nombre):
    #     self.nombre = nombre
    _atributo = "Este es un atributo de clase, protegido"

    def __init__(self, nombre):
        self._nombre = "Este es un atributo de instancia protegido"

    def saludar(self):
        print("Cuando saludo, paso la mano")

    def construir_casas(self):
        print("Puedo construir casa tradicionales de ladrilla y cemento")
    

class Abuela():
    pass
    
    def saludar(self):
        print("Cuando saludo, doy el brazo")

    def pintar_casas(self):
        print("Puedo pintar casas con rodillo y pincel")

class Padre(Abuela, Abuelo):
    pass

# abuela = Abuela()
# abuelo = Abuelo()

# abuelo.saludar()
# abuela.saludar()

class Hijo(Padre):
    pass

# hijo = Hijo('Info')
# print(hijo.nombre)

# hijo2 = Hijo('Informatorio')
# print(hijo2.nombre)
# print(hijo2.apellido)
# hijo.pintar_casas()
# hijo.construir_casas()
# hijo.saludar()
print(Abuelo._atributo)
objeto = Hijo(None)
print(objeto._nombre)
