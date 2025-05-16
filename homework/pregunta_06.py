"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    # Diccionario para almacenar los valores máximos y mínimos por clave
    valores_por_clave = {}

    # Abrir y leer el archivo CSV
    with open("files/input/data.csv", "r") as file:
        # Leer todas las líneas
        lines = file.readlines()

        # Procesar cada línea
        for line in lines:
            # Dividir la línea por tabulaciones
            columns = line.strip().split("\t")
            # Obtener el diccionario de la columna 5
            diccionario = columns[4]

            # Procesar cada par clave-valor
            for par in diccionario.split(","):
                clave, valor = par.split(":")
                valor = int(valor)

                # Actualizar máximo y mínimo para esta clave
                if clave not in valores_por_clave:
                    valores_por_clave[clave] = {"max": valor, "min": valor}
                else:
                    valores_por_clave[clave]["max"] = max(
                        valores_por_clave[clave]["max"], valor
                    )
                    valores_por_clave[clave]["min"] = min(
                        valores_por_clave[clave]["min"], valor
                    )

    # Convertir el diccionario a lista de tuplas y ordenar
    resultado = [
        (clave, datos["min"], datos["max"])
        for clave, datos in sorted(valores_por_clave.items())
    ]

    return resultado
