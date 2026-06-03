numero  = print(10)






































































print("hola mundo")
estudiantes=[["angel", 5.0,2.0,3.0],["fabian", 4.0,5.0,3.4],["rodigo", 2.9,3.5,4.2]]
print(estudiantes)
notas=[5.0,3.0,2.0]
notas.sort()
promedio = sum(notas) / len(notas)
print(f"notas ordenadas: {notas}")
print (f"promedio: {promedio:.1f}")
if promedio >= 3.0:
    print("aprobado")
else:
    print("reprobado