"""
1.12. Determine quais são os possíveis números (no intervalo fechado de 0 a  9)
que se substituídos nos símbolos F, I, A, T
torna a multiplicação a seguir
verdadeira:
#
      IF
     ×AT
    -----
    FIAT
#
Os valores de F, I, A, T devem ser diferentes entre si.
"""

import random

valores = list(range(10))

F = 0
i = 0
A = 0
T = 0

while True:
    random.shuffle(valores)
    F = valores[0]
    i = valores[1]
    A = valores[2]
    T = valores[3]
    valor1 = str(i) + str(F)
    valor2 = str(A) + str(T)
    resultado = int(valor1) * int(valor2)
    if (
        F != i
        and F != A
        and F != T
        and i != A
        and i != T
        and A != T
        and len(str(resultado)) > 3
    ):
        if (
            str(resultado)[0] == str(F)
            and str(resultado)[1] == str(i)
            and str(resultado)[2] == str(A)
            and str(resultado)[3] == str(T)
        ):
            print(
                f"  {i}{F}\n"
                f"x {A}{T}\n"
                f"F:{F}   I:{i}   A:{A}   T:{T}"
                )
            break
