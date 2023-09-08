"""
MDC entre x e y
ex: x=18 y=15

Algoritmo para calcular o máximo divisor comum entre dois números
"""
x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))

while y != 0:
    r = x % y
    x = y
    y = r
print(x)
