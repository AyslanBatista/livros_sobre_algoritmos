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
Recursão é quando uma função chama a si mesma

Estratégia de dividir para conquistar, separar problema em caso-base e caso recursivo
É usada para tornar a resposta mais clara. Não há nenhum benefício quanto ao desempenho ao utilizar a recursão
Os loops podem melhorar o desempenho do seu programa. A recusão melhora o desempenho do seu programador. Escolha o que for mais importante para a sua situação

Toda função recursiva tem duas parte: o caso-base e o caso recursivo
caso recursivo é quando a função chama a si mesma
caso base é quando a função não chama a si mesmo novamente, de forma que o programa não se torna um loop infinito

Pilha tem duas operações push e pop
todas as chamadas de função vão para a pilha de chamada
Usar pilha é bom, porém, existe um custo: salvar toda essa informação pode ocupar muita memória
cada uma destas funções de chamada ocupa um pouco de memória.
e quando sua pilha está muito chea é sinal de que seu computador está salvando informação para muitas chamadas de funções
Opções:
- Reescrever seu código utilizando loops
- Utilizar o que chamamos de tail recursion(recursão de cauda)

Todas as chamadas de função vão para a pilha de chamada.
A pilha de chamada pode ficar muito grande e ocupar muita memória

===================================================** ''' CAPITULO 4 ''' **===================================================
===***'''Técnica DC - Quicksort'''***===
Algoritmo de ordenação elegante que é utilizado com frequência, Este algoritmo utiliza a técnica de dividir para conquistar.
Este algoritmo é muito mais rápido do que a ordenação por seleção e é muito utilizado na pratica.

-1 Descubra o caso-base, que deve ser o caso mais simples possível
-2 Divida ou diminua o seu problema até que ele se torne o caso-base

Quando estiver escrevendo uma função de recursão que envolva um array, o caso-base será, muitas vezes
um array vazio ou um array com apenas um elemento

--Array 3 elementos--
Caso-base do quicksort consegue ordenar arrays de dois elementos (o subarray esquerdo) e também arrays vazios (o subarray direito)
Assim, se utilizar o quicksort em ambos os subarrays e então combinar os resultados, terá um array ordenado!
quicksort([15,10]) + [33] + quicksort([])
>[10,15,33]

Quicksort tem tempo de execução médio O('n' log 'n') na pior situação, o quicksort tem tempo de execução O(n²)
tem uma constante menor do que o merge sort. Assim, como ambos têm tempo de execução O('n' log 'n'), o quicksort
acaba sendo mais rápido, na prática, ele funciona mais vezes no caso médio do que no pior caso.

Desempenho do quicksort depende bastante da escolha do pivô
Com o primeiro elemento sendo o pivô, você não está dividindo o array em duas metades. Em vez disso, um dos subarrays está
sempre vazio, o que faz com que a pilha de chamada seja sempre muito longa.
Agora, imagine que você sempre escolha o elemento central do array como pivô. Perceba como a pilha de chamada é menor

O peso da pilha de chamada [ou pilha de execução] é O(log 'n'). Cada nível tem tempo de execução O('n')
algoritmo como um todo tem o tempo de execução O('n')*O(log 'n') = O('n' log 'n')  Este é o melhor caso

Pior caso existem O('n') níveis. Portanto o algoritmo tem tempo de execução O('n') * O('n') = O(n²)

Se você estiver implementando o quicksort, escolha um elemento aleatório como o pivô. O tempo de execução médio do quicksort é O('n' log 'n')


===================================================** ''' CAPITULO 5 ''' **===================================================
===***'''Tabelas Hash'''***=== # mapas hash, mapas, dicionários e tabelas de dispersão
Uma função hash é uma função na qual você insere uma string e, depois disso, a função retorna um número
Função Hash "mapeia strings e números"

A função Hash mapeia consistentemente um nome para o mesmo índice, mapeia diferentes strings para diferentes índices.
Ela tem o conhecimento sobre o tamanho do seu array e retornará apenas índices válidos

Tabela Hash é a primeira estrutura de dados que tem uma lógica adicional aliada
Elas usam uma função hash para indicar, de maneira inteligente, onde armazenar os elementos.

Mapear o endereço de um website para um endereço IP, esse caso é perfeito para utilização de tabelas hash
Este processo é chamado de resolução DNS, e as tabelas hash são uma das maneiras pelas quais esta funcionalidade pode ser implementada

Tabela hash informa instantaneamente se o nome da pessoa está ou não na lista.
Logo, a checagem por duplicatas é realizada muito rapidamente com o uso de uma tabela hash

--Utilizando Tabelas hash como cache--
Caching:
Você recebe a página da web muito mais rapidamente, de forma memorizada, respondendo instantaneamente.
Isso faz com que haja menos trabalho

As tabelas hash são úteis para 
- Modelar relações entre dois itens
- Filtrar por duplicatas
- Caching/memorização de dados, em vez de solicitar estes dados do servidor.

===***'''COLISÕES E DESEMPENHO'''***===
# Colisão são quando duas chaves são indicadas para o mesmo espaço
- Tempo constante não é algo que acontece instantaneamente, mas sim um tempo que continuará
sempre o mesmo, independentemente de quão grande a tabela hash possa ficar

#       Caso Medio  Pior Caso
Procura |  O(1)  |   O(n)
inserção|  O(1)  |   O(n)
Remoção |  O(1)  |   O(n)

Para evitar colisões são necessários:
- um baixo fator de carga
- uma boa função Hash 

=="FATOR CARGA"
100 espaços, se os 100 espaços estão preenchidos o fator carga é 1
50 espaços, se tivesse 100 itens, o fator de carga é 2, pois não existem espaços suficientes

Fator maior que 1, indica que você não tem mais espações em seu array

Quando precisa adicionar mais espaços em sua tabelha hash, se chama "redimensionamento"
Uma boa regra geral é: redimensione quando o fator de carga for maior do que 0,7
Boa função hash distribui os valores no array simetricamente

===================================================** ''' CAPITULO 6 ''' **===================================================
===***'''Pesquisa em Largura'''***=== # Permite encontrar o menor caminho entre dois objetos
# Push e Pop
1- Modelo o problema utilizando grafos
2- Resolva o problema utilizando a pesquisa em largura

#GRAFOS
Vértice    aresta
 ______             ______ 
| ALEX | _________>| RAMA |
 _______           _______ 

Grafos são formados por vértices(CIRCULOS) e arestas(SETAS), e um vértice pode ser diretamente concetado a muitos outros vértices.
São maneira de modelar como eventos diferentes estão conectados entre si

Este algortmo ajuda a responder a dois tipos de pergunta:
1- Existe algum caminho do vértice A até o vértice B?(Existe um vendedor de manga na minha rede?)
2- Qual o caminho mínimo do vértice A até o vértice B?(Quem é o vendedor de manga mais próximo?)

Estrutura de dados específica: FILA(Função similar aos das pilhas)
Não é possível acessar elementos aleatórios em uma fila.
Duas operações são possíveis
(enfileirar) e (desenfilerar)

Pilha = LIFO (Ultimo a entrar, primeiro a sair)
Fila = FIFO (Primeiro a entrar, primeiro a sair)

Como expressar uma relação do tipo"você->bob"?
"TABELA HASH"

Não importa em que ordem você adiciona os pares chave/valor.
Pois as tabelas hash não são ordenadas

um grafo não direcionado (ou simplesmente grafo) não contém setas

Pode ocorrer de adicionar duas vezes na lista a mesma pessoa
Verificá-la duas vezes será perda de tempo, Dessa forma, ao verificar uma pessoa,
você deve marcá-la como verificada para que ela não seja pesquisada novamente
Caso isso não seja feito, sua pesquisa poderá entrar em um loop infinito

cada aresta será analisada, tempo de execução O(número de arestas)
Além disso, também terá uma lista de pessoas verificadas, adicionar uma pessoa
leva um tempo constante O(1) fazer isso para cada pessoa O(número de pessoas)
a pasquisa em largura tem tempo de execução:
="O(número de pessoas + número de arestas) O(V+A)"=

