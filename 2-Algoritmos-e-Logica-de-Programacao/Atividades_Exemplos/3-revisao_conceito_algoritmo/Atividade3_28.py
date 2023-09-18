"""
3.28. Elabore um fluxograma e um algoritmo em Portugol que permitam a
entrada de n valores e mostre a soma de seus quadrados.

"""

lista_numeros = []
while True:
    numero = input("informe um numero : ")
    if not numero.replace(".", "").isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue
    elif numero == "0":
        print("###### ERROR: informe valor maior que 0 - ######")
        continue
    lista_numeros.append(int(numero))

    pergunta = input("Deseja informar mais um numero? 'SIM' ou 'NAO'")
    if pergunta == "nao" or pergunta == "NAO":
        break
    else:
        continue


nova_lista_numeros = []
for i in lista_numeros:
    quadrado = i**2
    nova_lista_numeros.append(quadrado)


somar_inverso = sum(nova_lista_numeros)

print(f"{somar_inverso}")
