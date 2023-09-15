"""
Elabore um fluxograma e um algoritmo em Portugol que leiam as  quatro notas
de prova (P1, P2, P3 e P4) e quatro notas de trabalho (T1,  T2, T3 e T4) e
posteriormente exibam a mensagem ‘Aprovado’ ou ‘Não  aprovado’ dependendo dos
valores obtidos, conforme as regras de cálculo  definidas a seguir:
"""
print("Exemplo: 10, 9, 8.5, 6.5")
notas_provas = input("Informe as notas referente as provas: ")

print("Exemplo: 10, 9, 8.5, 6.5")
notas_trabalhos = input("Informe as notas referente aos trabalhos: ")

notas_provas = [float(i) for i in notas_provas.split(",")]
notas_trabalhos = [float(i) for i in notas_trabalhos.split(",")]

media_provas = sum(notas_provas) / 4
media_trabalhos = sum(notas_trabalhos) / 4
media_final = (media_provas * 0.8) + (media_trabalhos * 0.2)

if media_final >= 6.0:
    print("#" * 50)
    print("{:-^50}".format("APROVADO"))
    print(f"Sua media final é de {media_final:.2f}\n")
    print()
    print("#" * 50)
else:
    print("#" * 50)
    print("{:-^50}".format("REPROVADO"))
    print(f"Sua media final é de {media_final:.2f}\n")
    print("#" * 50)
