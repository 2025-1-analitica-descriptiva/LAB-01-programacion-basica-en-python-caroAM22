"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    # Diccionario para almacenar la suma por cada letra
    suma_por_letra = {}

    # Abrir y leer el archivo CSV
    with open("files/input/data.csv", "r") as file:
        # Leer todas las líneas
        lines = file.readlines()

        # Procesar cada línea
        for line in lines:
            # Dividir la línea por tabulaciones
            columns = line.strip().split("\t")
            letra = columns[0]
            valor = int(columns[1])

            # Sumar el valor a la letra correspondiente
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor

    # Convertir el diccionario a lista de tuplas y ordenar
    resultado = sorted(suma_por_letra.items())

    return resultado
