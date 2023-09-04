def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []  # Vetor que contem as pessoas verificadas
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if (
            not pessoa in verificadas
        ):  # Verifica somente se ela não foi verificada
            print(f"{pessoa} é um vendedor de manga!")
            return True
        else:
            fila_de_pesquisa += grafo[pessoa]
            verificadas.append(pessoa) # Marca a pessoa como verificada
    return False
