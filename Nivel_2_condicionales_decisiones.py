# Ejercicio 7 ################################################################

age = int(input(" Por favor ingresa su edad "))

if age >=18:
    print(" Eres maoyr de edad ")
else:
    print(" Eres menor de edad ")


# Ejercicio 8 ###############################################################

number = int(input(" Por favor ingresa un numero "))

if number > 0:
    print(" El numero es positivo")
elif number < 0:
    print(" El numero es negativo")
else:
    print(" El numero es cero ")


# Ejercicio 9 ##############################################################

parInpar = int(input(" ingrese el numero a validar "))

if parInpar % 2 == 0:
    print(" El numero es par ")
else:
    print(" El numero es impar ")


# Ejercicio 10 ##############################################################

num1 = float(input(" Ingresa el primero numero "))
num2 = float(input(" Ingresa el segundo numero "))

operation= input("Ingresa la operación (+, -, *, /): ")

if operation == "+":
    print("Resultado:", num1 + num2)
elif operation == "-":
    print("Resultado:", num1 - num2)
elif operation == "*":
    print("Resultado:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Operador no válido")



# Ejericio 11 ###############################################################

nota = float(input(" Cual fue su nota "))

if nota >= 5:
    print(" su nota es Excelente")

elif nota >=3 and nota <= 4.9:
    print(" Fuiste aprobado")

else:
    print(" fuiste reprobado")



# Ejercicio 12 #############################################################

dta1 = int(input(" Ingrese el primer dato "))
dta2 = int(input(" Ingrese el segundo dato "))
dta3 = int(input(" Ingrese el tercero dato "))

if dta1 > dta2 and  dta1 > dta3 :
    print(f"El numero {dta1} es el mayor ")
elif dta2 > dta3 and dta2 > dta1:
    print(f"El numero {dta2} es mayor ")
else:
    print(f"el numero {dta3} es el meyor ")

if dta1 < dta2 and  dta1 < dta3 :
    print(f"El numero {dta1} es el menor ")
elif dta2 < dta3 and dta2 < dta1:
    print(f"El numero {dta2} es menor ")
else:
    print(f"el numero {dta3} es el menor ")

