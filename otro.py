class Empleado:
    def __init__(self, sueldo):
        self.sueldo = sueldo

    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 1/100)
        print(f"El sueldo anual del empleado NORMAL es de ARS${sueldoAnual:.2f}")

class Programador(Empleado):
    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 4/100) # 4% bonus
        print(f"El sueldo anual del Programador es de ARS${sueldoAnual:.2f}")

class Diseniador(Empleado):
    def calcularSueldoAnual(self):
        sueldoAnual = 12 * self.sueldo * (1 + 5/100) # 5% bonus
        print(f"El sueldo anual de un Diseñador es de ARS${sueldoAnual:.2f}")

empleados = [
    Empleado(1000),
    Programador(1850),
    Empleado(2500),
    Diseniador(1054),
    Diseniador(2202),
    Programador(5070)
]

def calculoEmpleadosEmpresa():
    for empleado in empleados:
        empleado.calcularSueldoAnual()

calculoEmpleadosEmpresa()
