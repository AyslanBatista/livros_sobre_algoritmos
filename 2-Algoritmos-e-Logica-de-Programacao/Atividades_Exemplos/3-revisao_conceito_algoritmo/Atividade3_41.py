"""
Elabore  um algoritmo em Pythonque deverão calcular o número de maneiras
de escolher r dentre n objetos diferentes, não  importando a ordem

"""

import math


def calcular_combinacoes(n, r):
    if n < r:
        combinacoes = math.comb(r, n)
        return combinacoes
    else:
        combinacoes = math.comb(n, r)
        return combinacoes


# Solicitar entrada do usuário para n e r
n = int(input("Digite o valor de n: "))
r = int(input("Digite o valor de r: "))

# Calcular e exibir o número de combinações
combinacoes = calcular_combinacoes(n, r)
print(
    f"O número de maneiras de escolher {r} entre {n} "
    f"objetos diferentes é {combinacoes}."
)
