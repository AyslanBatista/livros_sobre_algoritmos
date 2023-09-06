def verificar_moeda_falsa(peso_total, peso_unico):
    peso_divido = peso_total / 5
    if peso_divido == peso_unico:
        return print("Não existe moeda falsa")
    else:
        return print("Existe moeda falsa")


peso_total_moedas = float(input("Informe o peso de todas as moedas: "))
peso_unico_moeda = float(input("Informe o peso de uma unica moeda: "))

verificar_moeda_falsa(peso_total_moedas, peso_unico_moeda)
