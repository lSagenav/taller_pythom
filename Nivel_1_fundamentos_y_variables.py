# Nivel 1 — Fundamentos y Variables


nombre = input("Por favor ingrese su nombre ")
edad = int(input("Por favor ingrese su edad "))

print(f"Hola {nombre} tienes {edad} años")



# Ejercicio 2 ########################################################

num1 = int(input("Por favor ingrese el primero numero a sumar "))
num2 = int(input("Por favor ingrese el segundo numero a sumar "))

result = num1 + num2

print(f"La suma de las dos cifras es {result}")



# Ejercicio 3 ########################################################

print("Vamos a calcular el area de un triangulo ")

base = int(input("Por favor ingrese la altura del triangulo "))
height = int(input("Por favor ingresa la base del triangulo "))

area = base * height / 2
print(f" El area del triangulo es {area}")


# Ejercicio 4 #######################################################

print("Conversor de grados Celsius a Fahrenheit.")

celcius = float(input("Cuantos grados Celsius deseas convertir "))
result = (celcius *9 / 5) + 32

print(f"La conversion es de {result} Grados Fahrenheit")


# Ejercicio 5 #######################################################

print(" Veremos l tipo de variable ")

data1 = input("ingresa su nombre ")
data2 = int(input("ingresa su edad "))
data3 = float(input("ingresa un dato numerico "))
data4 = bool(input("ingresa si o no "))

print(f"{type(data1)} !! {type(data2)} {type(data3)} {type(data4)}")


# Ejercicio 6 #######################################################


print(" Calculemos tu edad en 10 años ")

age = int(input(" Ingresa tu edad "))

future_age = age + 10

print(f"Tendras {future_age} años dentro de 10 años si no te mueres antes xD ")