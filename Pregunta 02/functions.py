
def obtener_calificaciones(entrada):
    try:
        calificaciones = [int(calificacion.strip()) for calificacion in entrada.split(',')]
        return calificaciones
    except ValueError:
        return None
    except ZeroDivisionError:
        return None