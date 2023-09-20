"""
Elabore um fluxograma e um algoritmo em Portugol que permitam a entrada
de um número inteiro entre 1 e 9999 e escreva seu valor por extenso.
"""


def numero_para_extenso(numero):
    unidades = [
        "",
        "um",
        "dois",
        "três",
        "quatro",
        "cinco",
        "seis",
        "sete",
        "oito",
        "nove",
    ]
    dezenas = [
        "",
        "dez",
        "vinte",
        "trinta",
        "quarenta",
        "cinquenta",
        "sessenta",
        "setenta",
        "oitenta",
        "noventa",
    ]
    especiais = [
        "dez",
        "onze",
        "doze",
        "treze",
        "quatorze",
        "quinze",
        "dezesseis",
        "dezessete",
        "dezoito",
        "dezenove",
    ]

    if 1 <= numero <= 9999:
        milhares = numero // 1000
        centenas = (numero // 100) % 10
        dezena_unidade = numero % 100

        extenso = ""

        if milhares > 0:
            extenso += unidades[milhares] + " mil"
            if centenas > 0 or dezena_unidade > 0:
                extenso += " e "

        if centenas > 0:
            extenso += (
                unidades[centenas] + "cento"
                if centenas == 1
                else unidades[centenas] + "centos"
            )
            if dezena_unidade > 0:
                extenso += " e "

        if dezena_unidade > 0:
            if dezena_unidade < 10:
                extenso += unidades[dezena_unidade]
            elif dezena_unidade < 20:
                extenso += especiais[dezena_unidade - 10]
            else:
                dezena = dezena_unidade // 10
                unidade = dezena_unidade % 10
                extenso += dezenas[dezena]
                if unidade > 0:
                    extenso += " e " + unidades[unidade]

        return extenso

    else:
        return "Número fora do intervalo (1 a 9999)"


# Solicita a entrada do usuário
numero = int(input("Digite um número entre 1 e 9999: "))
extenso = numero_para_extenso(numero)

# Exibe o número por extenso
print(f"O número {numero} por extenso é: {extenso}")
