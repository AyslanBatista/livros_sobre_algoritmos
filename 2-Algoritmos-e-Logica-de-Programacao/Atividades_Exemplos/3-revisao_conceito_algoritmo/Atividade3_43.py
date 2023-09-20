"""
Escreva um fluxograma e um algoritmo em Portugol que leiam três
valores quaisquer para as variáveis A, B e C. A seguir, ordene esses
valores  exibindo as mesmas variáveis A, B e C, agora já ordenadas.

"""

A = int(input("Informe o valor A: "))
B = int(input("Informe o valor B: "))
C = int(input("Informe o valor C: "))

lista_valores = [A, B, C]

nova_lista = sorted(lista_valores)

A = nova_lista[0]
B = nova_lista[1]
C = nova_lista[2]

print(f"{A}\n{B}\n{C}")
