def quicksort(array):
    if len(array) < 2:
        # Base: arrays com 0 ou 1 elemento já estão "ordenados"
        return array
    else:
        # Caso recursivo
        pivo = array[0]
        # subarray de todos os elementos menores do que o pivô
        menores = [i for i in array[1:] if i <= pivo]
        # subarray de todos os elementos maiores do que o pivô
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort([10, 5, 2, 3]))
