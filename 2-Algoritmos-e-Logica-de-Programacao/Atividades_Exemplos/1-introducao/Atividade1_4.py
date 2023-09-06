"""
Três garrafas com fomatos diferentes
Uma Cheia até a boca, capacidade de 8 litros
outras duas vazias, capacidade de 5 e 3 litros

Deseja separa o conteúdo da primeira garrafa em duas quantidades iguais
Realizar a tarefa sem fazer medidas.
"""

garrafa_8_litros = 8
garrafa_5_litros = 0
garrafa_3_litros = 0
print(garrafa_8_litros, garrafa_5_litros, garrafa_3_litros)
# Primeiro passo será encher a garrafa de 5 LT, utilizando a garrafa de 8 LT
garrafa_8_litros -= 5
garrafa_5_litros += 5
print(garrafa_8_litros, garrafa_5_litros, garrafa_3_litros)

# Segundo passo será encher a garrafa de 3 LT, utilizando a garrafa de 5 LT
garrafa_5_litros -= 3
garrafa_3_litros += 3
print(garrafa_8_litros, garrafa_5_litros, garrafa_3_litros)


# Temos 2 garrafas com a mesma quantidade
print(garrafa_8_litros, garrafa_3_litros)
