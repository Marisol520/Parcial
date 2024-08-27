class Cliente:
    def __init__(self, nombre, apellido, edad, dias_estancia, habitacion, metodo_pago, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dias = dias_estancia 
        self.habitacion = habitacion 
        self.metodo_pago = metodo_pago
        self.direccion = direccion
        self.telefono = telefono
        self.estado = "NO ATENDIDO"  
        self.clasificacion = self.clasificar_cliente()
#esta funcion es la que nos ayudara a saber la estancia del clinte si su estancia es menor a 5 dias
# se utilizara la funcion del if,y al final del registro dira gracias por su estancia#
# en caso de que el cliente desee quedarse mayor a 5 se utilizara la funcion que returna el else, 
#  los dias el programa le dira que es poseedor de un decuento#
    def clasificar_cliente(self):
        if self.dias < 5:
            return "gracias por su preferncia "
        else:
            return "poseedor de descuento"

    def atender_cliente(self):
        self.estado = "ATENDIDO"
#las lineas de codigo de los codigos siguientes sirven para mostrar la informacion del cliente al momento de registrarse al Hotel#
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Días de estancia: {self.dias}")
        print(f"Habitación: {self.habitacion}")
        print(f"Método de pago: {self.metodo_pago}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Clasificación: {self.clasificacion}")
        print(f"Estado: {self.estado}")
#estas son etiquetas que apareceran al momento de aser el registro como por ejemplo la de Bienvenidos#
def main():
    print("BIENVENIDO")
    print("Registro de cliente")
    print("Estado inicial del cliente: NO ATENDIDO")  

    nombre = input("Nombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    edad = int(input("Edad (en años): "))
    dias_estancia = int(input("Días de estancia (en días): "))
    habitacion = input("Tamaño de habitación: ")
    metodo_pago = input("Método de pago: ")
    direccion = input("Dirección del cliente: ")
    telefono = input("Teléfono del cliente: ")

    nuevo_cliente = Cliente(nombre, apellido, edad, dias_estancia, habitacion, metodo_pago, direccion, telefono)

    nuevo_cliente.atender_cliente()

    print(f"\nEstado final: {nuevo_cliente.estado}")
    nuevo_cliente.mostrar_informacion()

if __name__ == "__main__":
    main()
