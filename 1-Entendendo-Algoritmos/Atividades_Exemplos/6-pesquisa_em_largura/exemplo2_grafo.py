from collections import deque

fila_de_pesquisa = deque()  # Cria uma nova lista
fila_de_pesquisa += grafo[
    "voce"
]  # Adiciona todos os seus vizinhos para a lista de pesquisa


while fila_de_pesquisa:  # Enquanto a fila não estiver vazia
    pessoa = fila_de_pesquisa.popleft()  # Pega a primeira pessoa da fila
    if pessoa_e_vendedor(pessoa):  # Verifica se a pessoa vende manga
        print(f"{pessoa} é um vendedor de manga!")  # sim vende manga
        return True
    else:
        fila_de_pesquisa += grafo[pessoa]  # Não vende, adiciona amigos a lista
return False  # Ninguem vende manga
