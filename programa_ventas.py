# Trabajo Practico N° 2 - Organización Empresarial

inventario = {} # Diccionario a utilizar

while True: # Bucle para que luego de cada opción vuelvas al menú

    print ("Tienda BluestCat")  # Cargamos la bienvenida y el menú de opciones
    print ("1. Carga Inicial de Productos ")
    print ("2. Carga de Stock")
    print ("3. Carga de Precios")
    print ("4. Visualización de Inventario")
    print ("54. Consulta de Stock (Existencias Individuales)")
    print ("5. Reporte de Agotados")
    print ("6. Alta de Nuevo Producto")
    print ("7. Actualización de Stock (Ingresos)")
    print ("8. Carga de Ventas")
    print ("9. Estadísticas")
    print ("10. Salir ")

    opcion = input ("Ingrese la opción a realizar ") # Pedimos que elijan un número del 1 al 10

    match opcion: # Unimos el número dado a la acción a realizar

        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass
        case "10":
            pass
        case _:
            print ("Por favor ingrese un número del 1 al 10")