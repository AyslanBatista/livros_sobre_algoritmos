"""
1. Monte uma pilha com as caixas que serão analisadas
2. Pegue uma caixa e olhe o que tem dentro dela.
3. Se você encontrar outra caixa dentro dela, adicione-a a um novo monte para ser verificada mais tarde
4. Se vocẽ encontrar uma chave, terminou
5. Repita
"""


def procure_pela_chave(caixa_principal):
    pilha = main_box.crie_uma_pilha_para_busca()
    while pilha is not vazia:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print("Achei a chave!")
