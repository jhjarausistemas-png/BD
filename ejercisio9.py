notas = [
    [4.0, 3.5, 4.2],
    [3.0, 4.1, 3.7],
    [4.5, 3.8, 4.0],
    [2.8, 3.2, 3.5],
    [3.9, 4.5, 4.2]
]
#promedio de cada estudiante
print("Promedio de cada estudiante:")

for estudiante in notas:
    suma = 0

    for nota in estudiante: 
        suma += nota

    promedio = suma / 3

    print("promedio", promedio)

#promedio de cada asignatura
print("\nPromedio de cada asignatura:")

suma_programacion = 0
suma_matematicas = 0
suma_ingles = 0

for estudiante in notas:
    suma_programacion += estudiante[0]
    suma_matematicas += estudiante[1]
    suma_ingles += estudiante[2]

    promedio_programacion = suma_programacion / 5
    promedio_matematicas = suma_matematicas / 5
    promedio_ingles = suma_ingles / 5

    print("programación:", promedio_programacion)
    print("matemáticas:", promedio_matematicas)
    print("inglés:", promedio_ingles)

    #nota mayor 
    mayor = notas[0][0]

    for estudiante in notas:
        for nota in estudiante:
            if nota > mayor:
                mayor = nota

                print("\nLa nota mayor es:", mayor)

                #nota menor
                menor = notas[0][0]

                for estudiante in notas:
                    for nota in estudiante:
                        if nota < menor:
                            menor = nota

                            print("\nLa nota menor es:", menor)
