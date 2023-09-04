# ## Ejercicio A

# Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# 1. El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar. Se trata de un
# entorno completamente observable, determinista y estático.

from random import randint, random
import numpy as np

class Environment:
    def __init__(self):
        matriz = np.full((100, 100), '_', dtype=str)
        #print(matriz)