"""
Elabore um fluxograma e um algoritmo em Portugol que representem o
algoritmo para calcular a soma dos primeiros N termos da sequência
definida a seguir, com N fornecido via teclado:
1/2, 1/4, 1/6, 1/8, 1/10, ...
"""

while True:
    numero = input("informe um numero : ")
    if not numero.replace(".", "").isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue
    elif numero == "0":
        print("###### ERROR: informe valor maior que 0 - ######")
        continue
    numero = int(numero)
    break

soma = 0
divisor = 2
for i in range(0, numero):
    valor = 1 / divisor
    divisor += 2
    soma += valor


print(soma)
