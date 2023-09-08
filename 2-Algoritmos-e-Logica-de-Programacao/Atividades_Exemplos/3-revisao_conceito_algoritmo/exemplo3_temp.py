"""
Algoritmo do fluxograma
com valores de entrada corretos: N = 3 e temperaturas da lista  (10,11,12)
"""

N = int(input("Informe quantos valores de temperatura será inserido: "))


def calculando_media_temperatura(quantidade):
    if quantidade < 0:
        print("N deve ser maior que zero!")
    else:
        S = 0
        i = 1
    while i <= N:
        T = int(input("Informe uma das temperaturas: "))
        S += T
        i += 1
    M = S / N
    return print(f"media das temperaturas é: {M}")


calculando_media_temperatura(N)
