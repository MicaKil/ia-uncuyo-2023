# Trabajo Práctico 3: Búsqueda no informada

**Estudiante:** Del Longo, Micaela

[**Link al TP:** https://docs.google.com/document/d/1xZF3YCyxGod-ceHELV0tk8tRhhCF83QYBzBGrV2ecKQ/edit](https://docs.google.com/document/d/1xZF3YCyxGod-ceHELV0tk8tRhhCF83QYBzBGrV2ecKQ/edit)

A partir de la lectura del CAP 3 de AIMA (3era edición) (en particular las secciones 3.1, 3.2, 3.3, 3.4.1, 3.4.2, 3.4.3 y 3.4.4). Completar los siguientes enunciados:

## Ejercicio A

Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

Considerar lo siguiente:

1. El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar. Se trata de un entorno completamente observable, determinista y estático.
2. Las acciones posibles del agente son: (arriba, abajo, izquierda, derecha)
3. El agente deberá ser capaz de resolver el problema planteado mediante los siguientes algoritmos de búsqueda no informada:
   - Búsqueda por Anchura
   - Búsqueda por Profundidad 
   - Búsqueda Por Profundidad limitada
   - Búsqueda Uniforme
4. Al finalizar el proceso de formulación se deberán imprimir por pantalla:
   - La matriz generada con los obstáculos (opcional)
   - La secuencia de estados completa para llegar desde el estado inicial al estado destino. (si es posible)

## Ejercicio B

Ejecutar un total de 30 veces cada algoritmo en un escenario aleatorio con una tasa de obstáculos del 8 por ciento, calcular la media y la desviación estándar de la cantidad de estados explorados para llegar al destino (si es que fue posible). Evaluar cada uno de los algoritmos sobre el mismo conjunto de datos generado.  Presentar los resultados en un gráfico de cajas y bigotes o boxplots.

## Ejercicio C

¿Cuál de los 3 algoritmos considera más adecuado para resolver el problema planteado en A)?. Justificar la respuesta.

## Forma de entrega:

Dentro del repositorio en github con el nombre de ia-uncuyo-2023 crear una carpeta con el nombre tp3-busquedas-no-informadas.

Colocar un archivo con el nombre tp3-reporte.md que contenga la respuesta a la pregunta B y C.

Dentro de dicha carpeta (tp3-busquedas-no-informadas) crear una nueva carpeta code para el proyecto desarrollado en python

Dentro tp3-busquedas-no-informadas crear un archivo de nombre no-informada-results.csv en formato csv (comma separated values) con los resultados de las 30 ejecuciones para cada uno de los algoritmos evaluados. El formato deberá ser el siguiente: algorithm_name, run_n, estate_n, solution_found