"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    # Diccionario para almacenar los valores máximos y mínimos por letra
    valores_por_letra = {}

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

            # Actualizar máximo y mínimo para esta letra
            if letra not in valores_por_letra:
                valores_por_letra[letra] = {"max": valor, "min": valor}
            else:
                valores_por_letra[letra]["max"] = max(
                    valores_por_letra[letra]["max"], valor
                )
                valores_por_letra[letra]["min"] = min(
                    valores_por_letra[letra]["min"], valor
                )

    # Convertir el diccionario a lista de tuplas y ordenar
    resultado = [
        (letra, datos["max"], datos["min"])
        for letra, datos in sorted(valores_por_letra.items())
    ]

    return resultado
