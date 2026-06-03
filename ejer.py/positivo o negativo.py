numero = int(input("Ingresa un número: "))
if numero == 0:
    print("el numero es cero")
elif numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")
    
    



    #3 numeros (cual es mayor )
    
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
if n1 == n2 == n3:
    print("Los tres números son iguales.")
elif n1 >= n2 and n1 >= n3:
    print(f"El mayor es el primer número: {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"El mayor es el segundo número: {n2}")
else:
    print(f"El mayor es el tercer número: {n3}")

# (nultiplo de 5 )
n5= float(input("ingresa un numero: "))
if n5 % 5 == 0:
    print("el numero es multiplo de 5 ")
else:
    print (" el numero no es multiplo de 5 ")





