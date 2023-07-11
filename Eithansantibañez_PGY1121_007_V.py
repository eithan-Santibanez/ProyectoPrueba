import numpy as np
import datetime
# Matriz para representar el estado de los departamentos
tabla = np.full((10, 4), ' ')

# Precios de los departamentos
precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}

# Compradores de departamentos
compradores = []

# Validar formato del RUT
def validar_rut(rut):
    return rut.isdigit() and len(rut) <= 9 and '.' not in rut and '-' not in rut
#isdigit me permite devolver a TRUE si los caracteres son digitos, de lo contrario sera un FALSE

# Mostrar el estado actual de los departamentos
def mostrar_tabla():
    print("Estado actual de los departamentos:")
    print("Piso | Tipo A | Tipo B | Tipo C | Tipo D")
    print("Precio:--3800-----3300-----2800------3500")
    for piso in range(10, 0, -1):
        fila = tabla[piso-1]
        fila_str = [departamento if departamento != ' ' else ' ' for departamento in fila]
        print("{:<4} | {}      | {}      | {}      | {}".format(piso, *fila_str))
    print("---------------------------------------")

# Comprar departamento
def comprar_departamento(nombre, rut):
    mostrar_tabla()
    departamento = input("Ingresa el departamento a comprar: ") #las letras son validadas estando en MAYUS
    
    # Verificar que el departamento sea valido
    if len(departamento) != 2 or departamento[0] not in ['A', 'B', 'C', 'D'] or not departamento[1].isdigit():
        print("Departamento inválido.")
        return
    
    piso = int(departamento[1])
    tipo = departamento[0]
    
    # Verificar que el piso este en las opciones
    if piso < 1 or piso > 10:
        print("Piso inválido.")
        return
    
    # verifiacion de disponibilidad de un departamento
    if tabla[piso-1][ord(tipo) - ord('A')] == ' ':
        tabla[piso-1][ord(tipo) - ord('A')] = tipo
        compradores.append({'nombre': nombre, 'rut': rut, 'departamento': departamento})
        print("Departamento {} comprado exitosamente.".format(departamento))
    else:
        print("El departamento {} esta vendido.".format(departamento))

# Ver listado de compradores
def ver_listado_compradores():
    if len(compradores) == 0:
        print("No hay compradores en el registro .")
    else:
        print("Listado de compradores:")
        print("Nombre | RUT | Departamento")
        print("-------------------------------------------")
        for comprador in sorted(compradores, key=lambda c: c['rut']): #lambda permite aceptar varios argumentos y devolver un valor
            print("{:<14} | {:<12} | {}".format(comprador['nombre'], comprador['rut'], comprador['departamento']))

# ganancias totales
def mostrar_ganancias_totales():
    total_por_tipo = {tipo: 0 for tipo in ['A', 'B', 'C', 'D']}
    
    for comprador in compradores:
        tipo = comprador['departamento'][0]
        total_por_tipo[tipo] += precios[tipo]
    
    total_general = sum(total_por_tipo.values())
    
    print("Tipo de Departamento | Cantidad | Total")
    print("--------------------------------------")
    for tipo in ['A', 'B', 'C', 'D']:
        cantidad = np.count_nonzero(tabla == tipo)
        total = total_por_tipo[tipo]
        print("{:<20} | {:<8} | {:<8}".format(tipo, cantidad, total))
    
    print("--------------------------------------")
    print("TOTAL | {:<8} | {:<8}".format(sum(total_por_tipo.values()), total_general))

# Función para salir del programa
def salir(nombre, rut):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    print("¡Gracias por elegir nuestros departamentos!!")
    print("Nombre: {} [{}]".format(nombre, rut))
    print("Fecha Actual: {}".format(fecha))

# Función principal
def control_venta_departamentos():
    nombre = input("Ingrese su nombre: ")
    rut = input("Ingrese su RUT: ")
    while True:
        print("\n--- Inmobiliaria Casa Feliz :D ---")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            comprar_departamento(nombre,rut)

        elif opcion == '2':
            mostrar_tabla()

        elif opcion == '3':
            ver_listado_compradores()

        elif opcion == '4':
            mostrar_ganancias_totales()

        elif opcion == '5':
            salir(nombre,rut)
            break

        else:
            print("Opción no valida. Intenta nuevamente.")

control_venta_departamentos()