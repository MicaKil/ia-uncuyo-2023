# Trabajo Práctico 4: Búsqueda informada
**Estudiante:** Del Longo, Micaela

[**Link al TP:** https://docs.google.com/document/d/1tiR1-6OG6KcwdsWdJNemLShTyV38S1jho7ObcrUI2bw/edit#heading=h.lqya3ojnc5h1](https://docs.google.com/document/d/1tiR1-6OG6KcwdsWdJNemLShTyV38S1jho7ObcrUI2bw/edit#heading=h.lqya3ojnc5h1)

## Ejercicio B
Ejecutar un total de 30 veces el algoritmo A* en un escenario aleatorio con una tasa de obstáculos del 8 por ciento, 
calcular la media y la desviación estándar de la cantidad de estados explorados para llegar al destino (si es que fue 
posible). Evaluar cada uno de los algoritmos sobre el mismo conjunto de datos generado. Presentar los resultados en un 
gráfico de cajas y bigotes o boxplot. Incluya también los resultados obtenidos en el punto B del TP3 sobre búsquedas no 
informadas.

### Representación Tabular de los Resultados
| Agente           | Estados explorados (promedio) | Desviación estándar | Costo de la solución (promedio) | Desviación estándar | Porcentaje de éxito |
|------------------|-------------------------------|---------------------|---------------------------------|---------------------|---------------------|
| BFSAgent         | 5133.37                       | 2753.95             | 75                              | 35.52               | 100.00%             |
| AStarAgent       | 133.10                        | 107.47              | 75                              | 35.52               | 100.00%             |
| DLSAgent         | 2759.10                       | 1448.07             | 213.44                          | 60.37               | 60.00%              |
| UniformCostAgent | 5209.87                       | 2747.22             | 75                              | 35.52               | 100.00%             |
| DFSAgent         | 2856.23                       | 2361.80             | 873.87                          | 524.74              | 100.00%             |

Los resultados sin redondear se encuentran en la sección [Raw Data](#raw-data) y los 30 entornos generados se 
encuentran en la sección [Entornos Generados](#entornos-generados).

### Gráfico de Cajas y Bigotes para los Estados Explorados
![Boxplot de los estados explorados](pics/states_explored.png)

### Gráfico de Cajas y Bigotes para el Costo de la Solución (path_cost)
![Boxplot del costo de la solución](pics/path_cost.png)

## Raw Data

Agente: **BFSAgent**
- Estados explorados en promedio: 5133.366666666667
- Desviación estándar: 2753.9521003939717
- Costo de la solución en promedio: 75
- Desviación estándar: 35.52269794040871

Agente: **AStarAgent**
- Estados explorados en promedio: 133.1
- Desviación estándar: 107.46750912364806
- Costo de la solución en promedio: 75
- Desviación estándar: 35.52269794040871

Agente: **DLSAgent**
- Estados explorados en promedio: 2759.1
- Desviación estándar: 1448.06763868505
- Costo de la solución en promedio: 213.44444444444446
- Desviación estándar: 60.36674408024399

Agente: **UniformCostAgent**
- Estados explorados en promedio: 5209.866666666667
- Desviación estándar: 2747.218075439769
- Costo de la solución en promedio: 75
- Desviación estándar: 35.52269794040871

Agente: **DFSAgent**
- Estados explorados en promedio: 2856.233333333333
- Desviación estándar: 2361.801455688423
- Costo de la solución en promedio: 873.8666666666667
- Desviación estándar: 524.7401809193426

### Porcentaje de entornos resueltos por agente:
- Porcentaje de veces que **BFSAgent** encontró la solución: 100.00%
- Porcentaje de veces que **AStarAgent** encontró la solución: 100.00%
- Porcentaje de veces que **DLSAgent** encontró la solución: 60.00%
- Porcentaje de veces que **UniformCostAgent** encontró la solución: 100.00%
- Porcentaje de veces que **DFSAgent** encontró la solución: 100.00%

## Entornos Generados

### Entorno 1
<div align="center">
  <img src="pics/entorno_1.png" alt="Entorno 1">
</div>

### Entorno 2
<div align="center">
  <img src="pics/entorno_2.png" alt="Entorno 2">
</div>

### Entorno 3
<div align="center">
  <img src="pics/entorno_3.png" alt="Entorno 3">
</div>

### Entorno 4
<div align="center">
  <img src="pics/entorno_4.png" alt="Entorno 4">
</div>

### Entorno 5
<div align="center">
  <img src="pics/entorno_5.png" alt="Entorno 5">
</div>

### Entorno 6
<div align="center">
  <img src="pics/entorno_6.png" alt="Entorno 6">
</div>

### Entorno 7
<div align="center">
  <img src="pics/entorno_7.png" alt="Entorno 7">
</div>

### Entorno 8
<div align="center">
  <img src="pics/entorno_8.png" alt="Entorno 8">
</div>

### Entorno 9
<div align="center">
  <img src="pics/entorno_9.png" alt="Entorno 9">
</div>

### Entorno 10
<div align="center">
  <img src="pics/entorno_10.png" alt="Entorno 10">
</div>

### Entorno 11
<div align="center">
  <img src="pics/entorno_11.png" alt="Entorno 11">
</div>

### Entorno 12
<div align="center">
  <img src="pics/entorno_12.png" alt="Entorno 12">
</div>

### Entorno 13
<div align="center">
  <img src="pics/entorno_13.png" alt="Entorno 13">
</div>

### Entorno 14
<div align="center">
  <img src="pics/entorno_14.png" alt="Entorno 14">
</div>

### Entorno 15
<div align="center">
  <img src="pics/entorno_15.png" alt="Entorno 15">
</div>

### Entorno 16
<div align="center">
  <img src="pics/entorno_16.png" alt="Entorno 16">
</div>

### Entorno 17
<div align="center">
  <img src="pics/entorno_17.png" alt="Entorno 17">
</div>

### Entorno 18
<div align="center">
  <img src="pics/entorno_18.png" alt="Entorno 18">
</div>

### Entorno 19
<div align="center">
  <img src="pics/entorno_19.png" alt="Entorno 19">
</div>

### Entorno 20
<div align="center">
  <img src="pics/entorno_20.png" alt="Entorno 20">
</div>

### Entorno 21
<div align="center">
  <img src="pics/entorno_21.png" alt="Entorno 21">
</div>

### Entorno 22
<div align="center">
  <img src="pics/entorno_22.png" alt="Entorno 22">
</div>

### Entorno 23
<div align="center">
  <img src="pics/entorno_23.png" alt="Entorno 23">
</div>

### Entorno 24
<div align="center">
  <img src="pics/entorno_24.png" alt="Entorno 24">
</div>

### Entorno 25
<div align="center">
  <img src="pics/entorno_25.png" alt="Entorno 25">
</div>

### Entorno 26
<div align="center">
  <img src="pics/entorno_26.png" alt="Entorno 26">
</div>

### Entorno 27
<div align="center">
  <img src="pics/entorno_27.png" alt="Entorno 27">
</div>

### Entorno 28
<div align="center">
  <img src="pics/entorno_28.png" alt="Entorno 28">
</div>

### Entorno 29
<div align="center">
  <img src="pics/entorno_29.png" alt="Entorno 29">
</div>

### Entorno 30
<div align="center">
  <img src="pics/entorno_30.png" alt="Entorno 30">
</div>