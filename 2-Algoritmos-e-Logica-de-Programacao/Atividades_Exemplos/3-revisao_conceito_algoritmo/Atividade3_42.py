"""
A fórmula de juros compostos é a seguinte:  = (1 )N  V iV  f i  +  ⋅
Vf é o valor final obtido após N períodos de aplicação com juros i.
Vi é o  valor inicial, à vista. Elabore um fluxograma e um algoritmo
em Portugol que, após lerem o valor inicial, o número de períodos
(que normalmente  são meses) e a taxa de juros,
calculem o valor final desejado.
"""

meses = int(input("Informe a quantidade de Meses: "))
juros = float(input("Informe o valor da taxa de juros: "))
valor_inicial = float(input("Informe o valor inicial: "))

valor_final = ((1 + juros/100) ** meses) * valor_inicial

print(valor_final)
