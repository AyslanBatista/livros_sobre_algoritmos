def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("infi")
    nodo_custo_mais_baixo = None
    for nodo in custos:  # vá por cada vértice
        custo = custos[nodo]
        if (
            custo < custo_mais_baixo and nodo not in processados
        ):  # Se for o vértice de menor custo até o momento e ainda não tiver sido processado...
            custo_mais_baixo = (
                custo  # atribua como o novo vértice de menor custo
            )
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo
