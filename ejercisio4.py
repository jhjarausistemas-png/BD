#ejercisio4
#funciones y calculadora
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b


def multiplicacion(a,b):
    return a * b


def division(a,b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    else:
        return a / b

while True:
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == '5':
        print("Saliendo del programa...")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = suma(num1, num2)
        print(f"El resultado de la suma es: {resultado}")

    elif opcion == '2':
        resultado = resta(num1, num2)
        print(f"El resultado de la resta es: {resultado}")

    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
        print(f"El resultado de la multiplicación es: {resultado}")

    elif opcion == '4':
        resultado = division(num1, num2)
        print(f"El resultado de la división es: {resultado}")

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
