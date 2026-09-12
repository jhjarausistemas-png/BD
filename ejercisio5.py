# ejercicio 5

nota1 = 3.5
nota2 = 4.2
nota3 = 2.8
nota4 = 4.5
nota5 = 3.9

# Calcular promedio
suma = nota1 + nota2 + nota3 + nota4 + nota5
promedio = suma / 5

print("Promedio:", promedio)

# Encontrar mayor nota
mayor = nota1
if nota2 > mayor:
    mayor = nota2
if nota3 > mayor:
    mayor = nota3
if nota4 > mayor:
    mayor = nota4
if nota5 > mayor:
    mayor = nota5
print("Mayor nota:", mayor)

# Encontrar menor nota
menor = nota1
if nota2 < menor:
    menor = nota2
if nota3 < menor:
    menor = nota3
if nota4 < menor:
    menor = nota4
if nota5 < menor:
    menor = nota5
print("Menor nota:", menor)

# Contar aprobados
aprobados = 0
if nota1 >= 3:
    aprobados = aprobados + 1
if nota2 >= 3:
    aprobados = aprobados + 1
if nota3 >= 3:
    aprobados = aprobados + 1
if nota4 >= 3:
    aprobados = aprobados + 1
if nota5 >= 3:
    aprobados = aprobados + 1
print("Cantidad de aprobados:", aprobados)
