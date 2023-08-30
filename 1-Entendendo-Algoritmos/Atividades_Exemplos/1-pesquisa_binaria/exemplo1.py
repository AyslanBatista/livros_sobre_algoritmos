"""
EXEMPLO NUMERO 1

baixo = 0
alto = len(lista)-1
meio = (baixo+alto)/2
chute = lista[meio]

if chute < item:
    baixo = meio + 1

"""


def pesquisa_binaria(lista, item):
    # baixo e alto acompanham a parte da lista que você está prcurando
    baixo = 0
    alto = len(lista) - 1
    # enquanto ainda não conseguiu chegar a um único elemento
    while baixo <= alto:
        # Verificar o elemento central
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        # Acha o item
        if chute == item:
            return chute
        # Chute foi muito alto
        if chute > item:
            alto = meio - 1
        # Chute foi muito baixo
        else:
            baixo = meio + 1
    # O item não existe
    return None


minha_lista = [1, 3, 5, 7, 9, 10, 11, 12]
# breakpoint()

# Lembre-se, as listas começam no 0. O próximo endereço tem índice 1.
print(pesquisa_binaria(minha_lista, 12))  # 12
print(pesquisa_binaria(minha_lista, -1))  # None
