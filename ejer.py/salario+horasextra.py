salario_base = float(input("Salario base: "))
horas_extra = float(input("Horas extra: "))
if salario_base > 0:
    v_hora = salario_base / 160
    # Anidado: si hay extras, aplica 1.5, si no, es 0
    pago_extra = (horas_extra * v_hora * 1.5) if horas_extra > 0 else 0
    print(f"Total a pagar: ${salario_base + pago_extra:,.2f}")
else:
    print("Salario no válido")