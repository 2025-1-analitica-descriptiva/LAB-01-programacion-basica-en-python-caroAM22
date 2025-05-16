"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    # Lista para almacenar los resultados
    resultados = []

    # Abrir y leer el archivo CSV
    with open("files/input/data.csv", "r") as file:
        # Leer todas las líneas
        lines = file.readlines()

        # Procesar cada línea
        for line in lines:
            # Dividir la línea por tabulaciones
            columns = line.strip().split("\t")
            letra = columns[0]

            # Contar elementos en la columna 4 (separados por coma)
            elementos_col4 = len(columns[3].split(","))

            # Contar elementos en la columna 5 (separados por coma)
            elementos_col5 = len(columns[4].split(","))

            # Agregar tupla al resultado
            resultados.append((letra, elementos_col4, elementos_col5))

    return resultados
