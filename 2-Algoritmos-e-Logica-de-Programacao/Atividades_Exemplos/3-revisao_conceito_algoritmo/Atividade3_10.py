"""
O mesmo do Exercício 3.9 com as seguintes exigências: só podem ser  utilizadas
duas variáveis e operações de adição e subtração.
"""

x = int(input("informe o primeiro numero: "))
y = int(input("informe o segundo numero: "))
x = x + y
y = x - y
x = x - y


print(f"x:{x} y:{y}")
