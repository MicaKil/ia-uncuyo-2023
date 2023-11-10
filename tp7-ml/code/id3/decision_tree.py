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


class Attribute:
    def __init__(self, name, values):
        self.name = name
        self.values = values


class DecisionTree:
    def __init__(self, attribute):
        self.attribute = attribute
        self.branches = {}

    def __str__(self):
        return str(self.attribute)

    def __repr__(self):
        return str(self.attribute)

    def __getitem__(self, item):
        return self.branches[item]

    def add_branch(self, value, subtree):
        self.branches[value] = subtree

    def bfs(self):
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node)
            for branch in node.branches.values():
                queue.append(branch)


def decision_tree_learning(examples: pd.DataFrame, attributes, parent_examples):
    if len(examples) == 0:
        return plurality_value(parent_examples)
    elif same_classification(examples):
        return examples.iloc[0, -1]
    elif len(attributes) == 0:
        return plurality_value(examples)
    else:
        a = max(attributes, key=lambda x: importance(x, examples))
        tree = DecisionTree(a)
        for vk in a.values:
            exs = examples[examples[a.name] == vk]
            subtree = decision_tree_learning(exs, attributes - {a}, examples)
            tree.branches[vk] = subtree
        return tree


def plurality_value(examples):
    target_attribute = examples.columns[-1]
    return examples[target_attribute].value_counts().idxmax()
# .value_counts() cuenta la frecuencia de cada valor en esa columna
# .idxmax() devuelve el valor que tiene la frecuencia máxima


def same_classification(examples: pd.DataFrame):
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
    attribute = example[a.name]
    len_example = len(example)
    return sum((len(example[attribute == vk]) / len_example) * b(len(example[attribute == vk]) / len_example)
               for vk in a.values)


# The information gain from the attribute test on A is the expected reduction in entropy
def importance(a, examples):
    return b(len(examples[examples.iloc[:, -1] == 'yes']) / len(examples)) - remainder(a, examples)


if __name__ == '__main__':
    tennis = pd.read_csv('tennis.csv')
    attributes = set([Attribute(name, tennis[name].unique()) for name in tennis.columns[:-1]])
    tree = decision_tree_learning(tennis, attributes, None)
    tree.bfs()

# Forma de entrega:

# 1. Colocar un archivo con el nombre tp7-reporte-id3.md que contenga:
#    1. Resultados sobre la evaluación sobre tennis.csv
#    2. Información sobre las estrategias para datos de tipo real
# 2. Dentro de la carpeta (tp7-ml/code) crear una nueva carpeta id3/ donde se va a incluir el código utilizado para la
# implementación del árbol de decisión.
