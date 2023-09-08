"""
3.1.
Elabore um fluxograma e um algoritmo em Portugol que calculem
quantas notas de 50, 10 e 1 são necessárias para pagar uma conta cujo valor 
é fornecido
"""

while True:
    valor = input("Informe o valor da conta: ")
    if not valor.isdigit():
        print("Valor informado não é um numero")
        continue
    else:
        valor_int = int(valor)
        break


def pagar_conta(valor_conta):
    valor_inicial = valor_conta

    notas_50 = valor_conta // 50
    if notas_50 != 0:
        valor_conta -= notas_50 * 50

    notas_20 = valor_conta // 20
    if notas_20 != 0:
        valor_conta -= notas_20 * 20

    notas_1 = valor_conta // 1
    if notas_1 != 0:
        valor_conta -= notas_1 * 1

    return print(
        f"Valor de {valor_inicial} será pago com as quantidade de notas:\n"
        f"50: {notas_50}   20: {notas_20}   1: {notas_1}"
    )


pagar_conta(valor_int)
