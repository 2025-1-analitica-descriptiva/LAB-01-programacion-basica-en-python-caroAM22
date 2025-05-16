"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


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
            valor_col2 = int(columns[1])
            letras_col4 = columns[3].split(",")

            # Sumar el valor a cada letra de la columna 4
            for letra in letras_col4:
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_col2

    # Ordenar el diccionario por clave
    resultado = dict(sorted(suma_por_letra.items()))

    return resultado
