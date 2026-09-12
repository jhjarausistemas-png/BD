#ejercisio 6
estudiantes = [
    "carlos",
    "maria",
    "juan",
    "ana",
    "luis",
    "laura",
    "anderson",
    "antonio",
    "miguel",
    "camila",
]
#mostar la lista de estudiantes
print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

#mostrar primer estudiante
print("Primer estudiante:", estudiantes[0])

#mostrar ultimo estudiante
print("Ultimo estudiante:", estudiantes[-1])

#mostrar  cantidad de estudiantes
print("Cantidad de estudiantes:", len(estudiantes))

#agregar un estudiante al final de la lista
estudiantes.append("sofia")

print("Lista de estudiantes actualizada:")
for estudiante in estudiantes:
    print(estudiante)

#elminar un estudiante de la lista
estudiantes.remove("juan")

print("Lista de estudiantes actualizada después de eliminar a Juan:")
for estudiante in estudiantes:
    print(estudiante)

#buscar un estudiante en la lista
buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
if buscar in estudiantes:
    print(buscar, "está en la lista de estudiantes.")
else:
    print(buscar, "no está en la lista de estudiantes.")
