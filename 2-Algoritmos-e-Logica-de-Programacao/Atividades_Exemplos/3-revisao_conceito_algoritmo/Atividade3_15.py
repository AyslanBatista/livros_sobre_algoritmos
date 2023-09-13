"""
Elabore um fluxograma e um algoritmo em Portugol que calculem e  exibam
a soma dos números pares contidos entre zero e um número par  fornecido
via teclado.
"""
while True:
    numero = input("Informe um numero par: ")
    if not numero.isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue

    numero = int(numero)
    if numero % 2 != 0:
        print("###### ERROR: Informe apenas numeros pares - ######")
    else:
        break


def gerar_numeros(numero_par):
    lista_pares = []
    lista = range(0, numero_par)
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares


def somar_lista(lista):
    return sum(lista)


print(somar_lista(gerar_numeros(numero)))
