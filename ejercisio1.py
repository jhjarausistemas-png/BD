class estudiante:
    def __init__(self, nombre, edad, programa, semestre):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.edad = input("Ingrese la edad del estudiante: ")
        self.programa = input("Ingrese el programa del estudiante: ")
        self.semestre = input("Ingrese el semestre del estudiante: ")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Programa: {self.programa}")
        print(f"Semestre: {self.semestre}")
