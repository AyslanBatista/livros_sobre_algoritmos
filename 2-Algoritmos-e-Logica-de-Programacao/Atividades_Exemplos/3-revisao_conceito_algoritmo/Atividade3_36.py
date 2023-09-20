"""
Elabore um fluxograma e um algoritmo em Portugol que representem o
algoritmo do cálculo dos 50 primeiros termos da série apresentada a seguir,
sendo X um valor digitado:  23 25 27 29  ,,,,  XXXX 3579  ⋅⋅⋅⋅  ++++  
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
for i in range(0, 50):
    valor = (2 * divisor) / (numero + divisor)
    divisor *= 2
    soma += valor


print(soma)
