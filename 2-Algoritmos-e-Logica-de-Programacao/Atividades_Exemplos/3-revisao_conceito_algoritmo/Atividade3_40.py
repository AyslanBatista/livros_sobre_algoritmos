"""
3.40. Elabore um fluxograma e um algoritmo em Portugol que, dado um
valor n inteiro, calculará seu fatorial. Lembrando, o fatorial de um número
n é calculado pela expressão:  n nn n n  ! = (1) (2) (3) 1  ⋅−⋅−⋅−⋅ 

"""

valor_q = float(input("informe o valor de Q: "))
valor_d = float(input("informe o valor de D : "))
n = 0

if valor_d > 100:
    n = 2
elif valor_d < 50:
    n = 6
else:
    n = 4

S = n * (4 * valor_q) / (3.14 * (valor_d**2))

print(S)
