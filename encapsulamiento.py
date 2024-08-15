class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.__pi = 3.1415

    def calcular_area(self):
        return self.__pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * self.__pi * self.radio
    
    def imprimir_resultado(self, area):
        print("El area del circulo es: ", area)

    def getPi(self):
        return f"el valor de pi es{self.__pi}"
    
    def setPi(self, nuevoValor):
        if type(nuevoValor) == int or type(nuevoValor) == float:
            if nuevoValor > 0:
                self.__pi = nuevoValor
                print(f"El nuevo valor de PI es {self.__pi}")
            else:
                print("PI no puede ser Negativo")
        else:
            print("El valor debe ser un numero positivo")

circulo_uno = Circulo(3.5)
circulo_uno.setPi(-5)
circulo_uno.setPi(4.6)
circulo_uno.setPi("hola")

# radio = 5
# area_circulo = circulo.calcular_area()
# circulo.imprimir_resultado(area_circulo)

circulo_uno = Circulo(3.5)
# print(circulo_uno.calcular_area())
# print(circulo_uno.calcular_perimetro())
