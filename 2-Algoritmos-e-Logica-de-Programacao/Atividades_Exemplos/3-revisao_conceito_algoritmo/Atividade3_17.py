"""
A contribuição para o INSS
(interessante para estrutura condicional por  ser progressivo)
é calculada a partir da tabela a seguir:
TABELA VIGENTE
Tabela de contribuição dos segurados empregado,
empregado doméstico e trabalhador avulso,
para pagamento de remuneração a partir de 1º de janeiro de 2017
Portaria Ministerial MF no 8, de 13 de janeiro de 2017

Salário de contribuição (R$) Alíquota para fins de recolhimento  ao INSS (%)
até R$ 1.659,38                             8,00%
de R$ 1.659,39 a R$ 2.765,66                9,00%
de R$ 2.765,67 até R$ 5.531,31              11,00%
acima de R$ 5.531,31                 valor fixo de R$ 608,44

Elabore um algoritmo (fluxograma, em Portugol) que, para uma entrada
do salário bruto, calcule a contribuição ao INSS e o salário líquido restante.
"""
salario1 = [0, 1659.38]
salario2 = [salario1[1] + 0.01, 2765.66]
salario3 = [salario2[1] + 0.01, 5531.31]
salario4 = [salario2[1]]
taxas = [8, 9, 11, 608.44]

tabela_valores = {
    "parametro1": {
        "salario": salario1,
        "percentual": taxas[0],
    },
    "parametro2": {
        "salario": salario2,
        "percentual": taxas[1],
    },
    "parametro3": {
        "salario": salario3,
        "percentual": taxas[2],
    },
    "parametro4": {
        "salario": salario4,
        "percentual": taxas[3],
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


def calcular_percentual(valor_salario, taxa):
    return (taxa * valor_salario) / 100.0


valor_a_pagar = calcular_inss(salario, tabela_valores)

print(f"Valor total a pagar de INSS é: R$ {valor_a_pagar:.2f}")
