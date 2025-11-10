
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

