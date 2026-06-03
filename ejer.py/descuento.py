edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    

    #(Solicitar valor de compra y aplicar descuento)
compra = float(input("Ingrese el valor de la compra: "))

if compra > 1000:
    descuento = compra * 0.10
    total = compra - descuento
    print(f"¡Felicidades! Tienes un descuento del 10% (${descuento}).")
    print(f"Total a pagar: ${total}")
else:
    print(f"No hay descuento aplicado. Total a pagar: ${compra}")