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

import pandas as pd
import numpy as np
from collections import deque


class TreeNode:
    def __init__(self, attribute=None, value=None, classification=None, parent=None):
        self.attribute = attribute  # Attribute to test at this node
        self.value = value  # Value of the attribute for this branch (None for leaf nodes)
        self.classification = classification  # Classification result for leaf nodes
        self.parent = parent
        self.children = {}  # Dictionary to store branches (key = attribute value, value = subtree)


def decision_tree_learning(examples: pd.DataFrame, attributes, parent_examples=None, parent=None):
    # if examples is empty then return PLURALITY-VALUE(parent examples)
    if examples.empty:
        return TreeNode(classification=plurality_value(parent_examples), parent=parent)
    # else if all examples have the same classification then return the classification
    elif same_classification(examples):
        return TreeNode(classification=examples.iloc[0, -1], parent=parent)
    # else if attributes is empty then return PLURALITY-VALUE(examples)
    elif not attributes:
        return TreeNode(classification=plurality_value(examples), parent=parent)
    else:
        best_attribute = max(attributes, key=lambda x: importance(x, examples))
        tree = TreeNode(attribute=best_attribute, parent=parent)
        for value_k in examples[best_attribute].unique():
            exs = examples[examples[best_attribute] == value_k]
            subtree = decision_tree_learning(exs, [a for a in attributes if a != best_attribute], examples, tree.attribute + " = " + value_k)
            tree.children[value_k] = subtree
        return tree


def plurality_value(examples):
    target_attribute = examples.columns[-1]
    return examples[target_attribute].value_counts().idxmax()
# .value_counts() cuenta la frecuencia de cada valor en esa columna
# .idxmax() devuelve el valor que tiene la frecuencia máxima


def same_classification(examples):
    return len(examples[examples.iloc[:, -1] == examples.iloc[0, -1]]) == len(examples)
# examples.iloc[:, -1] selecciona la última columna, que contiene las clasificaciones
# examples.iloc[0, -1] accede al valor de clasificación del primer ejemplo
# examples[examples.iloc[:, -1] == examples.iloc[0, -1]] filtra examples para incluir solo las filas donde la
# clasificación en la última columna es igual a la clasificación del primer ejemplo


def b(q):
    if q == 0 or q == 1:
        return 0
    return -(q * np.log2(q) + (1 - q) * np.log2(1 - q))


def remainder(a, example):
    attribute = example[a]
    len_example = len(example)
    return sum((len(example[example[a] == vk]) / len_example) * b(len(example[example[a] == vk]) / len_example)
               for vk in example[a].unique())


# The information gain from the attribute test on A is the expected reduction in entropy
def importance(a, examples):
    return b(len(examples[examples.iloc[:, -1] == examples.iloc[0, -1]]) / len(examples)) - remainder(a, examples)


def print_tree_bfs(root_node):
    if not root_node:
        return

    queue = deque([root_node])

    while queue:
        node = queue.popleft()
        if node.attribute is not None:
            print(f"Test {node.attribute}:")
            print(f"Parent: {node.parent}")
            for value, child_node in node.children.items():
                print(f"  {node.attribute} = {value}")
                queue.append(child_node)
        else:
            print(f"Classify as {node.classification} (Parent: {node.parent})")


if __name__ == '__main__':
    tennis = pd.read_csv('tennis.csv')
    attributes = ['outlook', 'temp', 'humidity', 'wind']
    root_node = decision_tree_learning(tennis, attributes)
    # root_node.print_tree()
    print_tree_bfs(root_node)

# Forma de entrega:

# 1. Colocar un archivo con el nombre tp7-reporte-id3.md que contenga:
#    1. Resultados sobre la evaluación sobre tennis.csv
#    2. Información sobre las estrategias para datos de tipo real
# 2. Dentro de la carpeta (tp7-ml/code) crear una nueva carpeta id3/ donde se va a incluir el código utilizado para la
# implementación del árbol de decisión.
