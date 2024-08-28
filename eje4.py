class Empleado:
    def __init__(self, nombre, tipo_empleado, salario_base=None, horas_trabajadas=None, comisiones=None, anios_trabajados=None):
        self.nombre = nombre
        self.tipo_empleado = tipo_empleado
        self.salario_base = salario_base
        self.horas_trabajadas = horas_trabajadas
        self.comisiones = comisiones
        self.anios_trabajados = anios_trabajados
    #calculr el pago que se le da al empleado
    def calc_pago(self):
        bono_adicional = 0
        if self.anios_trabajados and self.anios_trabajados > 5:
            bono_adicional = 500  # Bono adicional si es mas de 5 años
        
        if self.tipo_empleado == 'plaza fija':
            if self.salario_base is None or self.comisiones is None:
                raise ValueError("Para empleados de plaza fija se debe proporcionar salario base y comisiones.")
            return self.salario_base + self.comisiones + bono_adicional
        elif self.tipo_empleado == 'por horas':
            if self.horas_trabajadas is None:
                raise ValueError("Para empleados por horas se debe proporcionar horas trabajadas.")
            tarifa_por_hora = 20  # Tarifa fija por hora
            return (self.horas_trabajadas * tarifa_por_hora) + bono_adicional
        else:
            raise ValueError("Tipo de empleado no reconocido. Debe ser 'plaza fija' o 'por horas'.")
    #funcion para general las factura en si de pago para el empleado
    def generar_pago(self):
        try:
            pago = self.calc_pago()
            boleta = f"--- Boleta de Pago ---\n"
            boleta += f"Nombre: {self.nombre}\n"
            boleta += f"Tipo de Empleado: {self.tipo_empleado}\n"
            
            if self.tipo_empleado == 'plaza fija':
                boleta += f"Salario Base: ${self.salario_base:,.2f}\n"
                boleta += f"Comisiones: ${self.comisiones:,.2f}\n"
            elif self.tipo_empleado == 'por horas':
                boleta += f"Horas Trabajadas: {self.horas_trabajadas}\n"
                boleta += f"Tarifa por Hora: $20.00\n"
            
            if self.anios_trabajados and self.anios_trabajados > 5:
                boleta += f"Bono Adicional: $500.00\n"
            
            boleta += f"Total a Pagar: ${pago:,.2f}\n"
            boleta += "---------------------"
            return boleta
        except ValueError as e:
            return f"Error en la boleta de {self.nombre}: {e}"

# Ejemplo 
empleados = [
    Empleado(nombre="Ken", tipo_empleado="plaza fija", salario_base=3000, comisiones=300, anios_trabajados=8),
    Empleado(nombre="Dani", tipo_empleado="por horas", horas_trabajadas=200, anios_trabajados=4),
    Empleado(nombre="Jeff", tipo_empleado="plaza fija", salario_base=2500, comisiones=500, anios_trabajados=7),
    Empleado(nombre="Alexander", tipo_empleado="por horas", horas_trabajadas=90, anios_trabajados=6)
]

for empleado in empleados:
    print(empleado.generar_pago())
    print()

