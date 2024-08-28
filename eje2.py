#Un colegio privado desea registrar la asistencia de sus estudiantes a las
#clases cada docente tiene su listado de los estudiantes en los cuáles se
#es ha solicitado colocar a la par de cada estudiante si ha asistido, si
#cuenta con permiso o tiene inasistencia con la fecha respectiva.
#Actualmente esto se maneja por unas hojas de papel impreso y se
#entregan al director al final del día; la escuela necesita agilizar este proceso.
# Si el estudiante tiene un permiso el director necesita la razón de dicha falta, 
# ¿Cómo solventarías esta situación? Agrega tu propuesta al código

def registrar_asistencia(asistencia):
    nombre = input("Ingrese el nombre del estudiante: ")
    estado = input("Ingrese el estado de asistencia (asistido, permiso, inasistencia): ").strip().lower()
    fecha = input("Ingrese la fecha (DD/MM/AA): ")

    if estado not in ["asistido", "permiso", "inasistencia"]:
        print("Estado no válido. Use 'asistido', 'permiso' o 'inasistencia'.")
        return

    razon = None
    if estado == "permiso":
        razon = input("Ingrese la razón del permiso: ")

    asistencia[nombre] = {"estado": estado, "fecha": fecha, "razón": razon}

#Funcion para mostrar el registro
def mostrar_asistencia(asistencia):
    

    for nombre, info in asistencia.items():
        print(f"\nEstudiante: {nombre}")
        print(f"Estado: {info['estado']}")
        print(f"Fecha: {info['fecha']}")
        if info['estado'] == "permiso":
            print(f"Razón del permiso: {info.get('razón', 'No proporcionada')}")

# Diccionario para almacenar la información de los estudiantes
asistencia = {}

# Ciclo para registrar varias asistencias
while True:
    registrar_asistencia(asistencia)
    
    continuar = input("¿Desea registrar otro alumno? (si/no): ").strip().lower()
    if continuar != "si":
        break

# Mostrar la asistencia registrada
mostrar_asistencia(asistencia)