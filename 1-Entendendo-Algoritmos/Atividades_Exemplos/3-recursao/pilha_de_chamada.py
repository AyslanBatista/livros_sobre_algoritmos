def sauda2(nome):
    print(f"Como vai {nome} ?")


def tchau():
    print("ok, tchau")


def sauda(nome):
    print(f"ola, {nome} !")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau()
