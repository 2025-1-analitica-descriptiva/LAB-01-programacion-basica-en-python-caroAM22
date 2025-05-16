"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    # Diccionario para almacenar el conteo de cada letra
    conteo = {}

    # Abrir y leer el archivo CSV
    with open("files/input/data.csv", "r") as file:
        # Leer todas las líneas
        lines = file.readlines()

        # Procesar cada línea
        for line in lines:
            # Obtener la primera columna
            letra = line.strip().split("\t")[0]
            # Incrementar el contador para esta letra
            conteo[letra] = conteo.get(letra, 0) + 1

    # Convertir el diccionario a lista de tuplas y ordenar
    resultado = sorted(conteo.items())

    return resultado
