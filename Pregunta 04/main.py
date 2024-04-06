
from rectangulo import Rectangulo

def main():
    largo = input("Ingrese el largo del rectángulo: ")
    ancho = input("Ingrese el ancho del rectángulo: ")
    
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    
    if area is not None:
        print(f"El área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho} es: {area}")

if __name__ == "__main__":
    main()