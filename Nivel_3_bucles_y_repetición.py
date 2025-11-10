# Ejercicio 13 Contar del 1 al 10. ###############################################

conta = int(input("cantidad de nueros a imprimir "))

for i in range(conta):
    conta = conta +i
    print(f"Los numeros son {i}")




# Ejercicio 14 Sumatoria del 1 al n. #############################################

n = int(input("Ingresa un número: "))

# Variable acumuladora
suma = 0

# Bucle para sumar desde 1 hasta n
for i in range(1, n + 1):
    suma = suma + i

# Mostrar el resultado
print(f" La sumatoria del 1 al n es {suma} ")



# Ejercicio 15  Tabla de multiplicar. ############################################

tab = int(input(" Tabla de multiplicar "))

for i in range(1,11):
    print(f"{tab} x {i} = {tab * i} ")


# Ejercicio 16 Contador regresivo con while. #####################################


conta = int(input("cuenta regresiva de x numero  "))

while conta >= 0:
    print(conta)    
    conta -= 1


# Ejercicio 17 ##################################################################
    

import random

num_secre = int(input("porfa ingresa el rango de los numeros "))
num_secret = random.randint(1,num_secre)



intento = None

while intento != num_secret:
    intento = int(input("Ingresa tu número: "))
    
    if intento < num_secret:
        print("El número secreto es más grande.")
    elif intento > num_secret:
        print("El número secreto es más pequeño.")
    else:
        print("¡Felicitaciones! Adivinaste el número:", num_secret)


# Ejercicio 18 ###################################################################

#https://github.com/daveshb/riwipython/blob/main/modulo1/semana1/Taller1.md

intentos_num = int(input(" Por favor ingresa el valor a sumar "))
suma_total = 0

while intentos_num != 0:
    suma_total += intentos_num
    intentos_num = int(input(" Por favor ingresa otro valor "))

print(f" La suma total es {suma_total}")
 