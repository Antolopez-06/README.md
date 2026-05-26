# Trabajo Practico N° 2 - Organización Empresarial

inventario = {} # Diccionarios a utilizar
precios = {}

while True: # Bucle para que luego de cada opción vuelvas al menú

    print ("Tienda BluestCat")  # Cargamos la bienvenida y el menú de opciones
    print ("1. Carga de Productos con su Stock y Precios")
    print ("2. Visualización de Inventario")
    print ("3. Visualización de Precios")
    print ("4. Consulta de Stock (Existencias Individuales)")
    print ("5. Consulta de Precio Individual")
    print ("6. Reporte de Agotados")
    print ("7. Actualización de Stock (Ingresos)")
    print ("8. Actualización de Precios")
    print ("9. Carga de Ventas")
    print ("10. Estadísticas")
    print ("11. Salir ")

    opcion = input ("Ingrese la opción a realizar ") # Pedimos que elijan un número del 1 al 10

    match opcion: # Unimos el número dado a la acción a realizar

        case "1": # Carga Inicial de Productos con su Stock y Precios
            
            num_productos = input ("Ingrese el número de productos a cargar ") 
            if num_productos == " " or num_productos == "": # Si el número está vacío o presionan enter, imprimimos un aviso
                    print ("No se permiten caracteres vacíos ni letras")
            else: # Si imprimen un caracter primero nos aseguramos de que sea un digito
                if num_productos.isdigit(): # Si es un digito realizamos la acción correspondiente a este punto
                    for a in range (int(num_productos)): # Creamos un ciclo que se repita la cantidad de veces como herramienta fueron pedidas 
                        productos_cargar = input (f"Ingrese el nombre del producto {a+1} a cargar ") # En cada vuelta pedimos el nombre de la herramienta a cargar 
                        if productos_cargar == " " or productos_cargar == "" or productos_cargar.strip() in inventario: # Validamos que no este vacío ni duplicado
                            print ("No se permiten caracteres vacíos ni herramientas duplicadas")
                            break
                        else: 
                            stock_inicial = input (f"Ingrese el stock inicial de {productos_cargar.strip()} ")
                            if stock_inicial == " " or stock_inicial == "": # Validamos que no este vacío
                                print ("No se permiten caracteres vacíos")
                                break
                            else:
                                precio_inicial = input (f"Ingrese el precio unitario de {productos_cargar} ")
                                if precio_inicial == " " or precio_inicial == "": # Validamos que no este vacío
                                    print ("No se permiten caracteres vacíos") 
                                else: 
                                    inventario[productos_cargar.title().strip()] = stock_inicial
                                    precios[productos_cargar.title().strip()] = precio_inicial
                else:
                    print ("Por favor ingrese un número") # Si no ingresan un número, imprimimos el aviso

                print ("Información cargada correctamente")

        case "2": # Visualización de Inventario"

            if inventario:
                print ("El inventario actual es el siguiente:")
                print (inventario)
            else: 
                print ("Por favor cargue el inventario primero")

        case "3": # Visualización de Precios
            
            if precios:
                print ("La lista de precios es la siguiente:")
                print (precios)
            else: 
                print ("Por favor cargue los precios primero")
                        
        case "4": # Consulta de Stock (Existencias Individuales)
            
            nombre_producto = input ("Ingrese el nombre del producto que quiere saber el stock ")

            if nombre_producto.title().strip() in inventario:
                print (f"Del producto {nombre_producto.title().strip()} hay {inventario[nombre_producto.title().strip()]} unidades")
            else:
                print ("Ese producto no se encuentra en el sistema")

        case "5": # Consulta de Precio Individual
            
            nombre_producto = input ("Ingrese el nombre del producto que quiere saber el precio ")

            if nombre_producto.title().strip() in inventario:
                print (f"El producto {nombre_producto.title().strip()} sale ${precios[nombre_producto.title().strip()]}")
            else:
                print ("Ese producto no se encuentra en el sistema")

        case "6": # Reporte de Agotados

            for clave, valor in inventario.items():
                if valor == 0:
                    print(f"{clave} tiene stock cero")

        case "7": #  Actualización de Stock (Ingresos)
            
            nombre_producto = input ("Ingrese el nombre del producto que quiere agregar stock ")

            if nombre_producto.strip() != "": # Validamos que no este vacío
                if nombre_producto.title().strip() in inventario:
                    cantidad_stock = input ("Ingrese la cantidad de stock que quiere agregar ")
                    if cantidad_stock.isdigit():
                        stock_previo = inventario[nombre_producto.title().strip()]
                        stock_final = int(stock_previo) + int(cantidad_stock)
                        inventario[nombre_producto.title().strip()] = stock_final
                        print ("Se actualizó el inventario correctamente")
                    else:
                        print ("Por favor ingrese un número")
                else:
                    print ("El producto ingresado no se encuentra en el sistema")
            else:
                print ("El producto no puede estar vacío")

        case "8": # Actualización de Precios

            nombre_producto = input ("Ingrese el nombre del producto que quiere modificar el precio ")

            if nombre_producto.strip() != "": # Validamos que no este vacío
                if nombre_producto.title().strip() in inventario:
                    precio_actual = input ("Ingrese el nuevo precio ")
                    if precio_actual.isdigit():
                        precios[nombre_producto.title().strip()] = precio_actual
                        print ("Se actualizó el precio correctamente")
                    else:
                        print ("Por favor ingrese un número")
                else:
                    print ("El producto ingresado no se encuentra en el sistema")
            else:
                print ("El producto no puede estar vacío")
            

        case "9":
            pass
        case "10":
            pass
        case _:
            print ("Por favor ingrese un número del 1 al 10")