"""
Algortimo para calcular as raízes de uma equação de 2º grau
"""


from math import sqrt

A = int(input("Informe o valor de A: "))
B = int(input("Informe o valor de B: "))
C = int(input("Informe o valor de C: "))

if A == 0:
    print("Não é equação de 2º grau!")
else:
    D = sqrt(B) - 4 * A * C
    if D < 0:
        print("Não existe raízes reais!")
    else:
        r1 = (-B + sqrt(D)) / (2 * A)
        r2 = (-B - sqrt(D)) / (2 * A)
        print(f"r1: {r1}\n r2: {r2}")
