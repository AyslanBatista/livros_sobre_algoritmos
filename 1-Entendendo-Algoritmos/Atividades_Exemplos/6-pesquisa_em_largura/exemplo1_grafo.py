grafo = {}

grafo["voce"] = ["alice", "bob", "claire"]
# Note que "voce" é mapeado para um vetor.
# Logo grafo["voce"] lhe dará um vetor de todos os vizinho de "voce"

grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []
