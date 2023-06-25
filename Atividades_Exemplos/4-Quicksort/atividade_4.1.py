def soma(lista: list) -> int:
    if lista == []:
        return 0
    breakpoint()
    # Retorna a soma do primeiro objeto
    return lista[0] + soma(lista[1:])


lista = [1, 2, 3, 4, 5]
print(soma(lista))
