# ## Ejercicio G)
# Desarrollar un agente reflexivo que funcione para el entorno FrozenLake de la biblioteca Gymnasium. (OPCIONAL)

# **Descripción:**

# FrozenLake  es un entorno de cuadrícula donde un agente debe navegar desde un punto de inicio hasta una meta, evitando caer en los agujeros del hielo. 

# La medida de rendimiento recompensa al agente con un punto por cada casilla que cruza exitosamente sin caer en un agujero durante un período de tiempo específico, a lo largo de una vida de 1000 acciones.

# La dimensión de la cuadrícula se conoce de antemano, pero la distribución de los agujeros y la ubicación inicial del agente no se conocen (son aleatorios). Las casillas permanecen sólidas una vez cruzadas, y el objetivo del agente es alcanzar la meta sin caer en un agujero.
# Las acciones *"Left", "Right", "Up" y "Down"* mueven al agente en esas direcciones, excepto cuando dicho movimiento sacaría al agente de la cuadrícula o lo llevaría a un agujero.

# Las acciones permitidas son:
# - 0: Move left
# - 1: Move down
# - 2: Move right
# - 3: Move up

# El agente percibe su ubicación y si esa casilla contiene un agujero o es la meta.

# A continuación una porción de código que implementa un agente aleatorio en el entorno frozenLake. Se puede tomar como guía para implementar un agente reactivo que funcione sobre el mismo entorno.

# ------------------------------------------------------------------------------------------------------------------------------------------
# ## Ejercicio H)
# Evaluar el desempeño del agente agente reflexivo (medida de desempeño y unidades de tiempo consumidas) para: (OPCIONAL)

# 1. Entornos de : 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128
# 2. Porcentaje de agujeros en el ambiente: 0.1, 0,2 0,4, 0.8
# 3. Repetir 10 veces cada combinación.