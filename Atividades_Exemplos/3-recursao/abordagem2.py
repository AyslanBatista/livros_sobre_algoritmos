"""
1. Olhe o que tem dentro da caixa.
2. Se encontrar outra caixa, volte ao passo 1
3. Se encontrar a chave, terminou
"""


def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print("Achei a chave!")
