"""
Um número inteiro é considerado triangular se for o produto de três
números inteiros consecutivos, como, por exemplo 120 = 4x5x6 . Elabore
um fluxograma e um algoritmo em Portugol que, após lerem em um número
"""

numero = int(input("informe o numero que deseja verificar : "))

a = 0
b = 1
c = 2
while numero >= a:
    valor = a * b * c
    if valor == numero:
        print(f"{a}x{b}x{c}")
        print(numero)
        break
    a += 1
    b += 1
    c += 1
