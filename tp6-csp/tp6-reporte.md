# Trabajo Práctico 6: Constraint Satisfaction Problem
**Estudiante:** Del Longo, Micaela (11653)

[**Link al TP:** https://docs.google.com/document/d/17lgND6cZN5QtgTToGeFRQj6iZ2xopm3pPOJYp92DPHU/edit](https://docs.google.com/document/d/17lgND6cZN5QtgTToGeFRQj6iZ2xopm3pPOJYp92DPHU/edit)

## Ejercicio 1
Describir en detalle una formulación CSP para el Sudoku.

Componentes de CSP según AIMA (p. 202-203, 3ra edición):

> A constraint satisfaction problem consists of three components, X, D, and C:
> - X is a set of variables, {X1, . . . ,Xn}.
> - D is a set of domains, {D1, . . . ,Dn}, one for each variable.
> - C is a set of constraints that specify allowable combinations of values.
>
> Each domain Di consists of a set of allowable values, {v1, . . . , vk} for variable Xi. Each
constraint Ci consists of a pair <scope, rel>, where scope is a tuple of variables that participate
in the constraint and rel is a relation that defines the values that those variables can take on. A
relation can be represented as an explicit list of all tuples of values that satisfy the constraint,
or as an abstract relation that supports two operations: testing if a tuple is a member of the
relation and enumerating the members of the relation. For example, if X1 and X2 both have
the domain {A,B}, then the constraint saying the two variables must have different values
can be written as <(X1,X2), [(A,B), (B,A)]> or as <(X1,X2),X1 != X2>.
> 
> To solve a CSP, we need to define a state space and the notion of a solution. Each
state in a CSP is defined by an assignment of values ASSIGNMENT to some or all of the variables, {Xi =
vi,Xj = vj , . . .}. An assignment that does not violate any constraints is called a consistent
or legal assignment. A complete assignment is one in which every variable is assigned, and
a solution to a CSP is a consistent, complete assignment. A partial assignment is one that
assigns values to only some of the variables.

### Solución:

Para el caso del Sudoku, una posible **formulación CSP** es la siguiente:

- X = {X11, X12, ..., X19, X21, ..., X99}
- D = {D11, D12, ..., D19, D21, ..., D99}
- C = {C1, C2, ..., C36}

Donde cada **variable** Xi representa la celda de la fila i y columna j del tablero. El **dominio de cada variable** Xi 
es el conjunto de valores enteros entre 1 y 9. Las **restricciones** C1 a C9 son las que se aplican a cada fila del 
tablero. Las restricciones C10 a C18 son las que se aplican a cada columna del tablero. Las restricciones C19 a C27 son 
las que se aplican a cada región (cuadrado de 3x3) del tablero. Las restricciones C28 a C36 son las que se aplican a 
cada celda del tablero.

Es decir, las restricciones C1 a C9, C10 a C18 y C19 a C27 son las que aseguran que cada fila, columna y región del tablero
respectivamente contengan los números del 1 al 9 sin repetir. Las restricciones C28 a C36 son las que aseguran que cada
celda del tablero contenga un número del 1 al 9.

- Las **restricciones C1 a C9** son del tipo ``<(X11, X12, ..., X19), X11 != X12 != ... != X19>``. 
- Las **restricciones C10 a C18** son del tipo ``<(X11, X21, ..., X91), X11 != X21 != ... != X91>``.
- Las **restricciones C19 a C27** son del tipo ``<(X11, X12, X13, X21, X22, X23, X31, X32, X33), X11 != X12 != X13 != X21 != X22 != X23 != X31 != X32 != X33>``.
- Las **restricciones C28 a C36** son del tipo ``<(X11), X11 = 1 || X11 = 2 || ... || X11 = 9>``.

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

### Inciso A
Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia 
(siendo n número total de variables)

### Inciso B
Argumentar por qué lo demostrado en [A](#inciso-A) es suficiente.

## Ejercicio 6
1. Implementar una solución al problema de las n-reinas utilizando una formulación CSP.
2. Implementar una solución utilizando backtracking.
3. Implementar una solución utilizando encadenamiento hacia adelante. 
4. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas. 
5. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8, 
10, 12 y 15 reinas. 
6. Realizar un gráfico de cajas para los puntos c y d.
