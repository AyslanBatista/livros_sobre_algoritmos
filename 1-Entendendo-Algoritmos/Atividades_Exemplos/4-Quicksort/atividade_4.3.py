"""
Encontre o valor mais alto em uma lista.
"""


def valor_mais_alto(lista_valores):
    if len(lista_valores) == 2:
        return (
            lista_valores[0]
            if lista_valores[0] > lista_valores[-1]
            else lista_valores[-1]
        )
    x = lista_valores.pop(-1)
    maior_valor = valor_mais_alto(lista_valores)
    return maior_valor if maior_valor > x else x


lista = [12, 43, 65, 1, 34, 52, 71, 6, 4, 2]
print(valor_mais_alto(lista))
