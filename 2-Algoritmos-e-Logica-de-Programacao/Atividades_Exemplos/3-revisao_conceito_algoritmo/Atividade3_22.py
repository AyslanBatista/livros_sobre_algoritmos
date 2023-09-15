"""
Elabore um fluxograma e um algoritmo em Portugol que permitam a  entrada
de três valores e faça a contagem desde o primeiro deles até o segundo
com passo dado pelo terceiro.
"""


inicio = int(input("Digite o valor de início da contagem: "))
fim = int(input("Digite o valor de fim da contagem: "))
passo = int(input("Digite o valor do passo: "))


if passo <= 0:
    print("O valor do passo deve ser maior que zero.")
else:
    for contador in range(inicio, fim + 1, passo):
        print(contador)
