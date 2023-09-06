"""
Galinha, Cachorro e Raposa

Não podem ficar sozinhos:
Raposa e Cachorro
Raposa e Galinha
"""

Margem_inicio = ["Raposa", "Cachorro", "Galinha"]
Caminho = []
Margem_destino = []

# Pego a Raposa e levo ela até a margem destino
Margem_inicio = ["Cachorro", "Galinha"]
Caminho = ["Raposa"]
Margem_destino = ["Raposa"]

# Volto sozinho até a margem do inicio
Margem_inicio = ["Cachorro", "Galinha"]
Caminho = []
Margem_destino = ["Raposa"]

# Pego a galinha e levo ela até a margem destino
Margem_inicio = ["Cachorro"]
Caminho = ["Galinha"]
Margem_destino = ["Raposa", "Galinha"]

# Para não deixar os dois sozinhos, volto com a raposa para o inicio
Margem_inicio = ["Cachorro", "Raposa"]
Caminho = ["Raposa"]
Margem_destino = ["Galinha"]

# Pego o cachorro e levo ele na margem destino
Margem_inicio = ["Raposa"]
Caminho = ["Cachorro"]
Margem_destino = ["Cachorro", "Galinha"]

# Volto Sozinho para pegar a raposa
Margem_inicio = ["Raposa"]
Caminho = []
Margem_destino = ["Cachorro", "Galinha"]

# Agora levo a raposa para margem destino
Margem_inicio = []
Caminho = ["Raposa"]
Margem_destino = ["Cachorro", "Galinha", "Raposa"]
