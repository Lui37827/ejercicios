n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
if n1 > n2:
    print(f"El primero ({n1}) es mayor que el segundo ({n2}).")
elif n2 > n1:
    print(f"El segundo ({n2}) es mayor que el primero ({n1}).")
else:
    print("Ambos números son iguales.")