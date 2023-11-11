**Estudiante:** Del Longo, Micaela (11653)

# Parte C

## Ejercicio 1
_Implementar un algoritmo para construir un árbol de decisión de acuerdo al pseudocódigo provisto en AIMA._
   1. _El algoritmo solo deberá considerar variables discretas._ 
   2. _Se deberá comprobar su correcto funcionamiento de manera empírica sobre el dataset tennis.csv_ 

Los resultados sobre el dataset ``tennis.csv`` fueron los siguientes:

```
Test temp:
Parent: None
  temp = Hot
  temp = Mild
  temp = Cool
Test humidity:
Parent: temp = Hot
  humidity = High
  humidity = Normal
Test outlook:
Parent: temp = Mild
  outlook = Rain
  outlook = Sunny
  outlook = Overcast
Test humidity:
Parent: temp = Cool
  humidity = Normal
Test outlook:
Parent: humidity = High
  outlook = Sunny
  outlook = Overcast
Classify as Yes (Parent: humidity = Normal)
Test humidity:
Parent: outlook = Rain
  humidity = High
  humidity = Normal
Test humidity:
Parent: outlook = Sunny
  humidity = High
  humidity = Normal
Classify as Yes (Parent: outlook = Overcast)
Test outlook:
Parent: humidity = Normal
  outlook = Rain
  outlook = Overcast
  outlook = Sunny
Classify as No (Parent: outlook = Sunny)
Classify as Yes (Parent: outlook = Overcast)
Test wind:
Parent: humidity = High
  wind = Weak
  wind = Strong
Classify as Yes (Parent: humidity = Normal)
Classify as No (Parent: humidity = High)
Classify as Yes (Parent: humidity = Normal)
Test wind:
Parent: outlook = Rain
  wind = Weak
  wind = Strong
Classify as Yes (Parent: outlook = Overcast)
Classify as Yes (Parent: outlook = Sunny)
Classify as Yes (Parent: wind = Weak)
Classify as No (Parent: wind = Strong)
Classify as Yes (Parent: wind = Weak)
Classify as No (Parent: wind = Strong)
```

El diagrama del árbol de decisión obtenido es el siguiente:
<div align="center">
    <img src="pics/Tree.png"/>
</div>

## Ejercicio 2
_Investigar sobre las estrategias de los árboles de decisión para datos de tipo real y elaborar un breve resumen._
