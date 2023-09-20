"""
Elabore um fluxograma e um algoritmo em Portugol que permitam a  entrada
de dez valores e calcule o produto de todos eles.
"""

lista_numeros = []
while len(lista_numeros) <= 10:
    numero = input("informe um numero : ")
    if not numero.replace(".", "").isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue
    elif numero == "0":
        print("###### ERROR: informe valor maior que 0 - ######")
        continue
    lista_numeros.append(int(numero))

produto = 1
for i in lista_numeros:
    produto *= i

print(f"{lista_numeros}\nProduto: {produto}")
