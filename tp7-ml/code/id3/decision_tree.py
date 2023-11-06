# PARTE C

# 1. Implementar un algoritmo para construir un árbol de decisión de acuerdo al pseudocódigo provisto en AIMA (Se puede
# implementar en Python).
#    1. El algoritmo solo deberá considerar variables discretas.
#    2. Se deberá comprobar su correcto funcionamiento de manera empírica sobre el dataset tennis.csv
# 2. Investigar sobre las estrategias de los árboles de decisión para datos de tipo real y elaborar un breve resumen.

# function DECISION-TREE-LEARNING(examples, attributes, parent examples) returns a tree
#     if examples is empty then return PLURALITY-VALUE(parent examples)
#     else if all examples have the same classification then return the classification
#     else if attributes is empty then return PLURALITY-VALUE(examples)
#     else
#         A ← argmax{a ∈ attributes} IMPORTANCE(a, examples)
#         tree ← a new decision tree with root test A
#         for each value vk of A do
#             exs ← {e : e ∈ examples and e.A = vk}
#             subtree ← DECISION-TREE-LEARNING(exs, attributes − A, examples)
#             add a branch to tree with label (A = vk) and subtree subtree
#         return tree

# Forma de entrega:

# 1. Colocar un archivo con el nombre tp7-reporte-id3.md que contenga:
#    1. Resultados sobre la evaluación sobre tennis.csv
#    2. Información sobre las estrategias para datos de tipo real
# 2. Dentro de la carpeta (tp7-ml/code) crear una nueva carpeta id3/ donde se va a incluir el código utilizado para la
# implementación del árbol de decisión.