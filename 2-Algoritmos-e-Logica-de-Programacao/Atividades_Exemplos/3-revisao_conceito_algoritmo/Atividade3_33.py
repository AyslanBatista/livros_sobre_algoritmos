"""
3.33. O número π pode ser calculado por meio da série infinita:
π ⋅−+−+− + −

Elabore um fluxograma e um algoritmo em Portugol que calculem e exibam
o valor do número π utilizando a série anterior, até que o valor absoluto
da diferença entre o número calculado em uma interação e o da anterior
seja menor ou igual 0.00000000005.


"""


def calcular_pi():
    pi_aproximado = 0
    denominador = 1
    termo_atual = 1

    while True:
        termo_anterior = termo_atual
        termo_atual = (
            1 / denominador if denominador % 2 == 1 else -1 / denominador
        )
        pi_aproximado += termo_atual

        # Verifica se a diferença entre os termos
        # consecutivos é menor ou igual a 0.00000000005
        breakpoint()
        if abs(termo_atual - termo_anterior) <= 0.00000000005:
            break

        denominador += 2

    return 4 * pi_aproximado


valor_pi = calcular_pi()
print(f"Valor aproximado de π: {valor_pi}")
