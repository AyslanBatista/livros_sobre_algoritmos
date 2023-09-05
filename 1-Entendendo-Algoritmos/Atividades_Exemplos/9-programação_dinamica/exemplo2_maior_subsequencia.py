"""
Maior subsequência comum entre palavras
"""

if palavra_a[i] == palavra_b[j]:  # As letras combinam
    celula[i][j] = celula[i - 1][j - 1] + 1
else:  # As letras não combinam
    celula[i][j] = max(celula[i - 1][j], celula[i][j - 1])
