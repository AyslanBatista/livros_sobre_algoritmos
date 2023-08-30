"""
Você deve somar todos os números e retornar o valor total.
Isso é simples de ser feito com um loop:
"""


def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total


print(soma([1, 2, 3, 4]))
