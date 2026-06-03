edad = int(input("ingrese su edad: "))
if edad < 13:
    print("eres niño")
elif edad <= 17:
    print("eres adolescente")
elif edad >= 60:
    print("eres adulto mayor")
elif edad >= 18:
    print("eres adulto")






#calcular el lado=
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))
if lado1 == lado2 == lado3:
    print("El triángulo es Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es Isósceles.")
else:
    print("El triángulo es Escaleno.")