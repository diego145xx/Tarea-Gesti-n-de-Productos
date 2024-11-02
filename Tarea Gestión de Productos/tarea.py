import os

# Lista de productos
productos = []

def cargar_datos():
    """Carga los datos desde un archivo productos.txt."""
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(", ")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })

def guardar_datos():
    """Guarda los datos en un archivo productos.txt."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

def añadir_producto():
    """Añade un nuevo producto a la lista."""
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para el precio.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para la cantidad.")
    
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Producto añadido con éxito.")

def ver_productos():
    """Muestra la lista de productos."""
    if not productos:
        print("No hay productos en el inventario.")
        return
    print("Lista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    """Actualiza un producto existente en la lista."""
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            while True:
                campo = input("¿Qué deseas actualizar? (nombre/precio/cantidad): ").lower()
                if campo == "nombre":
                    nuevo_nombre = input("Introduce el nuevo nombre: ")
                    producto["nombre"] = nuevo_nombre
                    print("Nombre actualizado con éxito.")
                    return
                elif campo == "precio":
                    while True:
                        try:
                            nuevo_precio = float(input("Introduce el nuevo precio: "))
                            producto["precio"] = nuevo_precio
                            print("Precio actualizado con éxito.")
                            return
                        except ValueError:
                            print("Por favor, introduce un valor numérico para el precio.")
                elif campo == "cantidad":
                    while True:
                        try:
                            nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                            producto["cantidad"] = nueva_cantidad
                            print("Cantidad actualizada con éxito.")
                            return
                        except ValueError:
                            print("Por favor, introduce un valor numérico para la cantidad.")
            print("Opción no válida.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    """Elimina un producto de la lista."""
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for i, producto in enumerate(productos):
        if producto["nombre"] == nombre:
            del productos[i]
            print("Producto eliminado con éxito.")
            return
    print("Producto no encontrado.")

def menu():
    """Muestra el menú principal y gestiona la entrada del usuario."""
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    cargar_datos()  # Carga los productos al iniciar
    menu()          # Inicia el menú