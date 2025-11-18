# Ejercicio 25 Sistema de calificaciones. ############################################################################

cantidad_notas = (int(input(" Por favor ingresa la cantidad de notas a registrar ")))

notas = []

for i  in range(cantidad_notas):
    nota = float(input(f" Por favor ingresa otra nota {i + 1} "))
    notas.append(nota)

notas_promedio = sum(notas) / len(notas)

if notas_promedio >= 3.0:
    estado = " Aprobado "

elif notas_promedio >= 4.5:
    estado = " Sobresaliente "

elif notas_promedio >= 5.0:
    estado = " Excelnte "

else:
    estado = " Reporbado "



print(f" Notas ingresadas {notas} ")
print(f" Promedio de las notas ingresadas {notas_promedio} ")
print(f" Estado del curso {estado} ")


# Ejercicio 26 Carrito de compras ###################################################################################



## Ejercicio 27 cajero automatico ####################################################################

## Nivel 1: Fundamentos y Variables
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


# Ejercicio 28 Gestión de estudiantes (mini base de datos). #################################################
# Gestión de estudiantes con menú en consola

estudiantes = {}

def agregar_estudiante():
    matricula = input("Ingrese matrícula: ")
    if matricula in estudiantes:
        print(" Matrícula ya registrada.")
        return
    nombre = input("Ingrese nombre: ")
    edad = input("Ingrese edad: ")
    carrera = input("Ingrese carrera: ")
    estudiantes[matricula] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    print(" Estudiante agregado con éxito.")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\n--- Lista de estudiantes ---")
        for m, datos in estudiantes.items():
            print(f"Matricula: {m} || Estudiante: {datos['nombre']} || Carrera: {datos['carrera']} || Edad: {datos['edad']} años")
        print("----------------------------\n")

def buscar_estudiante():
    matricula = input("Ingrese matrícula a buscar: ")
    if matricula in estudiantes:
        datos = estudiantes[matricula]
        print(f"Encontrado: {datos['nombre']} - {datos['carrera']} ({datos['edad']} años)")
    else:
        print(" Estudiante no encontrado.")

def eliminar_estudiante():
    matricula = input("Ingrese matrícula a eliminar: ")
    if matricula in estudiantes:
        del estudiantes[matricula]
        print(" Estudiante eliminado.")
    else:
        print("Matrícula no encontrada.")

def menu():
    while True:
        print("\n--- Menú de Gestión de Estudiantes ---")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción inválida, intente de nuevo.")

# Ejecutar menú
menu()


# Ejercicio Calculadora avanzada (usar funciones).

import math

def sumar(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b

def potencia(a,b):
    return a ** b

def raiz(a,n=2):
    return a ** (1/n)

def seno(x):
    return math.sin(x)

def coseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def menu():
    while True:
        print("\n--- Calculadora Avanzada ---")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Potencia")
        print("6 - Raíz")
        print("7 - Seno")
        print("8 - Coseno")
        print("9 - Tangente")
        print("10 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "10":
            print(" Saliendo ...")
            break     

#       Operaciones con dos números
        if opcion in ["1","2","3","4","5"]:
            a = float(input("Ingresa el valor A: "))
            b = float(input("Ingresa el valor B: "))

            if opcion == "1":
                print(f"Resultado: {sumar(a, b)}")
            elif opcion == "2":
                print(f"Resultado: {resta(a, b)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicar(a, b)}")
            elif opcion == "4":
                print(f"Resultado: {division(a, b)}")
            elif opcion == "5":
                print(f"Resultado: {potencia(a, b)}")

#       Operaciones que requieren una variable numerica
        elif opcion in ["6","7","8","9"]:
            a = float(input("Ingresa el número: "))

            if opcion == "6":
                n = int(input("Ingrese el índice de la raíz (ej. 2 para raíz cuadrada): "))
                print(f"Resultado: {raiz(a, n)}")
            elif opcion == "7":
                print(f"Resultado: {seno(a)}")
            elif opcion == "8":
                print(f"Resultado: {coseno(a)}")
            elif opcion == "9":
                print(f"Resultado: {tangente(a)}")
        else:
            print(" Opción inválida, intente de nuevo.")

# Ejecutar menú
menu()