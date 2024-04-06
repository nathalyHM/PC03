
from functions import validar_fraccion, calcular_porcentaje, mostrar_resultado

def main():
    while True:
        fraccion_str = input("Ingrese una fracción en el formato X/Y: ")
        fraccion = validar_fraccion(fraccion_str)
        if fraccion:
            x, y = fraccion
            porcentaje = calcular_porcentaje(x, y)
            if porcentaje is not None:
                mostrar_resultado(porcentaje)
                break
            else:
                print("Error: División por cero. El denominador no puede ser cero.")
        else:
            print("Formato de fracción incorrecto o números inválidos. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()