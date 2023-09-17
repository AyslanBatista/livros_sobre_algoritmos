"""
3.25. Um número palíndromo é aquele que se lido da esquerda para a direita
e da direita para a esquerda possui o mesmo valor (por exemplo: 34543).
Elabore um fluxograma e um algoritmo em Portugol que leiam um número  n,
inteiro, e verifique se ele é um palíndromo.
"""

numero = input("informe o numero que deseja verificar se é palíndromo : ")

numero_lista = list(numero)
numero_lista_reverse = list(numero)
numero_lista_reverse.reverse()

if numero_lista == numero_lista_reverse:
    print(
        f"{numero_lista}\n"
        f"{numero_lista_reverse}\n"
        "Esse é um numero palíndromo"
    )
else:
    print(
        f"{numero_lista}\n"
        f"{numero_lista_reverse}\n"
        "Esse não é um numero palíndromo"
    )
