"""
Elabore um fluxograma e um algoritmo em Portugol que permitam a  entrada
de dez valores e calcule o produto de todos eles.
"""

A = int(input("Informe o lado A: "))
B = int(input("Informe o lado B: "))
C = int(input("Informe o lado C: "))

if A < (B + C) and B < (A + C) and C < (A + B):
    print(f"A: {A}   B: {B}  C: {C}\n" "Esses lados podem ser de um triângulo")
else:
    print(
        f"A: {A}   B: {B}  C: {C}\n"
        "Esses lados não podem ser de um triângulo"
    )

