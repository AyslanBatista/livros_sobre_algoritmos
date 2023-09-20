"""
Elabore um algoritmo em Python que, dados dois  números complexos c1 e c2,
calculem as seguintes operações: soma, subtração e multiplicação.
Lembrando: um número complexo possui duas partes, uma real (re) e uma
imaginária (im), representado genericamente como c = re + j . im


"""

c1_re = float(input("Digite a parte real de c1: "))
c1_im = float(input("Digite a parte imaginária de c1: "))
c2_re = float(input("Digite a parte real de c2: "))
c2_im = float(input("Digite a parte imaginária de c2: "))


c1 = complex(c1_re, c1_im)
c2 = complex(c2_re, c2_im)


soma = c1 + c2
subtracao = c1 - c2
multiplicacao = c1 * c2


print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
