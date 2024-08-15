class Empleado:
    def __init__(self, nombre, sueldo):
        self.sueldo = sueldo
        self.nombre = nombre
    

    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 1/100)
#                     12 meses * sueldo del empleado * 1% de bonus al ser empleado
        print(f"El sueldo anual del empleado NORMAL es de  {sueldoAnual}")

class Programador(Empleado):
    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 4/100) # 4% bonus
        print(f"El sueldo anual del Programador es de ARS${sueldoAnual}")

class Diseniador(Empleado):
    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 5/100)# 5% bonus
        print(f"El sueldo anual de un Diseñador es de ARS$ {sueldoAnual}")

empleados = [
    Empleado("Franco", 1000),
    Programador("Nelson", 1850),
    Empleado("Susana", 2500),
    Diseniador("Dario", 1054),
    Diseniador("Jazim", 2202),
    Programador("Luciana", 5070)
]

def calculoEmpleadosEmpresa():
    for empleado in empleados:
        empleado.calcularSueldoAnual()

calculoEmpleadosEmpresa()