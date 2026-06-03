tipo = input("Tipo de cliente (1=VIP, 2=Normal): ")
monto = float(input("Monto de la compra: "))

if tipo == "1":
    descuento = monto * 0.20
    print(f"Cliente VIP - Descuento del 20%: ${descuento}")
elif tipo == "2":
    descuento = monto * 0.05
    print(f"Cliente Normal - Descuento del 5%: ${descuento}")
else:
    print("Tipo de cliente no válido")
    descuento = 0

print(f"Total a pagar: ${monto - descuento}")


