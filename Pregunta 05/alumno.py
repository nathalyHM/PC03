
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
    
    def set_age(self, edad):
        try:
            self.edad = int(edad)
        except ValueError:
            print("Error: La edad debe ser un número entero.")
    
    def set_notas(self, *notas):
        for nota in notas:
            try:
                nota = float(nota)
                if nota < 0 or nota > 20:
                    raise ValueError("La nota debe estar entre 0 y 20.")
                self.notas.append(nota)
            except ValueError as e:
                print("Error:", e)