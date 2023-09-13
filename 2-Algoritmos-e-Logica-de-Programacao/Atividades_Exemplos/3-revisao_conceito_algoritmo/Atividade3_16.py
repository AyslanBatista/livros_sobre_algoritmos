"""
Elabore um fluxograma e um algoritmo em Portugol que calculem e exibam a soma
dos números ímpares contidos entre zero e um número ímpar  fornecido
via teclado.

"""
while True:
    numero = input("Informe um numero impar: ")
    if not numero.isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue

    numero = int(numero)
    if numero % 2 == 0:
        print("###### ERROR: Informe apenas numeros impares - ######")
    else:
        break


def gerar_numeros(numero_impar):
    lista_impares = []
    lista = range(0, numero_impar)
    for numero in lista:
        if numero % 2 != 0:
            lista_impares.append(numero)
    return lista_impares


def somar_lista(lista):
    return sum(lista)


print(somar_lista(gerar_numeros(numero)))
