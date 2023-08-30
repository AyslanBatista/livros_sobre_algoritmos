"""
Você se lembra da pesquisa binária do Capítulo 1? Ela também
é um algoritmo do tipo dividir para conquistar. Você consegue
determinar o caso-base e o caso recursivo para a pesquisa
binária?
"""


def pesquisa_binaria(valores, item):
    if not valores.count(item):
        return print(f"Esse valor {item}, não existe dentro da lista")
    baixo = 0
    alto = len(valores)
    meio = int((baixo + alto) / 2)
    chute = valores[meio]
    if chute == item:
        return chute
    else:
        return (
            pesquisa_binaria(valores[meio:], item)
            if chute < item
            else pesquisa_binaria(valores[:meio], item)
        )


minha_lista = [1, 3, 5, 7, 9, 10, 11, 12]
print(pesquisa_binaria(minha_lista, 10))
