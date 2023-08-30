"""
Arrays vazios ou arrays com apenas um elemento serão o caso-base.
Você pode apenas retornar esses arrays como eles estão, visto
que não há nada para ordenar:
"""


def quicksort(array):
    if len(array) < 2:
        return array
