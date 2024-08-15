class Vehiculo:
    def __init__(self, ruedas, marca, modelo, color):
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def acelerar(self):
        print(f"El {self.marca} {self.modelo} esta acelerando")

    def frenar(self):
        print(f"El {self.marca}{self.modelo} esta frenando")

class Coche(Vehiculo):
    def bocina(self):
        print("pipipii")

class Bicicleta(Vehiculo):
    def acelerar(self):
        print("Estoy empezando a pedalear")

mi_coche = Coche(4, "Totoya","corolla","Rojo")
mi_coche.bocina()

mi_bici = Bicicleta(2, "Vairo","CRX","Blanco")
mi_bici.acelerar()