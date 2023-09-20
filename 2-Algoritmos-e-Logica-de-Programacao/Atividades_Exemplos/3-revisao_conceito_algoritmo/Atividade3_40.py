"""
3.40. Elabore um fluxograma e um algoritmo em Portugol que, dado um
valor n inteiro, calculará seu fatorial. Lembrando, o fatorial de um número
n é calculado pela expressão:  n nn n n  ! = (1) (2) (3) 1  ⋅−⋅−⋅−⋅

"""

n = float(input("informe o valor de n: "))

Fat = 1
i = 1

while i <= n:
    Fat *= i
    i += 1

print(f"Fatorial: {Fat}")
