import json
import os

class Producto:
    def __init__(self, nombre, codigo, precio, proveedor, existencia, estado, descuento):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.proveedor = proveedor
        self.existencia = existencia
        self.estado = estado  # 'A' = Aprobado, 'N' = No Aprobado
        self.descuento = descuento

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Código: {self.codigo}, Precio: {self.precio}, "
              f"Proveedor: {self.proveedor}, Existencia: {self.existencia}, "
              f"Estado: {self.estado}, Descuento: {self.descuento}%")

def cargar_productos(filename):
    if not os.path.exists(filename):
        return []
    
    with open(filename, 'r') as file:
        return [Producto(**data) for data in json.load(file)]

def guardar_productos(filename, productos):
    with open(filename, 'w') as file:
        json.dump([vars(prod) for prod in productos], file)

def codigo_existente(productos, codigo):
    return any(prod.codigo == codigo for prod in productos)

def agregar_producto(productos):
    nombre = input("Ingrese nombre: ")
    codigo = input("Ingrese código: ")

    if codigo_existente(productos, codigo):
        print("Error: El código de producto ya existe.")
        return

    precio = float(input("Ingrese precio: "))
    proveedor = input("Ingrese proveedor: ")
    existencia = int(input("Ingrese existencia: "))
    estado = input("Ingrese estado (A/N): ")
    descuento = float(input("Ingrese descuento: "))

    nuevo_prod = Producto(nombre, codigo, precio, proveedor, existencia, estado, descuento)
    productos.append(nuevo_prod)
    guardar_productos("productos.json", productos)
    print("Producto agregado con éxito.")

def buscar_producto(productos):
    criterio = input("Buscar por código o nombre: ")
    encontrado = False

    for prod in productos:
        if prod.codigo == criterio or criterio in prod.nombre:
            prod.mostrar()
            encontrado = True

    if not encontrado:
        print("No se encontraron productos.")

def modificar_producto(productos):
    codigo = input("Ingrese el código del producto a modificar: ")

    for prod in productos:
        if prod.codigo == codigo:
            print("Modificar producto:")
            print(f"Nombre actual: {prod.nombre}, Ingrese nuevo nombre: ", end="")
            prod.nombre = input()
            print(f"Precio actual: {prod.precio}, Ingrese nuevo precio: ", end="")
            prod.precio = float(input())
            print(f"Proveedor actual: {prod.proveedor}, Ingrese nuevo proveedor: ", end="")
            prod.proveedor = input()
            print(f"Existencia actual: {prod.existencia}, Ingrese nueva existencia: ", end="")
            prod.existencia = int(input())
            print(f"Estado actual: {prod.estado}, Ingrese nuevo estado (A/N): ", end="")
            prod.estado = input()
            print(f"Descuento actual: {prod.descuento}, Ingrese nuevo descuento: ", end="")
            prod.descuento = float(input())

            guardar_productos("productos.json", productos)
            print("Producto modificado con éxito.")
            return

    print("Producto no encontrado.")

def main():
    productos = cargar_productos("productos.json")
    opcion = 0

    while opcion != 4:
        print("\nMenu de Productos:")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Modificar producto")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_producto(productos)
        elif opcion == 2:
            buscar_producto(productos)
        elif opcion == 3:
            modificar_producto(productos)
        elif opcion == 4:
            print("Saliendo...")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
