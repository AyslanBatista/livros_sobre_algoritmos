"""
Ler os valores de A e B
C <- 0
Enquanto A > B Faça
    Subtraia B de A, coloque o resultado em A e some 1 em C
Fim Equanto
Mostre os valores finais de C e de A

Execute essa intruções para os seguintes pares de
números: 10 e 2, 6 e 2, 15 e 3
O que significa o valor final de C? e o valor final de A?
"""


valores = {
    "valor1": {"A": 10, "B": 2},
    "valor2": {"A": 6, "B": 2},
    "valor3": {"A": 15, "B": 3},
}

for key, value in valores.items():
    C = 0
    while value["A"] >= value["B"]:
        C += 1
        value["A"] -= value["B"]
    print(f"C:{C}  A:{value['A']}")
