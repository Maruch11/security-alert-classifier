"""
dataset.py

Responsable de cargar el dataset de alertas desde un archivo CSV
y convertir cada registro en una instancia de la clase Instancia.
"""

import csv
from modelos import Instancia

def cargar_dataset(ruta):
    """
    Carga un archivo CSV y retorna una lista de objetos Instancia.

    Args:
        ruta (str): Ruta al archivo CSV.

    Returns:
        list[Instancia]: Lista de alertas cargadas
    """
    instancias = []

    with open('data/alertas.csv', newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        # saltar el encabezado
        next(reader)

        for row in reader:
            if(len(row)) != 3:
                raise ValueError(
                    f"Fila invalida: {row}"
                )
            # Conversion de tipos
            intentos_login = int(row[0])
            ips_distintas = int(row[1])
            alerta = int(row[2])

            # Crear instancia
            instancia = Instancia(
                intentos_login,
                ips_distintas,
                alerta
            )

            instancias.append(instancia)

    return instancias