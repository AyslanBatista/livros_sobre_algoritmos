# Lista de estados que deseja abranger
# Você passa um array como entrada e eele é convertido em um conjunto
# Conjunto é como uma lista, exceto pelo fato de cada item aparacer 1 vez
estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Lista para estações, Escolhi usar tabela hash
estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "nv", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

# Algo para armazenar o conjunto final de estações
estacoes_final = set()

# Melhor estação que cubra o maior número de estados
melhor_estacao = None
# conjunto de todos os estados que essa estação abrenge
estados_cobertos = set()
for estacao, estados_por_estacao in estacoes.items():
    # Fazendo uma intersecção
    cobertos = estados_abranger & estados_por_estacao
    if len(cobertos) > len(estados_cobertos):
        melhor_estacao = estacao
        estados_cobertos = cobertos
estacoes_final.add(melhor_estacao)
estados_abranger -= estados_cobertos

###################################################################

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados in estacoes.items():
        cobertos = estados_abranger & estados
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos
    estacoes_final.add(melhor_estacao)
