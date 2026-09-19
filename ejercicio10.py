
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    nota = float(input("Ingrese la nota: "))

    estudiante = [nombre, edad, nota]

    estudiantes.append(estudiante)

    print("Estudiante registrado")


def mostrar_estudiantes(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:

        for estudiante in estudiantes:

            print("Nombre:", estudiante[0])
            print("Edad:", estudiante[1])
            print("Nota:", estudiante[2])
            print("------------------------")


def buscar_estudiante(estudiantes):

    nombre = input("Ingrese el nombre a buscar: ")

    encontrado = False

    for estudiante in estudiantes:

        if estudiante[0].lower() == nombre.lower():

            print("Estudiante encontrado")
            print("Nombre:", estudiante[0])
            print("Edad:", estudiante[1])
            print("Nota:", estudiante[2])

            encontrado = True

    if encontrado == False:
        print("Estudiante no encontrado")


def promedio_estudiantes(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes")
    else:

        suma = 0

        for estudiante in estudiantes:
            suma = suma + estudiante[2]

        promedio = suma / len(estudiantes)

        print("Promedio:", promedio)


def mayor_nota(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes")
    else:

        mayor = estudiantes[0]

        for estudiante in estudiantes:

            if estudiante[2] > mayor[2]:
                mayor = estudiante

        print("Mayor nota:", mayor[2])
        print("Estudiante:", mayor[0])


def menor_nota(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes")
    else:

        menor = estudiantes[0]

        for estudiante in estudiantes:

            if estudiante[2] < menor[2]:
                menor = estudiante

        print("Menor nota:", menor[2])
        print("Estudiante:", menor[0])


def mostrar_aprobados(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes")
    else:

        print("Estudiantes aprobados:")

        for estudiante in estudiantes:

            if estudiante[2] >= 3:
                print(estudiante[0], "-", estudiante[2])


def ejercicio10():

    estudiantes = [
        ["Carlos", 20, 4.2],
        ["Maria", 19, 3.8],
        ["Juan", 21, 2.7]
    ]

    while True:

        print("==============================")
        print("     SISTEMA DE ESTUDIANTES")
        print("==============================")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Mostrar promedio")
        print("5. Mostrar mayor nota")
        print("6. Mostrar menor nota")
        print("7. Mostrar aprobados")
        print("8. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_estudiante(estudiantes)

        elif opcion == 2:
            mostrar_estudiantes(estudiantes)

        elif opcion == 3:
            buscar_estudiante(estudiantes)

        elif opcion == 4:
            promedio_estudiantes(estudiantes)

        elif opcion == 5:
            mayor_nota(estudiantes)

        elif opcion == 6:
            menor_nota(estudiantes)

        elif opcion == 7:
            mostrar_aprobados(estudiantes)

        elif opcion == 8:
            print("Programa terminado")
            break

        else:
            print("Opción inválida")


ejercicio10()