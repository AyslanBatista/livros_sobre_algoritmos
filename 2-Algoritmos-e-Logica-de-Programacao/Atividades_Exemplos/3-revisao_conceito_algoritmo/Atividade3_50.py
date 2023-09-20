"""
Elabore um fluxograma e um algoritmo em Portugol que permitam a
entrada de duas cadeias de caracteres, respectivamente, às variáveis
BUSCA e MENSAGEM, e então exibam todas as posições da cadeia contida
em  BUSCA que foram localizadas em MENSAGEM.
"""


def encontrar_posicoes(busca, mensagem):
    posicoes = []
    indice = mensagem.find(busca)

    breakpoint()
    while indice != -1:
        posicoes.append(indice)
        indice = mensagem.find(busca, indice + 1)

    return posicoes


# Solicitar entrada do usuário para as variáveis BUSCA e MENSAGEM
BUSCA = input("Digite a cadeia de caracteres a ser buscada: ")
MENSAGEM = input("Digite a mensagem onde deseja buscar: ")

# Encontrar as posições da cadeia BUSCA em MENSAGEM
posicoes = encontrar_posicoes(BUSCA, MENSAGEM)

# Exibir as posições encontradas
if posicoes:
    print(
        f"A cadeia '{BUSCA}' foi encontrada nas "
        f"seguintes posições em '{MENSAGEM}':"
    )
    for posicao in posicoes:
        print(posicao)
else:
    print(f"A cadeia '{BUSCA}' não foi encontrada em '{MENSAGEM}'.")
