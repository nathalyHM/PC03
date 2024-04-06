
class Rectangulo:
    def __init__(self, largo, ancho):
        try:
            self.largo = float(largo)
            self.ancho = float(ancho)
            if self.largo <= 0 or self.ancho <= 0:
                raise ValueError("Tanto el largo como el ancho deben ser números positivos.")
        except ValueError as e:
            print("Error:", e)
            self.largo = None
            self.ancho = None
    
    def calcular_area(self):
        if self.largo is not None and self.ancho is not None:
            try:
                area = self.largo * self.ancho
                return area
            except TypeError:
                print("Error: Tanto el largo como el ancho deben ser números.")
        else:
            return None