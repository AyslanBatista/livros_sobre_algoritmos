from math import sqrt

A = int(input("Lado A do triangulo: "))
B = int(input("Lado B do triangulo: "))
C = int(input("Lado C do triangulo: "))


def formula_heron(lado_A, lado_B, lado_C):
    s = (lado_A + lado_B + lado_C) / 2
    K = sqrt(s * (s - lado_A) * (s - lado_B) * (s - lado_C))
    return print(f"{K}cm^2")


formula_heron(A, B, C)
