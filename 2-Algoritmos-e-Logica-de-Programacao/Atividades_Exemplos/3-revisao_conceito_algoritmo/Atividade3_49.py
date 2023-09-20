"""
3.49. Elabore um fluxograma e um algoritmo em Portugol que permitam
a  entrada de N cadeias de caracteres e então exibam as seguintes
estatísticas: o  número total de caracteres digitados
(incluindo espaços em branco) e  o número total de palavras.
"""

nome = input("Informe um texto: ")

caracteres = len(nome)

palavras = nome.split()

quantidade_palavras = len(palavras)

print(
    f"Quantidade de caracteres: {caracteres}\n"
    f"Quantidade de palavras: {quantidade_palavras}"
)
