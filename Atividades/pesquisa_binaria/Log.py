import math
import sys


def log(numero, base):
    resultado = math.log(numero, base)
    return resultado


# log = lambda numero, base: math.log(numero, base)


while True:
    numero_log = input("Digite o logaritmando :").strip()
    base_log = input("Digite a base :").strip()

    try:
        numeros = []
        for n in [numero_log, base_log]:
            n = numeros.append(int(n))

    except ValueError as e:
        print(f"[Error] {e}, informe apenas números")
        sys.exit(1)

    print(f"Resultado = {log(numeros[0], numeros[1])}")

    if input("Pressione enter para continuar, qualquer tecla para sair"):
        break
