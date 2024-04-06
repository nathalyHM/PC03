
class Producto:
    def __init__(self, codigo, nombre, precio, año):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.año = año

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if self.productos:
            print("Productos en el catálogo:")
            for producto in self.productos:
                print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}")
        else:
            print("No hay productos en el catálogo.")
    
    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            print(f"Productos para el año {año}:")
            for producto in productos_filtrados:
                print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}")
        else:
            print(f"No hay productos para el año {año}.")