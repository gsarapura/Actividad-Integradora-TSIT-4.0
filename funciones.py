def promedio(lista):
    """
    Recibe una lista como argumento y retorna el promedio de sus elementos.
    """
    acumulador = 0
    for i in lista:
        acumulador += i
    promedio = acumulador // len(lista)
    return promedio