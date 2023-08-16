"""
A linguagem Python contém tabelas hash chamadas de dicionários.
Para criar uma nova tabela hash você pode utilizar a função dict
"""

caderno = dict()
caderno["maça"] = 0.67  # Uma maça custa 67 centavos
caderno["leite"] = 1.49  # O leite custa R$ 1,49
caderno["abacate"] = 1.49
print(caderno)
print(caderno["abacate"])  # O Preço de um abacate


lista_telefonica = dict()
lista_telefonica["jenny"] = 8675309
lista_telefonica["emergency"] = 911
print(lista_telefonica["jenny"])  # Número de telefone da Jenny


"""
A função get(pegar) retornará um valor se "Tom" já estiver na tabela hash.
Caso contrário, ela retornará None(nada). Você pode usar esta funcionalidade
para conferir se as pessoas já votaram!
"""

votaram = {}
valor = votaram.get("tom")


def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        votaram[nome] = True
        print("Deixe votar!")
        print(votaram)


verifica_eleitor("mike")
verifica_eleitor("tom")
verifica_eleitor("mike")
