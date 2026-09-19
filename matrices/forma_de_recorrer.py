import numpy
import sys
print("Ingrese el tamaño de la matriz (n x n): ")
r1=int(input("Ingrese el número de renglones de la matriz 1"))
c1=int(input("Ingrese el número de columnas de la matriz 1"))
r2=int(input("Ingrese el número de renglones de la matriz 2"))
c2=int(input("Ingrese el número de columnas de la matriz 2import numpy
import sys

print("Ingrese el tamaño de la matriz (n x n): ")
r1 = int(input("Ingrese el número de renglones de la matriz 1: "))
c1 = int(input("Ingrese el número de columnas de la matriz 1: "))
r2 = int(input("Ingrese el número de renglones de la matriz 2: "))
c2 = int(input("Ingrese el número de columnas de la matriz 2: "))

if c1 != r2:
    print("No se pueden multiplicar las matrices")
    sys.exit()

matriz1 = numpy.zeros((r1, c1))
matriz2 = numpy.zeros((r2, c2))
matrizr = numpy.zeros((r1, c2))

print("Ingrese los elementos de la primera matriz:")
for i in range(r1):
    for c in range(c1):
        matriz1[i, c] = float(input(f"Elemento [{i + 1}][{c + 1}]: "))

print("Ingrese los elementos de la segunda matriz:")
for i in range(r2):
    for c in range(c2):
        matriz2[i, c] = float(input(f"Elemento [{i + 1}][{c + 1}]: "))

for i in range(r1):
    for c in range(c2):
        suma = 0
        for k in range(r2):
            suma += matriz1[i, k] * matriz2[k, c]
        matrizr[i, c] = suma

print(matrizr)"))

# Verificar si las matrices se pueden multiplicar
if c1 != r2:
    print("No se pueden multiplicar las matrices")
    sys.exit()
    matriz1 = numpy.zeros((r1, c1))
    matriz2 = numpy.zeros((r2, c2))
    matrizr = numpy.zeros((r1, c2))
    print("Ingrese los elementos de la primera matriz:")
    for i in range(0, r1):
        for c in range(0, c1):
            matriz1[i ,c] = str(input(f"Elemento [{i+1}][{c+1}]: "))
    print("Ingrese los elementos de la segunda matriz:")
    for i in range(0, r2):
        for c in range(0, c2):
            matriz2[i ,c] = str(input(f"Elemento [{i+1}][{c+1}]: "))
#operación de multiplicación de matrices
for i in range(0, r1):
    for c in range(0, c2):
        for k in range(0, r2):
            matrizr[i ,c] += matriz1[i ,k] * matriz2[k ,c]
print(matrizr)