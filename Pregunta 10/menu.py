
from figuras import Circulo, Rectangulo, area_cuadrado

def mostrar_menu():
    print("\nMenu:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            area = circulo.calcular_area()
            if area is not None:
                print(f"El área del círculo es: {area}")
            else:
                print("Error: El radio debe ser un número.")
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            area = rectangulo.calcular_area()
            if area is not None:
                print(f"El área del rectángulo es: {area}")
            else:
                print("Error: El largo y el ancho deben ser números.")
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = area_cuadrado(lado)
            if area is not None:
                print(f"El área del cuadrado es: {area}")
            else:
                print("Error: El lado del cuadrado debe ser un número.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()