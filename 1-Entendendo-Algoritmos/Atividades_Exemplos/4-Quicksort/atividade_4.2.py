"""
Escreva uma função recursiva que conte
o número de itens em uma lista.
"""


def recursiva(valores):
    if len(valores) == 0:
        return 0
    else:
        valores.pop(-1)
        return 1 + recursiva(valores)


lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(recursiva(lista))
