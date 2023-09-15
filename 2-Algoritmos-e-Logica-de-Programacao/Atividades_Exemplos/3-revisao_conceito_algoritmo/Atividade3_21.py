"""
Elabore um fluxograma e um algoritmo em Portugol que permitam a  entrada
de dois valores inteiros e faça uma contagem decrescente desde o  maior
deles até o menor.
"""

primeiro_valor = int(input("Informe o primeiro valor: "))
segundo_valor = int(input("Informe o segundo valor: "))

if primeiro_valor < segundo_valor:
    [print(i) for i in reversed(range(primeiro_valor, segundo_valor + 1))]
else:
    [print(i) for i in reversed(range(segundo_valor, primeiro_valor + 1))]
