# ejercicio2

nota = float(input("Ingrese la nota definitiva: "))

if nota < 0 or nota > 5:
    print("La nota ingresada no es válida.")

elif nota >= 3:
    print("El estudiante ha aprobado")

else:
    print("El estudiante ha reprobado")
