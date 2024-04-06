
from catalogo import Catalogo, Producto

def main():
    catalogo = Catalogo()
    
    
    catalogo.agregar_producto(Producto("001", "Llantas", 300, 2024))
    catalogo.agregar_producto(Producto("002", "Batería", 500, 2022))
    catalogo.agregar_producto(Producto("003", "Frenos", 100, 2021))
    catalogo.agregar_producto(Producto("004", "Aceite", 50, 2020))
    

    catalogo.mostrar_productos()
    
   
    año_filtro = 2024
    catalogo.filtrar_por_año(año_filtro)

if __name__ == "__main__":
    main()