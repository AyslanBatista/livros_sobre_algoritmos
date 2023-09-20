"""
O número 3025 possui uma característica interessante,
sendo a seguinte: 30 25 = 55  + e 2  55 = 3025. Elabore um fluxograma e um
algoritmo em  Portugol que verifiquem se um número inteiro de quatro
algarismos (digitado) tem essa propriedade ou não.

"""

while True:
    numero = input("informe um numero : ")
    if not numero.replace(".", "").isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue
    elif len(numero) != 4:
        print("###### ERROR: informe um numero com 4 algarismos - ######")
        continue
    break


parte1 = numero[0:2]
parte2 = numero[2:4]

soma = int(parte1) + int(parte2)

if soma**2 == int(numero):
    print(f"Numero {numero} tem a propriedade")
else:
    print(f"Numero {numero} não tem a propriedade")
