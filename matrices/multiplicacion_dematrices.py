filasA = int(input("Filas de la matriz A: "))
columnasA = int(input("Columnas de la matriz A: "))
filasB = int(input("Filas de la matriz B: "))
columnasB = int(input("Columnas de la matriz B: "))

if columnasA != filasB:
    print("No se pueden multiplicar las matrices")
else:
    A = []
    B = []

    print("\nIngrese los datos de A:")
    for i in range(filasA):
        fila = []
        for j in range(columnasA):
            fila.append(int(input(f"A[{i}][{j}]: ")))
        A.append(fila)

    print("\nIngrese los datos de B:")
    for i in range(filasB):
        fila = []
        for j in range(columnasB):
            fila.append(int(input(f"B[{i}][{j}]: ")))
        B.append(fila)

    C = [[0] * columnasB for _ in range(filasA)]

    for i in range(filasA):
        for j in range(columnasB):
            for k in range(columnasA):
                C[i][j] += A[i][k] * B[k][j]

    print("\nResultado:")
    for fila in C:
        print(fila)