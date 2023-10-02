# Trabajo Práctico 6: Constraint Satisfaction Problem
**Estudiante:** Del Longo, Micaela (11653)

[**Link al TP:** https://docs.google.com/document/d/17lgND6cZN5QtgTToGeFRQj6iZ2xopm3pPOJYp92DPHU/edit](https://docs.google.com/document/d/17lgND6cZN5QtgTToGeFRQj6iZ2xopm3pPOJYp92DPHU/edit)

## Ejercicio 1
Describir en detalle una formulación CSP para el Sudoku.

## Ejercicio 2
Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación 
parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).

## Ejercicio 3
Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de
restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

## Ejercicio 4
AC-3 coloca de nuevo en la cola todo arco (Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si 
cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por  cada arco (Xk, Xi) se puede llevar 
la cuenta del número de valores restantes de Xi que sean consistentes con cada valor de Xk. 

Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo
total O(n<sup>2</sup>d<sup>2</sup>)

## Ejercicio 5
Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para 
ello, demostrar:

### Inciso a
Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia 
(siendo n número total de variables)

### Inciso b
Argumentar por qué lo demostrado en [a](#inciso-a) es suficiente.

## Ejercicio 6
1. Implementar una solución al problema de las n-reinas utilizando una formulación CSP.
2. Implementar una solución utilizando backtracking.
3. Implementar una solución utilizando encadenamiento hacia adelante. 
4. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas. 
5. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8, 
10, 12 y 15 reinas. 
6. Realizar un gráfico de cajas para los puntos c y d.
