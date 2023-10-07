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
Utilizar el algoritmo AC-3 para demostrar que la arco-consistencia puede detectar la inconsistencia de la asignación 
parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición).

### Algoritmo AC-3:

```
function AC-3(csp) returns false if an inconsistency is found and true otherwise
    inputs: csp, a binary CSP with components (X, D, C)
    local variables: queue, a queue of arcs, initially all the arcs in csp
    while queue is not empty do
        (Xi, Xj) ← REMOVE-FIRST(queue)
        if REVISE(csp, Xi, Xj ) then
            if size of Di = 0 then return false
            for each Xk in Xi.NEIGHBORS - {Xj} do
                add (Xk, Xi) to queue
    return true
```
```
function REVISE(csp, Xi, Xj ) returns true iff we revise the domain of Xi
    revised ← false
    for each x in Di do
        if no value y in Dj allows (x, y) to satisfy the constraint between Xi and Xj then
            delete x from Di
            revised ← true
    return revised
```

### Formulación CSP del problema con {WA=red, V=blue}:

- X = {WA, NT, Q, NSW, V, SA, T}


- D(WA) = {red}
- D(NT) = {red, green, blue}
- D(Q) = {red, green, blue}
- D(NSW) = {red, green, blue}
- D(V) = {blue}
- D(SA) = {red, green, blue}
- D(T) = {red, green, blue}


- C = {SA != WA, SA != NT, SA != Q, SA != NSW, SA != V, WA != NT, NT != Q, Q != NSW, NSW != V}

### Aplicación del algoritmo AC-3:

**Arcos:**
- SA → WA
- WA → SA
- SA → NT
- NT → SA
- SA → Q
- Q → SA
- SA → NSW
- NSW → SA
- SA → V
- V → SA
- WA → NT
- NT → WA
- NT → Q
- Q → NT
- Q → NSW
- NSW → Q
- NSW → V
- V → NSW

*Nota:* Los arcos se corresponden con las restricciones C del problema.

***Iteración 1:***
- Se toma el arco SA → WA
- El dominio de SA se reduce a D(SA) = {green, blue}
- Los arcos WA → SA, NT → SA, Q → SA, NSW → SA, V → SA ya se encuentra en la cola, por lo que esta no se modifica.
- **Dominios:** 
  - D(WA) = {red}
  - D(NT) = {red, green, blue}
  - D(Q) = {red, green, blue}
  - D(NSW) = {red, green, blue}
  - D(V) = {blue}
  - D(SA) = {green, blue}
  - D(T) = {red, green, blue}
- **Arcos en la cola:** WA → SA, SA → NT, NT → SA, SA → Q, Q → SA, SA → NSW, NSW → SA,
SA → V, V → SA, WA → NT, NT → WA, NT → Q, Q → NT, Q → NSW, NSW → Q, NSW → V, V → NSW

***Iteración 2:***
- Se toma el arco WA → SA
- El dominio de WA se mantiene igual.
- **Arcos en la cola:** SA → NT, NT → SA, SA → Q, Q → SA, SA → NSW, NSW → SA, SA → V,
V → SA, WA → NT, NT → WA, NT → Q, Q → NT, Q → NSW, NSW → Q, NSW → V, V → NSW

***Iteraciones 3 a 8:***
- Los dominios se mantienen igual.
- **Arcos en la cola:** SA → V, V → SA, WA → NT, NT → WA, NT → Q, Q → NT, Q → NSW,
NSW → Q, NSW → V, V → NSW

***Iteración 9:***
- Se toma el arco SA → V
- El dominio de SA se reduce a D(SA) = {green}.
- Se agregan los arcos: WA → SA, NT → SA, Q → SA, NSW → SA
- **Dominios:** 
  - D(WA) = {red}
  - D(NT) = {red, green, blue}
  - D(Q) = {red, green, blue}
  - D(NSW) = {red, green, blue}
  - D(V) = {blue}
  - D(SA) = {green}
  - D(T) = {red, green, blue}
- **Arcos en la cola:** V → SA, WA → NT, NT → WA, NT → Q, Q → NT, Q → NSW, NSW → Q,
NSW → V, V → NSW, WA → SA, NT → SA, Q → SA, NSW → SA

***Iteración 10:***
- Se toma el arco V → SA
- El dominio de V se mantiene igual.
- **Arcos en la cola:** WA → NT, NT → WA, NT → Q, Q → NT, Q → NSW, NSW → Q, NSW → V,
V → NSW, WA → SA, NT → SA, Q → SA, NSW → SA

***Iteración 11:***
- Se toma el arco WA → NT
- El dominio de WA se mantiene igual.
- **Arcos en la cola:** NT → WA, NT → Q, Q → NT, Q → NSW, NSW → Q, NSW → V, V → NSW,
WA → SA, NT → SA, Q → SA, NSW → SA

***Iteración 12:***
- Se toma el arco NT → WA
- El dominio de NT se reduce a D(NT) = {green, blue}.
- Se agregan los arcos: SA → NT, WA → NT
- **Dominios:** 
  - D(WA) = {red}
  - D(NT) = {green, blue}
  - D(Q) = {red, green, blue}
  - D(NSW) = {red, green, blue}
  - D(V) = {blue}
  - D(SA) = {green}
  - D(T) = {red, green, blue}
- **Arcos en la cola:** NT → Q, Q → NT, Q → NSW, NSW → Q, NSW → V, V → NSW, WA → SA,
NT → SA, Q → SA, NSW → SA, SA → NT, WA → NT

***Iteraciones 13 a 16:***
- Los dominios se mantienen igual.
- **Arcos en la cola:** NSW → V, V → NSW, WA → SA, NT → SA, Q → SA, NSW → SA, SA → NT, WA → NT

***Iteración 17:***
- Se toma el arco NSW → V
- El dominio de NSW se reduce a D(NSW) = {red, green}.
- Se agregan los arcos: SA → NSW, Q → NSW
- **Dominios:** 
  - D(WA) = {red}
  - D(NT) = {green, blue}
  - D(Q) = {red, green, blue}
  - D(NSW) = {red, green}
  - D(V) = {blue}
  - D(SA) = {green}
  - D(T) = {red, green, blue}
- **Arcos en la cola:** V → NSW, WA → SA, NT → SA, Q → SA, NSW → SA, SA → NT, WA → NT, SA → NSW, Q → NSW

***Iteraciones 18 a 19:***
- Los dominios se mantienen igual.
- **Arcos en la cola:** NT → SA, Q → SA, NSW → SA, SA → NT, WA → NT, SA → NSW, Q → NSW

***Iteración 20:***
- Se toma el arco NT → SA
- El dominio de NT se reduce a D(NT) = {blue}.
- Se agrega el arco: Q → NT
- **Dominios:** 
  - D(WA) = {red}
  - D(NT) = {blue}
  - D(Q) = {red, green, blue}
  - D(NSW) = {red, green}
  - D(V) = {blue}
  - D(SA) = {green}
  - D(T) = {red, green, blue}
- **Arcos en la cola:** Q → SA, NSW → SA, SA → NT, WA → NT, SA → NSW, Q → NSW, Q → NT

***Iteración 21:***
- Se toma el arco Q → SA
- El dominio de Q se reduce a D(Q) = {red, blue}.
- Se agregan los arcos: SA → Q, NT → Q, NSW → Q
- **Dominios:** 
  - D(WA) = {red}
  - D(NT) = {blue}
  - D(Q) = {red, blue}
  - D(NSW) = {red, green}
  - D(V) = {blue}
  - D(SA) = {green}
  - D(T) = {red, green, blue}
- **Arcos en la cola:** NSW → SA, SA → NT, WA → NT, SA → NSW, Q → NSW, Q → NT, SA → Q, NT → Q, NSW → Q

***Iteración 22:***
- Se toma el arco NSW → SA
- El dominio de NSW se reduce a D(NSW) = {red}.
- Se agrega el arco: V → NSW
- **Dominios:** 
  - D(WA) = {red}
  - D(NT) = {blue}
  - D(Q) = {red, blue}
  - D(NSW) = {red}
  - D(V) = {blue}
  - D(SA) = {green}
  - D(T) = {red, green, blue}
- **Arcos en la cola:** SA → NT, WA → NT, SA → NSW, Q → NSW, Q → NT, SA → Q, NT → Q, NSW → Q, V → NSW

***Iteraciones 23 a 25:***
- Los dominios se mantienen igual.
- **Arcos en la cola:** Q → NSW, Q → NT, SA → Q, NT → Q, NSW → Q, V → NSW

***Iteración 26:***
- Se toma el arco Q → NSW
- El dominio de Q se reduce a D(Q) = {blue}.
- Los arcos SA → Q, NT → Q, NSW → Q ya se encuentran en la cola, por lo que esta no se modifica.
- **Dominios:** 
  - D(WA) = {red}
  - D(NT) = {blue}
  - D(Q) = {blue}
  - D(NSW) = {red}
  - D(V) = {blue}
  - D(SA) = {green}
  - D(T) = {red, green, blue}
- **Arcos en la cola:** Q → NT, SA → Q, NT → Q, NSW → Q, V → NSW

***Iteración 27:***
- Se toma el arco Q → NT
- El dominio de Q se reduce a D(Q) = {}.
- return false

El algoritmo AC-3 devuelve **false**, por lo que la asignación parcial {WA=red, V=blue} es inconsistente.

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
ello, demostrar incisos A y B.

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
