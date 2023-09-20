"""
3.44. Um número da série de Fibonacci é gerado a partir da soma de dois
valores imediatamente anteriores. Convenciona-se que o primeiro número,
0f  é 0, e o segundo, 1  f, é 1. A partir desses valores é possível
calcular o  n-ésimo elemento da série assim (para n > 2):
nn n  =  1 2  ff f  − −  +
"""

n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print("1")
else:
    for count in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)
