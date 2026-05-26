# Trabajo Practico N° 2 - Organización Empresarial

inventario = {} # Diccionario a utilizar
precios = {}

while True: # Bucle para que luego de cada opción vuelvas al menú

    print ("Tienda BluestCat")  # Cargamos la bienvenida y el menú de opciones
    print ("1. Carga Inicial de Productos con su Stock y Precios")
    print ("2. Visualización de Inventario")
    print ("3. Consulta de Stock (Existencias Individuales)")
    print ("4. Reporte de Agotados")
    print ("5. Alta de Nuevo Producto")
    print ("6. Actualización de Stock (Ingresos)")
    print ("7. Carga de Ventas")
    print ("8. Estadísticas")
    print ("9. Salir ")

    opcion = input ("Ingrese la opción a realizar ") # Pedimos que elijan un número del 1 al 10

    match opcion: # Unimos el número dado a la acción a realizar

        case "1": # Carga inicial de productos
            
            num_productos = input ("Ingrese el número de productos a cargar ") 
            if num_productos == " " or num_productos == "": # Si el número está vacío o presionan enter, imprimimos un aviso
                    print ("No se permiten caracteres vacíos ni letras")
            else: # Si imprimen un caracter primero nos aseguramos de que sea un digito
                if num_productos.isdigit(): # Si es un digito realizamos la acción correspondiente a este punto
                    for a in range (int(num_productos)): # Creamos un ciclo que se repita la cantidad de veces como herramienta fueron pedidas 
                        productos_cargar = input (f"Ingrese el nombre del producto {a+1} a cargar ") # En cada vuelta pedimos el nombre de la herramienta a cargar 
                        if productos_cargar == " " or productos_cargar == "" or productos_cargar in inventario: # Validamos que no este vacío ni duplicado
                            print ("No se permiten caracteres vacíos ni herramientas duplicadas")
                            break
                        else: 
                            stock_inicial = input (f"Ingrese el stock inicial de {productos_cargar}")
                            if stock_inicial == " " or stock_inicial == "": # Validamos que no este vacío
                                print ("No se permiten caracteres vacíos")
                                break
                            else:
                                precio_inicial = input (f"Ingrese el precio unitario de {productos_cargar}")
                                if precio_inicial == " " or precio_inicial == "": # Validamos que no este vacío
                                    print ("No se permiten caracteres vacíos") 
                                else: 
                                    inventario[productos_cargar.title()] = stock_inicial
                                    precios[productos_cargar.title()] = precio_inicial
                else:
                    print ("Por favor ingrese un número") # Si no ingresan un número, imprimimos el aviso

                print (inventario)
                print (precios)

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