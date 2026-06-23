"""
Prueba unitaria con casos simples para verificar el cálculo de distancias, 
la selección de vecinos y la clasificación final de instancias.
El valor de k influye directamente en la clasificación.
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from modelos import Instancia, ModeloKNN

A = Instancia(1, 1, 0)
B = Instancia(2, 2, 0)
C = Instancia(10, 10, 1)

# Prueba caso 1
modelo = ModeloKNN(1, "euclideana")

modelo.entrenar([A, B, C])

X = Instancia(9, 9)

print(modelo.predecir(X))

# Prueba caso 2
modelo = ModeloKNN(3, "euclideana")

modelo.entrenar([A, B, C])

X = Instancia(9, 9)

print(modelo.predecir(X))

