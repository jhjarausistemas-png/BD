#ejercisio 7
notas = [3.5, 4.2, 2.8, 4.5, 3.9, 2.5, 4.0, 4.7]

#cantidad de estuduiantes
cantidad_estudiantes = len(notas)
print("Numero  de estudiantes:", cantidad_estudiantes)

#calcular suma y promedio 
suma = 0 
for nota in notas:
    suma = suma + nota

promedio = suma / cantidad_estudiantes
print("Promedio:", promedio)

#encontrar la mayor 
mayor = notas[0]

for nota in notas:
    if nota > mayor:
        mayor = nota

print("Nota mayor:", mayor)

#encontrar la menor
menor = notas[0]
for nota in notas: 
    if nota < menor:
        menor = nota

print("Nota menor:", menor)

#contar aprobados
aprobados = 0

for nota in notas:
    if nota >= 3.0:
        aprobados = aprobados + 1

print("Cantidad de aprobados:", aprobados)

#contar reprobados
reprobados = 0

for nota in notas:
    if nota < 3.0:
        reprobados = reprobados + 1

print("Cantidad de reprobados:", reprobados)

#mostrar notas mayores al promedio
print("Notas mayores al promedio:")

for nota in notas:
    if nota > promedio:
        print(nota)
