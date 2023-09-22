# A) Implementar un algoritmo de Hill Climbing (versión canónica) para resolver el problema de las n-reinas.
#
# El algoritmo deberá ser capaz de encontrar solamente una solución para tableros de diferentes tamaños.
# Una posible estructura para representar el tablero consiste en un arreglo de tamaño N, donde en cada posición hace
# referencia a una columna de tablero. Y cada valor hace referencia a una fila.
#
# Se define una función objetivo H(e) la cual contabiliza la cantidad de pares de reinas amenazadas para un tablero e.
#
# Se deberá definir una variable que establezca el número máximo de estados que podrán ser evaluados.
#
# El programa deberá devolver el tablero solución (únicamente la estructura que representa el tablero). Junto a la
# cantidad de estados que tuvo que recorrer el algoritmo para llegar a la solución. En caso de alcanzar el máximo de
# estados evaluados, devolver la mejor solución encontrada y el valor correspondiente de la función H.
#
# Replicar el punto 5 para los casos de las 4,8,10 reinas

# B)  Implementar el algoritmo Simulated Annealing para resolver el problema del punto A.
#
# C)  Implementar un algoritmo genético para resolver el problema del punto A.  Ademas de la implementación en código
# del mismo, se deberán incluir detalles respecto a
# 1. Definición de los individuos de la población
# 2. Estrategia de selección
# 3. Estrategia de reemplazo
# 4. Operadores.
