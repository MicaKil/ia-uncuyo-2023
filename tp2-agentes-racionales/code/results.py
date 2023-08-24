
# ## Ejercicio D)
# Evaluar el desempeño del agente reflexivo (medida de desempeño y unidades de tiempo consumidas) para:
# 1. Entornos de: 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128 
# 2. Porcentaje de Suciedad en el ambiente: 0.1, 0.2, 0.4, 0.8
# 3. Repetir 10 veces cada combinación.

# **Nota:** Se recomienda elaborar una tabla en google sheets (o algo similar) en donde se presente los resultados en términos de la medida 
# de rendimiento para cada uno de los casos. Esto luego se podrá utilizar para realizar alguna visualización de los resultados.

# ## Ejercicio E)
# Repetir el procedimiento descrito en el punto C, para el caso de un agente con comportamiento totalmente aleatorio.  En cada periodo de tiempo,
#  el agente toma una acción al azar.


import numpy as np
from random import randint, random
from abc import ABC, abstractmethod
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt

from env import Environment
from simpleAgent import SimpleAgent
from megaRandomAgent import RandAgent

@dataclass
class ExperimentResult:
    agent_name: str
    environment_size: str
    dirt_rate: float
    repetitions: int
    average_performance: float

results = []

# Configuración de experimentos
agent_names = ['RandAgent', 'SimpleAgent']
environment_sizes = [2, 4, 8, 16, 32, 64, 128]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
repetitions = 10

# Realizar los experimentos
for agent_name in agent_names:
    for size in environment_sizes:
        for dirt_rate in dirt_rates:
            total_performance = 0
            for _ in range(repetitions):
                env = Environment(size, size, dirt_rate)
                agent = globals()[agent_name](env)
                agent.start()
                total_performance += agent.getPerformance()
            average_performance = total_performance / repetitions
            result = ExperimentResult(agent_name, f'{size}x{size}', dirt_rate, repetitions, average_performance)
            results.append(result)

# Crear un DataFrame a partir de los resultados
df = pd.DataFrame(results)

# Crear una tabla pivot para visualizar los resultados
pivot_table = df.pivot_table(index=['agent_name', 'environment_size'], columns='dirt_rate', values='average_performance', aggfunc=np.mean)

# Mostrar la tabla pivot
print(pivot_table)

# Crear gráficos para visualizar los resultados
for agent_name in agent_names:
    agent_data = df[df['agent_name'] == agent_name]
    for size in environment_sizes:
        size_data = agent_data[agent_data['environment_size'] == f'{size}x{size}']
        plt.figure(figsize=(10, 6))
        plt.plot(size_data['dirt_rate'], size_data['average_performance'], marker='o')
        plt.title(f'{agent_name} - {size}x{size}')
        plt.xlabel('Dirt Rate')
        plt.ylabel('Average Performance')
        plt.grid()
        plt.show()
