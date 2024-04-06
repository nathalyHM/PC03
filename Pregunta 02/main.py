
from functions import obtener_calificaciones

def main():
    while True:
        entrada = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones = obtener_calificaciones(entrada)
        if calificaciones is not None:
            print("Calificaciones ingresadas:", calificaciones)
            break
        else:
            print("Error: Algunas calificaciones no son números enteros. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()