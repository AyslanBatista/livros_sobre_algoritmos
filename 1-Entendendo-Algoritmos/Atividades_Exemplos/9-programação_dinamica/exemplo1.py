"""
Estamos tentando encontrar a maior subtring comum que duas
palavras têm em comum, assim, qual substring hish e fish
tem em comum? E hish e vista? isso é oq ue você quer calcular
"""

if palavra_a[i] == palavra_b[j]:  # As letras combinam
    celula[i][j] = celula[i - 1][j - 1] + 1
else:  # As letras não combinam
    celula[i][j] = 0
