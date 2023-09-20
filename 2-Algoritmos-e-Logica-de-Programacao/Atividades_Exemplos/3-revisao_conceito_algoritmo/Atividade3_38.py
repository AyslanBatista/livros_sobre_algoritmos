"""
3.38. Elabore um fluxograma e um algoritmo em Portugol que calculem e
exibam a tensão S de uma barra cilíndrica de diâmetro D submetida a uma
carga Q. Os valores de D e Q devem ser digitados via teclado.
Utilize a fórmula 2  4  =  Q  S n  π D  ⋅  ⋅  ⋅  , considerando
as seguintes condições:
se D >100, então n = 2;
se D < 50, então n = 6;
caso contrário, n = 4.
"""

valor_q = float(input("informe o valor de Q: "))
valor_d = float(input("informe o valor de D : "))
n = 0

if valor_d > 100:
    n = 2
elif valor_d < 50:
    n = 6
else:
    n = 4

S = n * (4 * valor_q) / (3.14 * (valor_d**2))

print(S)
