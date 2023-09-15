"""
O desconto do IRRF (Imposto de Renda Retido na Fonte),
também denominado “Mordida do Leão”, é calculado sobre o salário líquido
após a  dedução da contribuição ao INSS, de acordo com a seguinte tabela:

Base de cálculo em R$       Alíquota%     Parcela a deduzir do  imposto em R$
Até 1.903,98                   –                            –
De 1.903,99 até 2.826,65      7,5                         142,80
De 2.826,66 até 3.751,05       15                         354,80
De 3.751,06 até 4.664,68      22,5                        636,13
Acima de 4.664,68             27,5                        869,36

Líquido = Bruto-INSS-IR
Líquido = Bruto-INSS-(base*alíquota – parcela)

Elabore um fluxograma e um algoritmo em Portugol que,
para uma entrada  do salário bruto e após a dedução da contribuição
(veja o Exercício 3.17),  calculem o desconto do IRRF.

"""

# INSS
salario1_inss = [0, 1659.38]
salario2_inss = [salario1_inss[1] + 0.01, 2765.66]
salario3_inss = [salario2_inss[1] + 0.01, 5531.31]
salario4_inss = [salario3_inss[1]]
taxas_inss = [8, 9, 11, 608.44]

# IRRF
salario1_irrf = [0, 1903.98]
salario2_irrf = [salario1_irrf[1] + 0.01, 2926.65]
salario3_irrf = [salario2_irrf[1] + 0.01, 3751.05]
salario4_irrf = [salario3_irrf[1] + 0.01, 4664.68]
salario5_irrf = [salario4_irrf[1]]
taxas_irrf = [0, 7.5, 15, 22.5, 27.5]
parcelas_irrf = [0, 142.80, 354.80, 636.13, 869.36]

# TABELA INSS
tabela_valores_inss = {
    "parametro1": {
        "salario": salario1_inss,
        "percentual": taxas_inss[0],
    },
    "parametro2": {
        "salario": salario2_inss,
        "percentual": taxas_inss[1],
    },
    "parametro3": {
        "salario": salario3_inss,
        "percentual": taxas_inss[2],
    },
    "parametro4": {
        "salario": salario4_inss,
        "percentual": taxas_inss[3],
    },
}

# TABELA IRRF
tabela_valores_irrf = {
    "parametro1": {
        "salario": salario1_irrf,
        "percentual": taxas_irrf[0],
        "parcela": parcelas_irrf[0],
    },
    "parametro2": {
        "salario": salario2_irrf,
        "percentual": taxas_irrf[1],
        "parcela": parcelas_irrf[1],
    },
    "parametro3": {
        "salario": salario3_irrf,
        "percentual": taxas_irrf[2],
        "parcela": parcelas_irrf[2],
    },
    "parametro4": {
        "salario": salario4_irrf,
        "percentual": taxas_irrf[3],
        "parcela": parcelas_irrf[3],
    },
    "parametro5": {
        "salario": salario5_irrf,
        "percentual": taxas_irrf[4],
        "parcela": parcelas_irrf[4],
    },
}


while True:
    print(
        "informe o valor do sálario com o centavos "
        "separado por . \nExemplo: 390.90 "
    )
    salario = input("Sálario: ")
    if not salario.replace(".", "").isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue
    elif salario == "0":
        print("###### ERROR: informe um salario real - ######")
        continue
    elif "." in salario:
        salario = float(salario)
    else:
        salario = int(salario)

    break


def calcular_inss(valor_salario, tabela_inss):
    parametros_salario1 = tabela_inss["parametro1"]
    parametros_salario2 = tabela_inss["parametro2"]
    parametros_salario3 = tabela_inss["parametro3"]
    parametros_salario4 = tabela_inss["parametro4"]
    if (
        valor_salario >= parametros_salario1["salario"][0]
        and valor_salario <= parametros_salario1["salario"][1]
    ):
        return calcular_percentual(
            valor_salario, parametros_salario1["percentual"]
        )
    elif (
        valor_salario >= parametros_salario2["salario"][0]
        and valor_salario <= parametros_salario2["salario"][1]
    ):
        return calcular_percentual(
            valor_salario, parametros_salario2["percentual"]
        )
    elif (
        valor_salario >= parametros_salario3["salario"][0]
        and valor_salario <= parametros_salario3["salario"][1]
    ):
        return calcular_percentual(
            valor_salario, parametros_salario3["percentual"]
        )
    else:
        return parametros_salario4["percentual"]


def calculado_irrf(salario_base, tabela_irrf):
    parametros_salario1 = tabela_irrf["parametro1"]
    parametros_salario2 = tabela_irrf["parametro2"]
    parametros_salario3 = tabela_irrf["parametro3"]
    parametros_salario4 = tabela_irrf["parametro4"]
    parametros_salario5 = tabela_irrf["parametro5"]

    if (
        salario_base >= parametros_salario1["salario"][0]
        and salario_base <= parametros_salario1["salario"][1]
    ):
        return (
            calcular_percentual(
                salario_base, parametros_salario1["percentual"]
            )
            - parametros_salario1["parcela"]
        )

    elif (
        salario_base >= parametros_salario2["salario"][0]
        and salario_base <= parametros_salario2["salario"][1]
    ):
        return (
            calcular_percentual(
                salario_base, parametros_salario2["percentual"]
            )
            - parametros_salario2["parcela"]
        )

    elif (
        salario_base >= parametros_salario3["salario"][0]
        and salario_base <= parametros_salario3["salario"][1]
    ):
        return (
            calcular_percentual(
                salario_base, parametros_salario3["percentual"]
            )
            - parametros_salario3["parcela"]
        )

    elif (
        salario_base >= parametros_salario4["salario"][0]
        and salario_base <= parametros_salario4["salario"][1]
    ):
        return (
            calcular_percentual(
                salario_base, parametros_salario4["percentual"]
            )
            - parametros_salario4["parcela"]
        )

    else:
        return (
            calcular_percentual(
                salario_base, parametros_salario5["percentual"]
            )
            - parametros_salario5["parcela"]
        )


def calcular_percentual(valor_salario, taxa):
    return (taxa * valor_salario) / 100.0


valor_a_pagar_inss = calcular_inss(salario, tabela_valores_inss)
base_inss = salario - valor_a_pagar_inss
valor_a_pagar_irrf = calculado_irrf(base_inss, tabela_valores_irrf)

print(f"Valor total a pagar de INSS é: R$ {valor_a_pagar_inss:.2f}")
print(f"Valor total a pagar de IRRF é: R$ {valor_a_pagar_irrf:.2f}")
