
import random

def generar_numeros():
    return [random.randint(0, 50) for _ in range(30)]

def mostrar_lista(lista):
    print("Lista de números generados:")
    print(lista)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)