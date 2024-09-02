class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, puesto, sueldo):
        super().__init__(nombre)
        self.puesto = puesto
        self.sueldo = sueldo
    
    def consultaEmpleado(self):
        print(f"Nombre: {self.nombre} \nPuesto: {self.puesto}\nSueldo: {self.sueldo}")

class Cliente(Persona):
    def __init__(self, nombre, numero_cliente, compras):
        super().__init__(nombre)
        self.numero_cliente = numero_cliente
        self.compras = compras

    def mostrarCliente(self):
        print(f"Nombre: {self.nombre} \nNro. Cliente: {self.numero_cliente} \nCompras: {self.compras}")


empleado1 = Empleado("juan", "administrativo", 15000)
empleado1.consultaEmpleado()
print("------------------------- * ----------------------")
cliente1 = Cliente("Pedro", 150, 20)
cliente1.mostrarCliente()
print("------------------------- * ----------------------")
cliente2 = Cliente("Maria", 200, 50)
cliente2.mostrarCliente()
print("------------------------- * ----------------------")
cliente3 = Cliente("Jose", 300, 100)