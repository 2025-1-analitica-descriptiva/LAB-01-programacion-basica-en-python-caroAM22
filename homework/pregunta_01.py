"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Abrir y leer el archivo CSV
    with open("files/input/data.csv", "r") as file:
        # Leer todas las líneas
        lines = file.readlines()

        # Inicializar la suma
        suma = 0

        # Procesar cada línea
        for line in lines:
            # Dividir la línea por tabulaciones
            columns = line.strip().split("\t")
            # Sumar el valor de la segunda columna (índice 1)
            suma += int(columns[1])

        return suma
