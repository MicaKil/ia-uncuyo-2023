# Trabajo Práctico 6: Introducción a Machine Learning

**Estudiante:** Del Longo, Micaela (11653)

[**Link al TP:** https://docs.google.com/document/d/1zj64IVuUn1DiVfW6bSds88U-69r_E4uJgOAj9T6m8EQ/edit#heading=h.er2uz274b9q7](https://docs.google.com/document/d/1zj64IVuUn1DiVfW6bSds88U-69r_E4uJgOAj9T6m8EQ/edit#heading=h.er2uz274b9q7)

**Statistical Learning** es otro nombre con el que se hace referencia a Machine Learning.

Proveer las respuestas a los puntos 1,2,5,6,7 de la sección 2.4 (página 52 del ISLRv2).

## Pregunta 1

_For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical
learning method to be better or worse than an inflexible method. Justify your answer._

_(a) The sample size n is extremely large, and the number of predictors p is small._

Un método **flexible sería mejor** que un método inflexible, ya que puede capturar la complejidad de la verdadera relación
entre los predictores y la respuesta sin sufrir de overfitting, debido al gran tamaño de la muestra.

_(b) The number of predictors p is extremely large, and the number of observations n is small._

Un método **flexible sería peor** que un método inflexible, ya que tendría un alto riesgo de overfitting, debido al pequeño 
número de observaciones en relación con el número de predictores. Un método inflexible evitaría el problema de la alta
varianza.

_(c) The relationship between the predictors and response is highly non-linear._

Un método **flexible sería mejor** que un método inflexible, ya que podría adaptarse mejor a la forma no lineal de la 
relación entre los predictores y la respuesta. Un método inflexible sería demasiado rígido y tendría un alto sesgo.

_(d) The variance of the error terms, i.e. σ<sup>2</sup> = Var(ϵ), is extremely high._

Un método **flexible sería peor** que un método inflexible, ya que amplificaría el efecto del ruido en los datos y tendría 
una baja precisión en la predicción. Un método inflexible sería más robusto y tendría una menor varianza.

## Pregunta 2

Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in
inference or prediction. Finally, provide n and p.

_(a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, 
industry and the CEO salary. We are interested in understanding which factors affect CEO salary._

Es un problema de **regresión**. Estamos interesados en entender la relación entre el salario del CEO y las otras
variables, que son continuas. Por lo tanto, estamos interesados en **inferencia**. El tamaño de la muestra **n es 500** y
el número de predictores **p es 4**.

_(b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect 
data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or 
failure, price charged for the product, marketing budget, competition price, and ten other variables._

Es un problema de **clasificación**. Queremos predecir si el nuevo producto será un éxito o un fracaso, que es un resultado
binario. Por lo tanto, estamos más interesados en la **predicción**. El tamaño de la muestra **n es 20**, y hay 
**p = 13** predictores.

_(c) We are interested in predicting the ed % change in the USD/Euro exchange rate in relation to the weekly changes in
the world stock markets. Hence, we collect weekly data for all of 2012. For each week we record the % change in the 
USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market._

Es un problema de **regresión**. Estamos interesados en predecir el cambio porcentual en el tipo de cambio USD/Euro, que
es una variable continua. Por lo tanto, estamos más interesados en la **predicción**. El tamaño de la muestra **n es 52**
(52 semanas en un año), y hay **p = 4** predictores.

## Pregunta 5

_What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or 
classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When
might a less flexible approach be preferred?_

Un enfoque muy flexible para la regresión o la clasificación tiene la ventaja de poder adaptarse a formas complejas y no
lineales de los datos, lo que puede mejorar la precisión de la predicción. Sin embargo, también tiene la desventaja de 
tener un alto riesgo de overfitting, lo que significa que captura el ruido y las variaciones aleatorias de los datos, 
reduciendo la capacidad de generalización a nuevos datos.

Un enfoque muy flexible puede ser preferido cuando el tamaño de la muestra es grande en relación con el número de 
predictores, y cuando la relación entre los predictores y la respuesta es altamente no lineal y desconocida.

Un enfoque menos flexible puede ser preferido cuando el tamaño de la muestra es pequeño en relación con el número de 
predictores, y cuando la relación entre los predictores y la respuesta es lineal o se basa en un conocimiento previo.

## Pregunta 6

_Describe the differences between a parametric and a non-parametric statistical learning approach. What are the 
advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are
its disadvantages?_

Un enfoque **paramétrico** asume una forma fija y conocida para la función que relaciona los predictores y la respuesta. 
Por ejemplo, una línea o un polinomio. En cambio, un enfoque **no paramétrico** no hace ninguna suposición sobre la forma 
de la función y trata de aprenderla directamente de los datos.

**Ventajas** de un enfoque paramétrico:
- Es más simple y rápido de ajustar que un enfoque no paramétrico.
- Requiere menos datos para estimar los parámetros de la función.
- Permite hacer inferencia sobre los efectos de los predictores sobre la respuesta.

**Desventajas** de un enfoque paramétrico:
- Puede tener un alto sesgo si la forma asumida para la función no se ajusta a la realidad.
- Puede perder información relevante al ignorar aspectos de los datos que no se ajustan al modelo.

## Pregunta 7

_The table below provides a training data set containing six observations,
three predictors, and one qualitative response variable._

| Obs. | X1 | X2 | X3 | Y     |
|------|----|----|----|-------|
| 1    | 0  | 3  | 0  | Red   |
| 2    | 2  | 0  | 0  | Red   |
| 3    | 0  | 1  | 3  | Red   |
| 4    | 0  | 1  | 2  | Green |
| 5    | -1 | 0  | 1  | Green |
| 6    | 1  | 1  | 1  | Red   |

_Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors._

_(a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0._

_(b) What is our prediction with K = 1? Why?_

_(c) What is our prediction with K = 3? Why?_

_(d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for K to be
large or small? Why?_
