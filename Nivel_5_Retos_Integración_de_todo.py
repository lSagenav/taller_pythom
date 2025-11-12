# # Ejercicio 25 Sistema de calificaciones. ############################################################################

# cantidad_notas = (int(input(" Por favor ingresa la cantidad de notas a registrar ")))

# notas = []

# for i  in range(cantidad_notas):
#     nota = float(input(f" Por favor ingresa otra nota {i + 1} "))
#     notas.append(nota)

# notas_promedio = sum(notas) / len(notas)

# if notas_promedio >= 3.0:
#     estado = " Aprobado "

# elif notas_promedio >= 4.5:
#     estado = " Sobresaliente "

# elif notas_promedio >= 5.0:
#     estado = " Excelnte "

# else:
#     estado = " Reporbado "



# print(f" Notas ingresadas {notas} ")
# print(f" Promedio de las notas ingresadas {notas_promedio} ")
# print(f" Estado del curso {estado} ")


# # Ejercicio 26 Carrito de compras ###################################################################################

# def agregarProducto(carrito):
#     nombre = input(" Ingrese el nombre del producto: ")
#     try:
#         precio = float(input(" Ingrese el valor del producto: "))
#         carrito.append({"nombre": nombre, "precio": precio})
#         print(f" Producto {nombre} Agregado correctamente ")
#     except ValueError:
#         print(" Precio Invalido. Intenta de nuevo ")

# def eliminar_producto(carrito):
#     nombre = input(" Ingrese el nombre del producto que desea eliminar ")
#     encontrado = False
#     for producto in carrito:
#         if producto["nombre"].lower() == nombre.lower():
#             carrito.remove(producto)
#             print(f" El producto {producto} Fue eliminado exitosamente ")
#             encontrado = True
#             break
#     if not encontrado:
#         print(f" el producto {producto} no esta en el carrito ")

# def mostrar_carrito(carrito):
#     if not carrito:
#         print("El carrito está vacío. ")
#     else:
#         print("\nContenido del carrito: ")
#         for producto in carrito:
#             print(f"- {producto['nombre']}: ${producto['precio']}")


# def calcular_total(carrito):
#     total = sum(producto["precio"] for producto in carrito)
#     print(f"\nTotal a pagar: ${total}")

# def ejecutar_carrito():
#     carrito = []

#     while True:
#         print("\n--- MENÚ DEL CARRITO ---")
#         print("1. Agregar producto ")
#         print("2. Eliminar producto ")
#         print("3. Mostrar carrito ")
#         print("4. Calcular total ")
#         print("5. Salir ")

#         opcion = input("Selecciona una opción (1-5): ")

#         if opcion == "1":
#             agregarProducto(carrito)
#         elif opcion == "2":
#             eliminar_producto(carrito)
#         elif opcion == "3":
#             mostrar_carrito(carrito)
#         elif opcion == "4":
#             calcular_total(carrito)
#         elif opcion == "5":
#             print("Gracias por usar el carrito de compras. ¡Hasta pronto!")
#             break
#         else:
#             print("Opción no válida. Intenta de nuevo.")

# ejecutar_carrito()

# ## Ejercicio 27 cajero automatico ####################################################################

# Nivel 1: Fundamentos y Variables
saldo = 1000
pin_correcto = "1234"
transacciones = []

# Nivel 2: Condicionales
pin = input("Ingrese su PIN: ")
if pin != pin_correcto:
    print("PIN incorrecto. Acceso denegado.")
else:
    # Nivel 3: Bucles
    while True:
        print("\n--- Menú Cajero ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver transacciones")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Su saldo actual es: ${saldo}")
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            saldo += monto
            transacciones.append(f"Depósito: +${monto}")
            print("Depósito exitoso.")
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= saldo:
                saldo -= monto
                transacciones.append(f"Retiro: -${monto}")
                print("Retiro exitoso.")
            else:
                print("Fondos insuficientes.")
        elif opcion == "4":
            print("Historial de transacciones:")
            for t in transacciones:
                print("-", t)
        elif opcion == "5":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


## Ejercicio 28 Gestión de estudiantes (mini base de datos). #################################################

