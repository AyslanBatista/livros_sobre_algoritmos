"""
3.48. Elabore um fluxograma e um algoritmo em Portugol que compactem
um texto contido em uma cadeia de caracteres, eliminando os seus espaços
em branco. Mais especificamente, se o texto fornecido
for ‘O amor é  lindo!’ (representa um espaço em branco), o resultado
a ser apresentado  deverá ser ‘Oamorélindo!’.



"""

nome = input("Informe um texto: ")

print(nome.replace(" ", ""))
