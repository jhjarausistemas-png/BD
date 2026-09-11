# ejercicio3

#numeros del 1 al 50
print("numeros del 1 al 50")
for numero in range(1, 51):
    print(numero)

#numeros pares
print("numeros pares")
for numero in range(1, 51):
    if numero % 2 == 0:
        print(numero)

#numeros impares
print("numeros impares")
for numero in range(1, 51):
    if numero % 2 != 0:
        print(numero)

#multiplos del 5
print("multiplos del 5")
for numero in range(1, 51):
    if numero % 5 == 0:
        print(numero)

#suma de los numeros del 1 al 50
print("suma de los números del 1 al 50")
suma = 0
for numero in range(1, 51):
    suma =suma + numero

print("La suma de los números del 1 al 50 es:", suma)
