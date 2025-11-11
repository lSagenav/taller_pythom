
## bjetivo: Crear, recorrer, modificar y eliminar elementos en listas.

# Ejercicio 19 Lista de frutas. #############################################################################

frutas = []

while True:
    fruta = input("Ingresa una fruta o Fin para terminar ")

    if fruta.lower() == "fin":
        break

    frutas.append(fruta)

print(f" Las frutas que ingresaste son {frutas}")


# Ejercicio 20 Agregar y eliminar frutas. ###################################################################

canasta = []

# Parte 1: Agregar frutas
while True:
    item = input("Escribe una fruta para agregar (o 'fin' para terminar y eliminar alguna fruta): ")
    
    if item.lower() == "fin":
        break
    
    canasta.append(item)

print(f"\nFrutas en la canasta: {canasta}")

# Parte 2: Eliminar una fruta
quitar = input("\n¿Quieres eliminar alguna fruta? Escribe su nombre (o 'no' para saltar): ")

if quitar.lower() != "no":
    if quitar in canasta:
        canasta.remove(quitar)
        print(f"{quitar} fue eliminada de la canasta.")
    else:
        print(f"{quitar} no está en la canasta.")

print(f"\nCanasta final: {canasta}")


# Ejercvicio 21 Buscar un elemento en la lista. ##############################################################


canasta2 = ["manzana", "pera", "mango", "banana"]

buscar = input("¿Qué fruta quieres buscar en la canasta? ")

if buscar in canasta2:
    print(f"{buscar} está en la canasta.")
else:
    print(f"{buscar} no se encuentra en la canasta.")


# Ejercicio 22 Lista de números y promedio. ##################################################################

numeros = []
cantidad = int(input("¿Cuántos números vas a ingresar? "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

promedio = sum(numeros) / len(numeros)

print(f"La lista de números es: {numeros}")
print(f"El promedio es: {promedio}")


# Ejercicio 23 Números pares: guardar solo los pares. #########################################################
import random

numList = int(input("por favor ingresa la cantidad de numeros que deseas tener "))
listNum = [numList]
listPares = []

for i in range (numList):
    numero = random.randint(1, 100)
    listNum.append(numero)

for numero in listNum:
    if numero % 2 == 0:
        listPares.append(numero)

print(f" la lista orogonal es esta {listNum}")
print(f" la lista con los pares es {listPares}")


# Ejercicio 22 Eliminar duplicados. ##############################################################################

numer = int(input(" Por favor ingresa un numero "))
lista = [numer]
sin_duplicados =[]
eliminados = []

for i in range(numer):
    number = int(input(f" Ingresa el numero {i + 1 } "))
    lista.append(number)


for num in lista:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

for num in lista:
    if lista.count(num) > 1 and num not in eliminados:
         eliminados.append(num)


print(f" Lista orogial es {lista} ")
print(f" Lista sin duplicados  {sin_duplicados} ")
print(f" los numeros duplicados son  {eliminados} ")



