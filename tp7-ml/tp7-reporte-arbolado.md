**Estudiante:** Del Longo, Micaela (11653)

# PARTE B

## Descripción del Proceso de Preprocesamiento
1. Se eliminaron las variables "ultima_modificacion", "area_seccion", "nombre_seccion" y "seccion".
2. Se crearon las variables "peligrosidad_especie", "peligrosidad_diametro" y "peligrosidad_altura".\
   Estas variables median la peligrosidad de cada árbol en función de su especie, diámetro y altura respectivamente.
3. Se reemplazaron las variables "especie", "diametro_tronco" y "altura" por las variables "peligrosidad_especie", 
   "peligrosidad_diametro" y "peligrosidad_altura" respectivamente.
4. No se normalizaron las variables, pero "peligrosidad_especie", "peligrosidad_diametro" y "peligrosidad_altura" toman
   valores entre 0 y 1.
5. Se balanceó el conjunto de datos utilizando la técnica de undersampling. Eliminando ejemplos de la clase mayoritaria
   hasta que la cantidad de ejemplos de cada clase sea la misma.

## Resultados Obtenidos sobre el Conjunto de Validación

No se utilizó un conjunto de validación.

## Resultados Obtenidos en Kaggle

- Con **Random Forest Classifier** se obtuvo un resultado de 0.7252 en la parte pública y 0.73 en la parte privada.
- Con **Random Forest Regressor** se obtuvo un resultado de 0.77516 en la parte pública.

## Descripción Detallada del Algoritmo Propuesto

La configuración utilizada para el **Random Forest** fue la siguiente:

```R
    formula <- inclinacion_peligrosa ~ circ_tronco_cm + lat + long + peligrosidad_especie + peligrosidad_diametro + peligrosidad_altura
    rf_model <- randomForest(formula,
                             data = train_data,
                             do.trace = TRUE,
                             mtry = 3,
                             importance = TRUE,
                             proximity = TRUE,
                             ntree = 600
    )
```

## Algoritmos y Técnicas Probadas

Para balancear las clases se probó también las técnicas de oversampling, undersampling y oversampling combinadas, y de 
cost-sensitive learning. Sin embargo, ninguna de estas técnicas mejoró los resultados obtenidos con undersampling.

Otros algoritmos probados fueron xgboost, svm y redes neuronales. Sin embargo, ninguno de estos algoritmos mejoró los
resultados obtenidos con random forest.
