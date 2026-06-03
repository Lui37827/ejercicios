def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Calcular Impuesto")
    print("3. Verificar Año Bisiesto")
    print("4. Salir")
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        print("¡Hola! Bienvenido al sistema.")
    elif opcion == "2":
        print("Ejecutando lógica de impuestos...")
        
    elif opcion == "3":
        print("Ejecutando lógica de año bisiesto...")
        
    elif opcion == "4":
        print("Saliendo del programa... ¡Adiós!")
        break 
    else:
        print("Opción no válida, intenta de nuevo.")
        
        
        
        
        