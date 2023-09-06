def verificar_moeda_falsa(peso_total, quantidade, peso_unico):
    peso_divido = peso_total / quantidade
    if peso_divido == peso_unico:
        return print("Não existe moeda falsa")
    else:
        if peso_divido > peso_unico:
            return print("Existe moeda falsa, e ela tem maior massa")
        else:
            return print("Existe moeda falsa, e ela tem menor massa")


peso_total_moedas = float(input("Informe o peso de todas as moedas: "))
quantidade_moedas = int(input("Informe quantidade de moedas: "))
peso_unico_moeda = float(input("Informe o peso de uma unica moeda: "))

verificar_moeda_falsa(peso_total_moedas, quantidade_moedas, peso_unico_moeda)
