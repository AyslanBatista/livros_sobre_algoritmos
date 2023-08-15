"""
Escreva o código para a função soma, vista anteriormente
"""


def soma(valores):
    if valores == []:
        return 0
    else:
        x = valores.pop(-1)
        return x + soma(valores)


lista = [2, 4, 6]
print(soma(lista))
