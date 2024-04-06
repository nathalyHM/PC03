
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        try:
            area = math.pi * (self.radio ** 2)
            return area
        except TypeError:
            return None

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        try:
            area = self.largo * self.ancho
            return area
        except TypeError:
            return None

def area_cuadrado(lado):
    try:
        area = lado ** 2
        return area
    except TypeError:
        return None