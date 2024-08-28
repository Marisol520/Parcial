productos = {}  # Debe ser inicializado antes de ser utilizado

def agregar_producto_proveedor():
    global productos  # Debe ser declarado como global para que se pueda acceder desde las funciones
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        precio_sugerido = float(input("Ingrese el precio sugerido de venta: "))
        while True:
            cantidad = int(input("Ingrese la cantidad de producto recibida: "))
            if cantidad > 0:
                break
            else:
                print("La cantidad debe ser mayor que cero")
        productos[nombre] = {"precio_sugerido": precio_sugerido, "cantidad": cantidad}
        respuesta = input("¿Desea agregar otro producto? (s/n): ")
        if respuesta.lower() != 's':
            break

def vender_producto():
    global productos  # Debe ser declarado como global para que se pueda acceder desde las funciones
    total_venta = 0
    while True:
        nombre = input("Ingrese el nombre del producto que desea vender (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        if nombre in productos:
            while True:
                cantidad_vender = int(input("Ingrese la cantidad que desea vender: "))
                if cantidad_vender > 0:
                    break
                else:
                    print("La cantidad debe ser mayor que cero")
            if cantidad_vender <= productos[nombre]["cantidad"]:
                precio_venta = float(input("Ingrese el precio de venta: "))
                productos[nombre]["cantidad"] -= cantidad_vender
                total_venta += precio_venta * cantidad_vender
                print(f"Venta realizada: {nombre} x {cantidad_vender} = {precio_venta * cantidad_vender:.2f}")
            else:
                print("No hay suficiente stock para vender esa cantidad")
        else:
            print("Producto no encontrado")
    return total_venta

def calcular_cambio(cliente_pago, total_venta):
    if cliente_pago >= total_venta:
        cambio = cliente_pago - total_venta
        print(f"Cambio: {cambio:.2f}")
    else:
        print("No hay suficiente pago para realizar la venta")

def mostrar_productos():
    global productos  # Debe ser declarado como global para que se pueda acceder desde las funciones
    print("Productos en la tienda:")
    for nombre, producto in productos.items():
        print(f"Nombre: {nombre}, Precio sugerido: {producto['precio_sugerido']}, Cantidad: {producto['cantidad']}")

def main():
    agregar_producto_proveedor()
    mostrar_productos()
    total_venta = vender_producto()
    cliente_pago = float(input("Ingrese el pago del cliente: "))
    calcular_cambio(cliente_pago, total_venta)

if __name__ == "__main__":
    main()