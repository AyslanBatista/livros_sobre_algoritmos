grafo = {}
grafo["inicio"] = {}

grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}  # O vértice final não tem vizinhos

print(grafo)

#######################################################
# Tempo necessário para chegar até o final
# este tempo é considerado infinito
infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

########################################################
# Tabelha hash para os pais
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

# Array para manter registro de todos os vértices processados
processador = []
