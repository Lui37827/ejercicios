nombre = input("Ingrese su nombre: ")
hora = int(input("Ingrese la hora (0-12): "))
genero = input("Género (M/F): ").upper()
if hora >= 0 and hora <= 12:
    if hora < 12:
        momento = "Buenos días"
    elif hora < 18:
        momento = "Buenas tardes"
    else:
        momento = "Buenas noches"
    if genero == "M":
        print(f"{momento}, bienvenido {nombre}.")
    elif genero == "F":
        print(f"{momento}, bienvenida {nombre}.")
    else:
        print(f"{momento}, hola {nombre}.")
else:
    print("Hora no válida.")

#opcion de salir 
continuar = True

while continuar:
    print("\n1. Saludar\n2. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("¡Hola! Espero que estés teniendo un gran día. ;v")
    elif opcion == "2":
        print("Saliendo del sistema... ¡Hasta luego!")
        continuar = False
    else:
        print("Opción no válida. Intenta de nuevo.")