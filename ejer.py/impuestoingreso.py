salario = int(input("ingrese u salario: "))
if salario < 1500000:
    porcentaje = 0.0
elif salario <= 3000000:
    porcentaje = 0.10
else:
    porcentaje = 0.20
impuesto = salario * porcentaje
salario_neto = salario - impuesto
print(f"\n--- Resumen de Nómina ---")
print(f"Salario Bruto: ${salario:,.2f}")
print(f"Impuesto ({int(porcentaje*100)}%): ${impuesto:,.2f}")
print(f"Salario Neto: ${salario_neto:,.2f}")