"""
Elabore um fluxograma e um algoritmo em Portugol que permitam a  entrada
de 30 valores e mostre a soma de seus inversos.
Observação: o inverso de x é 1/ x.
"""
valor = 0
lista_numeros = []
while valor <= 30:
    numero = input(f"informe o valor de número {valor}: ")
    if not numero.replace(".", "").isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue
    elif numero == "0":
        print("###### ERROR: informe valor maior que 0 - ######")
        continue
    lista_numeros.append(float(numero))
    valor += 1

nova_lista_numeros = []
for i in lista_numeros:
    inverso = 1 / i
    nova_lista_numeros.append(inverso)


somar_inverso = sum(nova_lista_numeros)

print(f"{somar_inverso}")
