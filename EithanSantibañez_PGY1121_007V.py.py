import numpy as np

# Variables globales
tabla = np.array([[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])
clientes = [] #en caso de que 2 personas se llamen igual, guarda solo el nombre lo que forma una lista unica tambien para ese cliente
tamaño_lote = 1000000  # Tamaño en metros cuadrados (1 millón)
precio_lote = 100000000  # Precio en pesos chilenos (100 millones)
#cada lote tiene el mismo espacio cuadrado y el mismo precio

# mostrar el tablero
def mostrar_tabla():
    print("   1   2    3    4    5")
    print("1 {} | {} | {} | {} | {}".format(tabla[0][0], tabla[0][1], tabla[0][2], tabla[0][3], tabla[0][4]))
    print("  ---------------------")
    print("2 {} | {} | {} | {} | {}".format(tabla[1][0], tabla[1][1], tabla[1][2], tabla[1][3], tabla[1][4]))
    print("  ---------------------")
    print("3 {} | {} | {} | {} | {}".format(tabla[2][0], tabla[2][1], tabla[2][2], tabla[2][3], tabla[2][4]))
    print("  ---------------------")
    print("4 {} | {} | {} | {} | {}".format(tabla[3][0], tabla[3][1], tabla[3][2], tabla[3][3], tabla[3][4]))

# Verificar si no queda más stock de lotes
def no_mas_lotes(): 
    # Filas
    for fila in tabla:
        if ' ' in fila:
            return False
    return True

# Realizar un movimiento
def hacer_movimiento(fila, col, cliente):
    if tabla[fila][col] == ' ':
        tabla[fila][col] = 'X'
        cliente['compras'] += 1
        return True
    else:
        print("La posición seleccionada ya está ocupada. Elige otra posición.")
        return False

# Mostrar los detalles del lote elegido
def ver_detalles_lote():
    fila = int(input("Selecciona una fila (1-4): ")) - 1
    col = int(input("Selecciona una columna (1-5): ")) - 1
    if tabla[fila][col] == ' ':
        print("El lote seleccionado está disponible.")
        print("Tamaño del lote: {} metros cuadrados.".format(tamaño_lote))
        print("Precio del lote: ${:,}.".format(precio_lote).replace(',', '.')) 
    else:
        print("El lote seleccionado no se encuentra disponible.")

# lista de clientes
def ver_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
    else:
        print("Lista de clientes:")
        for i, cliente in enumerate(clientes): #obtenemos el indice i como el elemento cliente en cada iteracion
            print("Cliente {}: {} (Compras: {})".format(i+1, cliente['nombre'], cliente['compras'])) #me permite iterar sobre la lista de clientes y muestra la información de cada cliente

# Función para vender lotes
def vender_lotes():
    while True:
        print("\nBienvenido al Lotes DUOC")
        print("1. ver disponibilidad de lotes")
        print("2. Comprar lote")
        print("3. Ver detalles de lotes ")
        print("4. lista de clientes")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_tabla()

        elif opcion == '2':
            if no_mas_lotes():
                print("No hay mas lotes disponibles, lo sentimos :( )")
            else:
                nombre = input("Ingrese su nombre: ")
                cliente = {'nombre': nombre, 'compras': 0}
                while True:
                    print("Seleccione un lote de su preferencia:")
                    mostrar_tabla()
                    print("Compra de {}: ".format(nombre))
                    fila = int(input("Selecciona una fila (1-4): ")) - 1
                    col = int(input("Selecciona una columna (1-5): ")) - 1

                    if hacer_movimiento(fila, col, cliente):
                        mostrar_tabla()
                        total_pagar = cliente['compras'] * precio_lote
                        print("Total a pagar por el lote seleccionado: ${:,}.".format(total_pagar).replace(',', '.')) #reemplaza cada "," por "."
                        respuesta = input("¿Deseas comprar otro lote? (s/n): ")
                        if respuesta.lower() == 'n':
                            break

                clientes.append(cliente)

        elif opcion == '3':
            ver_detalles_lote()

        elif opcion == '4':
            ver_clientes()

        elif opcion == '5':
            print("¡gracias por su visita!")
            break

        else:
            print("Opción invalida. Intenta nuevamente.")

vender_lotes()
