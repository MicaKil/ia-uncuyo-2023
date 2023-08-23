# Trabajo Práctico 2: Agentes Racionales 

**Estudiante:** Del Longo, Micaela

[**Link al TP:** https://docs.google.com/document/d/1IfD2rfzS-OBa9bLG6XfHMr4gJYbrktLxAahTQBz-i0E/edit#heading=h.k95nk1o7cede](https://docs.google.com/document/d/1IfD2rfzS-OBa9bLG6XfHMr4gJYbrktLxAahTQBz-i0E/edit#heading=h.k95nk1o7cede)

## Ejercicio A)

Para cada una de las siguientes actividades, describa en PEAS el entorno de la tarea y caracterizarlo en términos de las propiedades enumeradas.

### Jugar al CS (o cualquier otro 3D Shooter).
- **Performance:**  Puntaje, número de enemigos derrotados, salud del jugador
- **Environment:** Ambiente simulado en 3D, otros jugadores,  obstáculos, enemigos y armas
- **Actuators:** Mouse, teclado, joystick
- **Sensors:** Visuales, sonido, información posicional
- **Properties:** Parcialmente observable, uni-agente, estocástico, secuencial, dinámico, discreto. 
### Explorar los océanos.
- **Performance:** Profundidad explorada, especies descubiertas, muestras recolectadas.
- **Environment:** Océano, vida marina diversa, terreno submarino y condiciones variables.
- **Actuators:** Controles de vehículos sumergibles, brazos robóticos
- **Sensors:** Visuales, sonar, sensores de temperatura 
- **Properties:** Parcialmente observable, uni-agente, estocástico, secuencial, dinámico, continuo. 
### Comprar y vender tokens crypto.
- **Performance:** Ganancia, valor de la cartera, operaciones exitosas
- **Environment:** Plataforma de intercambio de criptomonedas en línea con datos de mercado y otros traders
- **Actuators:** Colocar órdenes de compra/venta, gestionar la cartera
- **Sensors:** Datos de mercado, información de la cuenta
- **Properties:** Totalmente observable, multi-agente, estocástico, secuencial, dinámico, discreto. 
### Practicar el tenis contra una pared.
- **Performance:** Número de golpes exitosos, precisión en los golpes
- **Environment:** Pared para hacer rebotar la pelota
- **Actuators:** Raqueta de tenis, movimientos corporales
- **Sensors:** Visuales, sonido
- **Properties:** Totalmente observable, uni-agente, determinista, episódico, dinámico, continuo. 
### Realizar un salto de altura.
- **Performance:** Altura superada, técnica, saltos exitosos
- **Environment:** Pista de atletismo con equipamiento de salto de altura
- **Actuators:** Movimientos corporales del corredor, técnica de despegue
- **Sensors:** Altura de la barra, ángulo del salto, posición del atleta
- **Properties:** Totalmente observable, uni-agente, estocástico, episódico, estático, continuo.
### Pujar por un artículo en una subasta.
- **Performance:** Oferta ganadora, relación calidad-precio
- **Environment:** Plataforma de subastas con varios postores y un subastador
- **Actuators:** Colocar ofertas, retirarse de la subasta
- **Sensors:** Oferta actual, tiempo restante, acciones de otros postores
- **Properties:** Parcialmente observable, multi-agente, estocástico, episódico, dinámico, continuo.

## Ejercicio B)
Implementar un simulador que determine la medida de rendimiento para el entorno del mundo de la aspiradora según las siguientes especificaciones:

1. La medida de rendimiento premia con un punto al agente por cada recuadro que limpia (aspira) en un período de tiempo concreto, a lo largo de una «vida» de 1000 acciones. 
2. La «dimensión» de la grilla se conoce a priori pero la distribución de la suciedad y la localización inicial del agente no se conocen (aleatorio). Las cuadrículas se mantienen limpias y aspirando se limpia la cuadrícula en que se encuentra el agente
3. Las acciones Izquierda, Derecha, Arriba, Abajo mueven al agente en dichas direcciones, excepto en el caso en que lo pueda llevar fuera de la grilla.
4. Las acciones permitidas son:
   1. Arriba
   2. Abajo
   3. Izquierda
   4. Derecha
   5. Limpiar (aspirar)
   6. NoHacerNada
5. El agente percibe su locación y si esta contiene suciedad

**Posible** interfaz a utilizar:
```
class Environment:
	def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate)		
    def accept_action(self,action):
    def is_dirty(self):
	def get_performance(self): 
	def print_environment(self): 
```
## Ejercicio C)
Implementar un agente reflexivo simple para el entorno de la aspiradora del ejercicio anterior.

Posible interfaz para el Agente:
```
class Agent:           
    def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
    def up(self):
    def down(self):      
    def left(self):
    def right(self):
    def suck(self): # Limpia
    def idle(self): # no hace nada
    def perspective(self,env): #sensa el entorno
    def think(self): # implementa las acciones a seguir por el agente
```
## Ejercicio G)
Desarrollar un agente reflexivo que funcione para el entorno FrozenLake de la biblioteca Gymnasium. (OPCIONAL)

**Descripción:**

FrozenLake  es un entorno de cuadrícula donde un agente debe navegar desde un punto de inicio hasta una meta, evitando caer en los agujeros del hielo. 

La medida de rendimiento recompensa al agente con un punto por cada casilla que cruza exitosamente sin caer en un agujero durante un período de tiempo específico, a lo largo de una vida de 1000 acciones.

La dimensión de la cuadrícula se conoce de antemano, pero la distribución de los agujeros y la ubicación inicial del agente no se conocen (son aleatorios). Las casillas permanecen sólidas una vez cruzadas, y el objetivo del agente es alcanzar la meta sin caer en un agujero.
Las acciones *"Left", "Right", "Up" y "Down"* mueven al agente en esas direcciones, excepto cuando dicho movimiento sacaría al agente de la cuadrícula o lo llevaría a un agujero.

Las acciones permitidas son:
- 0: Move left
- 1: Move down
- 2: Move right
- 3: Move up

El agente percibe su ubicación y si esa casilla contiene un agujero o es la meta.

A continuación una porción de código que implementa un agente aleatorio en el entorno frozenLake. Se puede tomar como guía para implementar un agente reactivo que funcione sobre el mismo entorno.

## Ejercicio H)
Evaluar el desempeño del agente agente reflexivo (medida de desempeño y unidades de tiempo consumidas) para: (OPCIONAL)

1. Entornos de : 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128
2. Porcentaje de agujeros en el ambiente: 0.1, 0,2 0,4, 0.8
3. Repetir 10 veces cada combinación.