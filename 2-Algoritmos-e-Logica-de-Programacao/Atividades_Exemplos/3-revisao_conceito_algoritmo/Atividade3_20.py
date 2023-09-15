"""
3.20. Elabore um fluxograma e um algoritmo em Portugol que transformem  uma
temperatura fornecida em o C na correspondente em o F.

"""

temperatura_c = float(
    input("Informe a temperatura em Cº que deseja transformar em ºF: ")
)


temperatura_f = (temperatura_c * 1.8) + 32

print("#" * 50)
print("{:-^50}".format("TEMPERATURA"))
print(f"\nCº: {temperatura_c:.2f}")
print(f"Fº: {temperatura_f:.2f}\n")
print("#" * 50)
