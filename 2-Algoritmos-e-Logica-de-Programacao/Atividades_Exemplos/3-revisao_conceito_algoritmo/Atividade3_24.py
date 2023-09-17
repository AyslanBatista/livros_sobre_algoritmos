"""
3.24. Elabore um fluxograma e um algoritmo em Portugol que leiam um valor n
inteiro e verifique se este é ou não primo
(número primo é divisível  por um e por ele mesmo).

"""

numero = int(input("informe o numero que deseja verificar se é primo : "))


numeros = [i for i in range(2, numero + 1)]
divisor = 0
while numero > divisor:
    if numero == 1:
        print(f"Esse numero não é Primo {numero}")
        break

    divisor = numeros.pop(0)
    if numero % divisor == 0 and numero != divisor:
        print(f"Esse numero não é Primo {numero}")
        break
    elif numero == 2:
        print(f"Esse numero é Primo {numero}")
    elif (divisor + 1) == numero:
        print(f"Esse numero é Primo {numero}")
