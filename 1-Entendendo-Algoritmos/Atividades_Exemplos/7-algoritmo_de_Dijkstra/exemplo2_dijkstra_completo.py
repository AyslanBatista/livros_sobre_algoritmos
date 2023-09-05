nodo = ache_no_custo_mais_baixo(
    custos
)  # Encontrar o custo mais baixo n processado
while (
    nodo is not None
):  # caso todos os vertices tenham sido processados, finaliza
    custo = custos[nodo]
    for n in vizinhos.key():  # Percorrer todos os vizinhos
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:  # Caso o custo for maior que o novo custo
            custos[n] = novo_custo  # Atualiza custo
            pais[n] = nodo  # Este se torna pai doz vizinho

    # Marca o vértice como processado
    processados.append(nodo)

    # Encontrar o próximo vértice a ser processados, algoritmo repetido
    nodo = ache_no_custo_mais_baixo(custos)
