
def validar_fraccion(fraccion_str):
    try:
        x, y = map(int, fraccion_str.split('/'))
        if x <= 0 or y <= 0:
            raise ValueError("Los números deben ser positivos")
        if x > y:
            raise ValueError("El numerador debe ser menor o igual al denominador")
        return x, y
    except (ValueError, ZeroDivisionError):
        return None

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100
    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return round(porcentaje)

def mostrar_resultado(porcentaje):
    if porcentaje == 'E':
        print("Cantidad de combustible en el tanque: E (menor al 1%)")
    elif porcentaje == 'F':
        print("Cantidad de combustible en el tanque: F (mayor al 99%)")
    else:
        print(f"Cantidad de combustible en el tanque: {porcentaje}%")