"""
Elabore um fluxograma e um algoritmo em Portugol que representem o algoritmo
para calcular a soma dos primeiros 40 termos da sequência  definida a seguir,
com o valor de A fornecido via teclado:

7*A/3, 7*A/6, 7*A/12, 7*A/24, 7*A/48,...

"""

while True:
    numero = input("informe um numero : ")
    if not numero.replace(".", "").isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue
    elif numero == "0":
        print("###### ERROR: informe valor maior que 0 - ######")
        continue
    numero = float(numero)
    break

soma = 0
divisor = 3
for i in range(0, 40):
    valor = (7 * numero) / divisor
    divisor *= 2
    soma += valor


print(soma)
