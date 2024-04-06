
from circulo import Circulo

def main():
    radio_str = input("Ingrese el radio del círculo: ")
    circulo = Circulo(radio_str)
    area = circulo.calcular_area()
    if area is not None:
        print(f"El área del círculo con radio {circulo.radio} es: {area}")

if __name__ == "__main__":
    main()