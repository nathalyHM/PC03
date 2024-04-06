
import math

class Circulo:
    def __init__(self, radio):
        try:
            self.radio = float(radio)
            if self.radio <= 0:
                raise ValueError("El radio debe ser un número positivo.")
        except ValueError as e:
            print("Error:", e)
            self.radio = None
    
    def calcular_area(self):
        if self.radio is not None:
            try:
                area = math.pi * (self.radio ** 2)
                return area
            except TypeError:
                print("Error: El radio debe ser un número.")
        else:
            return None