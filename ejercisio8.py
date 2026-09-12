#productos

productos = [
    "teclado",
    "raton",
    "monitor",
    "impresora",
    "memoria ram",
    "disco ssd"
]

buscar = input("Ingrese el producto que desea buscar: ")

if buscar in productos:
    print("producto encontrado")
else:   
    print("producto no encontrado")
