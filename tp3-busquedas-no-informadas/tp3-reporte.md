# Trabajo Práctico 3: Búsqueda no informada

**Estudiante:** Del Longo, Micaela

[**Link al TP:** https://docs.google.com/document/d/1xZF3YCyxGod-ceHELV0tk8tRhhCF83QYBzBGrV2ecKQ/edit](https://docs.google.com/document/d/1xZF3YCyxGod-ceHELV0tk8tRhhCF83QYBzBGrV2ecKQ/edit)

## Ejercicio B

Ejecutar un total de 30 veces cada algoritmo en un escenario aleatorio con una tasa de obstáculos del 8 por ciento, calcular la media y la desviación estándar de la cantidad de estados explorados para llegar al destino (si es que fue posible). Evaluar cada uno de los algoritmos sobre el mismo conjunto de datos generado.  Presentar los resultados en un gráfico de cajas y bigotes o boxplots.
### Representación Tabular de los Resultados
También me pareció importante realizar los mismos cálculos para el costo de la solución encontrada por cada agente. 

| Agente           | Estados Explorados en Promedio | Desviación Estándar | Costo de la Solución en Promedio | Desviación Estándar |
|------------------|--------------------------------|---------------------|----------------------------------|---------------------|
| BFSAgent         | 3783.73                        | 2906.52             | 62.67                            | 41.39               |
| DFSAgent         | 3092.83                        | 2605.69             | 743.73                           | 521.57              |
| DLSAgent         | 2409.4                         | 1504.99             | 185.63                           | 73.84               |
| UniformCostAgent | 3854.03                        | 2893.52             | 62.67                            | 41.39               |

Los resultados sin redondear se encuentran en la sección [Raw Data](#raw-data) y los 30 entornos generados se encuentran en la sección [Entornos Generados](#entornos-generados).

### Gráfico de Cajas y Bigotes para los Estados Explorados
![Boxplot de los estados explorados](pics/states_explored.png)

### Gráfico de Cajas y Bigotes para el Costo de la Solución (path_cost)
![Boxplot del costo de la solución](pics/path_cost.png)

### Porcentaje de Entornos Resueltos
- Porcentaje de veces que **BFSAgent** encontró la solución: 100.00%
- Porcentaje de veces que **DLSAgent** encontró la solución: 60.00%
- Porcentaje de veces que **UniformCostAgent** encontró la solución: 100.00%
- Porcentaje de veces que **DFSAgent** encontró la solución: 100.00%

## Ejercicio C

¿Cuál de los 3 algoritmos considera más adecuado para resolver el problema planteado en A)?. Justificar la respuesta.

Teniendo en cuenta mi implementación y los resultados anteriores, el algoritmo que considero más adecuado es el de **búsqueda por anchura**. Esto se debe a que, en este caso, el *costo de las acciones es el mismo para todas*. BFS es completo, lo que garantiza encontrar una solución si existe, y encuentra la solución óptima en términos de longitud del camino, ya que explora todos los nodos en el mismo nivel antes de avanzar a niveles más profundos.

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

## Raw Data
**Agente: BFSAgent**
- **Estados explorados en promedio:** 3783.733333333333
  - **Desviación estándar:** 2906.5214537174056
- **Costo de la solución en promedio:** 62.666666666666664
  - **Desviación estándar:** 41.3924308700677

**Agente: DFSAgent**
- **Estados explorados en promedio:** 3092.8333333333335
  - **Desviación estándar:** 2605.6938990223503
- **Costo de la solución en promedio:** 743.7333333333333
  - **Desviación estándar:** 521.570634177943

**Agente: DLSAgent**
- **Estados explorados en promedio:** 2409.4
  - **Desviación estándar:** 1504.9904708141441
- **Costo de la solución en promedio:** 185.6315789473684
  - **Desviación estándar:** 73.83631335319122

**Agente: UniformCostAgent**
- **Estados explorados en promedio:** 3854.0333333333333
  - **Desviación estándar:** 2893.5199120809925
- **Costo de la solución en promedio:** 62.666666666666664
  - **Desviación estándar:** 41.3924308700677