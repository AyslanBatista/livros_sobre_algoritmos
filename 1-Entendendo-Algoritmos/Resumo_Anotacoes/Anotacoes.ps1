----------------------------- '''ENTENDENDO ALGORITMOS''' ------------------------------------

===================================================** ''' CAPITULO 1 ''' **===================================================
- A Pesquisa binária é muito mais rápida do que a pesquisa simples.
- O(log n) é mais rápido do que O(n), e O(log n) fica ainda mais rápido conforme os elementos da lista aumentam.
- A rapidez de um algoritmo não é medida em segundos
- O tempo de execução de um algoritmo é medido por meio de seu crescimento.
- O tempo de execução dos algoritmos é expresso na notação Big O


===***'''Pesquisa Binária'''***===
-Pesquisa binária só funciona quando a sua lista está ordenada-

A pesquisa binária é executada com tempo "logarítmico" O(log'n')
100 números igual 100 tentativas, isso é chamado de tempo linear o('n')

Para uma lista de n números
A pesquisa binária precisa de log2'N' para retornar o valor correto.
Enquanto a pesquisa simples precisa de 'N' etapas

Big 'O' levamos em conta que log sempre significa log2

===***'''Alguns Exemplos comuns de tempo de execução BIG O'''***===
-Ordenados do mais rápido para o mais lento-

.(log'n') também conhecido como tempo logarítmico. Exemplo: pesquisa binária
.O('n') conhecido como tempo linear. Exemplo: pesquisa Binária
.O('n'* log 'n') Exemplo: um algoritmo rápido de ordenação, como a ordenação por seleção
.O('n'^2) Exemplo: um algoritmo lento de ordenação, como a ordenação por seleção
.O('n'!) Exemplo: um algoritmo bastante lento, como o do caixeiro-viajante

===================================================** ''' CAPITULO 2 ''' **===================================================
O(n) = TEMPO DE EXECUÇÃO LINEAR
O(1) = TEMPO DE EXECUÇÃO CONSTANTE

===***'''ARRAYS'''***===
=====LEITURA: O(1)  INSERÇÂO: O(n)  ELIMINAÇÂO: O(n)========

Arryas são ótimos se você deseja ler elementos aleatórios
Você sabe o endereço de cada item na memoria
Adicionar novos itens a um array será muito lento. Uma maneira fácil de resolver isso é "reservando lugares"

Você pode não precisar dos espaços extras que reservou, então a memória será desperdiçada. Você não está utilizando a memória, mas ninguém mais pode usá-la também
você pode precisar adicionar mais de dez itens a sua lista de tarefas, então você terá de mover seus itens de qualquer maneira.

===***'''LISTAS ENCADEADAS'''***===
=====LEITURA: (n)  INSERÇÂO: O(1)  ELIMINAÇÂO: O(1)========

Na lista encadeada os elementos não estão próximos uns dos outros, Listas só podem lidar com acesso sequencial
Adicionar um item a uma lista encadeada é facíl: você o coloca em qualquer lugar da memória e armazena o endereço do item anterior
Com as listas encadeadas você nunca precisa mover os seus itens
Lista são melhores para inserir itens no meio da lista

Listas encadeadas são ótimas se você quiser ler todos os itens, um de cada vez, você pode ler um item, seguir para o endereço do próximo item
e fazer isso até o fim da lista. Mas se você quiser pular de um item para outro, as listas encadeadas são terríveis.

===***'''ORDENAR POR SELEÇÃO'''***===
Você precisa verificar cada item da lista. Isso tem tempo de execução O(n)
Então você tem uma operação com tempo de execução O(n) e precisa repetir essa operação 'n' vezes
Tempo de execução O(nxn) ou O(n²)

===================================================** ''' CAPITULO 3 ''' **===================================================
===***'''RECURSÃO'''***===
É usada para tornar a resposta mais clara. Não há nenhum benefício quanto ao desempenho ao utilizar a recursão
Os loops podem melhorar o desempenho do seu programa. A recusão melhora o desempenho do seu programador. Escolha o que for mais importante para a sua situação


