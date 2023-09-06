"""
10 sacos cheio de moedas idênticas na aparência
1 dos sacos são falsos com 1g menor que as verdadeiras

Qual o menor número de pesagens necessárias para descobrir
o saco de moedas falsas?
"""
saco_1 = 10
saco_2 = 10
saco_3 = 10
saco_4 = 10
saco_5 = 10
saco_6 = 10
saco_7 = 10
saco_8 = 10
saco_9 = 3
saco_10 = 10

lista_sacos = [
    saco_1,
    saco_2,
    saco_3,
    saco_4,
    saco_5,
    saco_6,
    saco_7,
    saco_8,
    saco_9,
    saco_10,
]

pesagem = 0


def verificar_saco_falso(total_sacos, quantidade_pesagem):
    if len(total_sacos) == 1:
        return print(
            f"Existe um salco falso com peso de {total_sacos},"
            f"pesagens feitas: {quantidade_pesagem}"
        )

    metade = len(total_sacos) // 2
    montante_esquerda, pesagem1 = balanca(total_sacos[:metade])
    montante_direita, pesagem2 = balanca(total_sacos[metade:])
    quantidade_pesagem += sum([pesagem1, pesagem2])
    breakpoint()
    if montante_esquerda < montante_direita:
        verificar_saco_falso(total_sacos[:metade], quantidade_pesagem)
    else:
        verificar_saco_falso(total_sacos[metade:], quantidade_pesagem)


def balanca(montante):
    pesagem = 1
    return sum(montante), pesagem


verificar_saco_falso(lista_sacos, pesagem)
