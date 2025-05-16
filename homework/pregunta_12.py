"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

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
            diccionario = columns[4]

            # Sumar los valores de la columna 5
            suma_valores = 0
            for par in diccionario.split(","):
                valor = int(par.split(":")[1])
                suma_valores += valor

            # Agregar la suma al total de la letra
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma_valores

    # Ordenar el diccionario por clave
    resultado = dict(sorted(suma_por_letra.items()))

    return resultado
