"""
10 sacos cheio de moedas idênticas na aparência
1 dos sacos são falsos com 1g menor que as verdadeiras

Qual o menor número de pesagens necessárias para descobrir
o saco de moedas falsas?
"""
saco_1 = 10
saco_2 = 3
saco_3 = 10
saco_4 = 10
saco_5 = 10
saco_6 = 10
saco_7 = 10
saco_8 = 10
saco_9 = 10
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
    (
        saco_peso_verdadeiro,
        quantidade_pesagem,
        provavel_saco_falso,
    ) = verificando_peso_verdadeiro(total_sacos[:2], quantidade_pesagem)

    if provavel_saco_falso < saco_peso_verdadeiro:
        return print(
            f"Existe um salco falso com peso de {provavel_saco_falso},\n"
            f"pesagens feitas: {quantidade_pesagem}"
        )

    nova_lista_total = total_sacos[2:]
    while len(nova_lista_total) > 1:
        metade = len(nova_lista_total) // 2
        montante_esquerda, pesagem1 = balanca(nova_lista_total[:metade])
        montante_direita, pesagem2 = balanca(nova_lista_total[metade:])
        quantidade_pesagem += sum([pesagem1, pesagem2])

        if montante_direita == montante_esquerda:
            return print(
                f"Não existe nenhum saco falso!!\n"
                f"pesagens feitas: {quantidade_pesagem}"
            )

        if (
            saco_peso_verdadeiro * len(nova_lista_total[:metade])
        ) != montante_esquerda:
            nova_lista_total = nova_lista_total[:metade]
        elif (
            saco_peso_verdadeiro * len(nova_lista_total[metade:])
        ) != montante_direita:
            nova_lista_total = nova_lista_total[metade:]
    return print(
        f"Existe um salco falso com peso de {nova_lista_total},\n"
        f"pesagens feitas: {quantidade_pesagem}"
    )


def verificando_peso_verdadeiro(dois_sacos, valor_da_pesagem):
    primeiro_saco, pesagem1 = balanca(dois_sacos[0])
    segundo_saco, pesagem2 = balanca(dois_sacos[1])
    valor_da_pesagem += sum([pesagem1, pesagem2])
    if primeiro_saco == segundo_saco or primeiro_saco > segundo_saco:
        return primeiro_saco, valor_da_pesagem, segundo_saco
    else:
        return segundo_saco, valor_da_pesagem, primeiro_saco


def balanca(montante):
    pesagem = 1
    if type(montante) == int:
        return montante, pesagem
    elif type(montante) == list:
        return sum(montante), pesagem


verificar_saco_falso(lista_sacos, pesagem)
