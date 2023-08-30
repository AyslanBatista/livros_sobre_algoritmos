def buscaMenor(arr):
    # Armazena o menor valor
    menor = arr[0]
    # Armazena o índice de menor valor
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


# Ordenações em um array
def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        # Encontrar o menor elemento do array e adiciona ao novo array
        menor = buscaMenor(arr)
        # insere o item na lista "novoArr" e apaga o item da lista "arr"
        breakpoint()
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoporSelecao([5, 3, 6, 2, 10]))
