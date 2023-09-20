"""
Elabore um fluxograma e um algoritmo em Portugol que representem
o  algoritmo para calcular a soma dos primeiros N termos da sequência
definida a seguir, com N fornecido via teclado:
S=1+2+3+4+5+...+N
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
for i in range(1, numero + 1):
    soma += i


print(soma)
