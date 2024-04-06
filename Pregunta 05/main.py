
from alumno import Alumno

def main():
    nombre = input("Ingrese el nombre del alumno: ")
    numero_registro = input("Ingrese el número de registro del alumno: ")
    
    alumno = Alumno(nombre, numero_registro)
    
    edad = input("Ingrese la edad del alumno: ")
    alumno.set_age(edad)
    
    cantidad_notas = int(input("Ingrese la cantidad de notas del alumno: "))
    for i in range(cantidad_notas):
        nota = input(f"Ingrese la nota {i + 1} del alumno: ")
        alumno.set_notas(nota)
    
    print("\nInformación del alumno:")
    alumno.display()

if __name__ == "__main__":
    main()