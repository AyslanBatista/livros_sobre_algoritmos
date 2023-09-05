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

#Dígrafo, as relações seguem a direção das setas
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

=A lista de pesquisa deve ser uma fila, caso contrário você não obterá o caminho mínimo

Como expressar uma relação do tipo"você->bob"?
"TABELA HASH"

Não importa em que ordem você adiciona os pares chave/valor.
Pois as tabelas hash não são ordenadas

=="""GRAFOS NÃO DIRECIONADOS"""==
um grafo não direcionado não contém setas, e as relações acontece nos dois sentidos

Pode ocorrer de adicionar duas vezes na lista a mesma pessoa
Verificá-la duas vezes será perda de tempo, Dessa forma, ao verificar uma pessoa,
você deve marcá-la como verificada para que ela não seja pesquisada novamente
Caso isso não seja feito, sua pesquisa poderá entrar em um loop infinito

cada aresta será analisada, tempo de execução O(número de arestas)
Além disso, também terá uma lista de pessoas verificadas, adicionar uma pessoa
leva um tempo constante O(1) fazer isso para cada pessoa O(número de pessoas)
a pasquisa em largura tem tempo de execução:
="O(número de pessoas + número de arestas) O(V+A)"=

===================================================** ''' CAPITULO 7 ''' **===================================================
===***'''Algoritmo de Dijkstra'''***=== # determina caminho mínimo até X para grafos ponderados
Algoritmo de Dijkstra só funciona com grafos acíclicos dirigidos
Você não pode usar o algoritmo de Disjkstra se você tiver arestas com peso negativo

1- Encontre o vértice mais "barato", aquele que tem o menor tempo possível
2- atualize o custo/valor dos vizinhos deste vértice
3- Repita até que tenha feito isso para cada vértice
4- Calcule o caminho final

Um grafo com pesos é chamado de grafo ponderado(grafo valorado)
Um grafo sem pesos é chamado de grafo não ponderado(grafo não valorado)

Ciclos indicam que é possível começar em um vértice, viajar ao redor dele e
terminar no mesmo vértice

Passos:
-faça uma tabela com custo de cada vértice, registrando o quanto você gasta em cada vértice
-você continuará atualizando esta tabela conforme o algoritmo for executado, para calcular o caminho final
-se o valor que foi atuliazado for menor, ele entrará como PAI na tabela

Este exemplo por objetivo mostrar que o caminho mínimo não precisa ser somente uma distância
física, mas que ele também envolve como reduzir algo, que nesse caso reduzir quantidade


='''Algoritmo de Bellman-Ford'''*= #Algoritmo específico para arestas com pesos negativos

===================================================** ''' CAPITULO 8 ''' **===================================================
===***'''Algoritmos gulosos'''***=== # Uma estratégia muito simples para resolver problemas
Deve escolher a que acaba mais cedo primeiro. Em termos técnicos:
a cada etapa, escolhe-se a solução ideal, e no fim você tem uma solução global ideal

Em alguns casos, tudo que vocẽ precisa é de um algoritmo que resolva o problema
de uma maneira muito boa. E ai que os algoritmos gulosos entram, pois eles são
simples de escrever e normalmente chegam bem perto da solução perfeita.

Calcular possíveis subconjunto de estações é muito longo, tempo de execução O(2n^n)
pois existem 2^n subconjunto

='''Algoritmo de aproximação'''*=
Quando é necessário muito tempo para calcular a solução exata, um algoritmo de
aproximação é uma boa ideia e funcion.
- por sua rapidez
- pela capacidade de chegar a solução ideal

==Algoritmo Exato O(n!)
==Algoritmo Guloso O(n2)

===**"""Problemas NP-Completos"""**===
Tanto o problema do caxeiro-viajante quanto ao problema da cobertura de conjuntos
têm algo em comum: Calcula-se cada solução possível e escolhe-se a menor.

É sempre bom saber se o problema que você está tentando resolver é NP-completo,
pois nesta situação você pode para de tentar resolvê-lo perfeitamente e, em vez
disso, resolvê-lo usando um algoritmo de aproximação.

A resposta simples é:
Não há uma maneira fácil de dizer se o problema em que você está trabalhando é 
NP-completo. Aqui alguns indicativos:
- Seu algortimo roda rápido para alguns itens, mas fica muito lento com o aumento de itens
- "Todas as combinações de X" geralmente significam um problema NP-completo
- Você tem de calcular "cada possível versão" de X porque não pode dividir em subproblemas menores? Talvez seja um problema NP-completo
- Se o seu problema envolve uma sequência ( como uma sequência de cidades, como o problema do caixeiro-viajante) e é dificil de resolver, pode ser um NP-completo
- Se o seu problema envolve um conjunto (como um conjunto de estações de radio) e é dificil de resolver, ele pode ser um problema NP-completo
- Você pode reescrever o seu problema como problema de cobertura mínima de conjuntos ou o problema do caixeiro-viajante? Então seu problema definitivamente é NP-completo

===================================================** ''' CAPITULO 9 ''' **===================================================
===***'''Programação dinâmica'''***=== # Técnica para resolução de problemas complexos que se baseia na divisão de problema em subproblemas

- A programação dinamica é util quando você está tentando otimizar algo em relação a um limite
- Você pode utilizar a programação dinâmica quando o problema puder ser dividido em subproblemas
- Todas as soluções em programação dinâmica envolvem uma tabela.
- Os valores nas células são, geralmente, o que você está tentando otimizar
- Cada célula é um subproblema, então pense sobre como é possível dividir este subproblema em outros subproblemas.
- Não existe uma formula unica para calcular uma solução em programação dinamica

Programção dinâmica é uma ferramenta poderosa para resolver subproblemas utilizando
respostas para resolver um problema geral. Porém a programação dinâmica só funciona
quando os seus subproblemas são discretos, ou seja, quando eles não são dependentes 
entre si.

Identificação do problema em programção dinâmica:
- A programação dinâmica é útil quando você está tentando otimizar em relação a um limite,
no problema da mochila, era necessario maximizar o valor dos itens roubados, limitados pela capacidade da mochila

- Você pode utilizar a programação dinamica quando o problema puder ser separado em subproblemas
discretos que não dependam um do outro.

-Toda solução de programação dinamica evolve uma tabela
-Os valores nas células são, geralmente, o que você está tentando otimizar, para o problema
da mochila, os valores nas celulas eram os valores dos itens
- Cada célula é um subproblema, portanto, pense em como voce pode dividi-lo em
outros subproblemas, pois isso lhe ajudará a descobrir quais são os seus eixos

===================================================** ''' CAPITULO 10 ''' **===================================================
===***'''K-vizinhos mais próximos'''***=== # Como prever um número, como estará o valor da bolsa de valores amanhã
Se você estiver tentando classificar alguma coisa, talvez seja uma boa ideia tentar usa-lo primeiro

Ao trabalhar com o algoritmo dos k-vizinhos mais próximos, é muito importante escolher as
características certas a serem comparadas, que são:
- Características diretamente correlacionadas aos filmes que você está tentando recomendar.
- Características imparciais ( se as únicas opções fornecidas aos usuários forem filmes de comédia,
esta avaliação não fornecerá nenhuma informação útil sobre o gosto dos usuários em relação a filmes de ação por exemplo.)

- Classificação = classificar em grupos
- Regressão = adivinhar uma resposta (como um número)
- O algoritmo dos k-vizinhos mais próximos é utilizado na classificação e também
na regressão, Ele envolve observar os K-vizinhos mais próximos.
- Extrair caracteristicas significa converter um item (como uma fruta ou um usuario)
em uma lista de números que podem ser comparados
- Escolher boas características é uma parte importante para que um algoritmo dos 
k-vizinhos mais próximos opere corretamente


===================================================** ''' CAPITULO 11 ''' **===================================================
===***'''Avore Binaria'''***=== 
Arvore binario de busca é rapida para inserções e remoções, em média

#         array       arvore binaria de busca
Busca   |  O(log n)  |   O(log n)
inserção|  O(n)      |   O(log n)
Remoção |  O(n)      |   O(log n)

Arvore binaria de busca tem desvantagens:
Não é possível utilizar acesso aleatório, isso faz com que seja impossível dizer:
"Me de o quinto elemento desta arvore"

Para arvores binaria de buscar tem um bom desempenho de meia, ela deve estar balanceada

As arvores B, um tipo espical de arvore binaria, são comumente usadas para armazenar dados em banco de dados.

===***'''Índices invertidos'''***=== 
Uma hash que mapeia palavras para lugares onde elas aparecem. Esa estrutura é muito
usada na contrução de ferramentas de busca

===***'''A transformada de Fourier'''***=== 
Usada no funcionamento do formato MP3:
Primeiro a música é separada em suas notas individuais. Então a transformada de Fourier
informa o quanto exatamente cada nota contruibui para a música como um todo. Sabendo disso
é possível eliminar notas que não são importante para a música.

===***'''Algoritmos paralelos'''***=== 
Se você tem dois núcloes no seu notebook em vez de somente um, isso quase nunca
significa que seu algoritmo será duas vezes mais rápido. Motivos:
- Gerenciamento do paralelismo - Imagine que você deve ordenar um array de 1.000 itens.
Como vocẽ divide esta tarefa entre dois núcleos? Você fornece 500 itens para cada núcleo
ordenar e então une ambos os arrays ordenados em um grande array? Unir os arrays leva tempo

- Balanceamento de carga - Suponha que você tenha dez tarefas que devam ser executadas e,
portanto cada núcleo receba cinco tarefas. Porém o núcleo A recebe todas as tarefas simples
e as finaliza em dez segundos, enquanto o núcleo B recebe todas as tarefas complexas e leva um minuto.
Ou seja, o núcleo A ficou parado durante cinquenta segundos enquanto o núcleo B esteve fazendo
todo o trabalho duro!

===***'''MapReduce'''***=== 
Algoritmo distribuido popular que pode ser usado no framework livre Apache Hadoop
O MapReduce é baseado em duas ideia simples: a função map (mapa) e a função reduce (reduzir)

===***'''Função map'''***=== 
A função map é muito simples, ela pega um array e aplica a mesma função para cada item no array

Não seria ótimo ter cem máquinas, sabendo que a função map poderia dividir automaticamente
as tarefas entre todas elas? Desta forma você estaria baixando cem páginas ao mesmo tempo e o trabalho
estaria acabado muito antes! Esta é a ideia por trás da função "map" do MapReduce

===***'''Função reduce'''***=== 
Ideia central desta função é "reduzir" uma lista inteira para apenas um item
com a função reduce, você transforma um array em um simples item.

===***'''Filtro de Bloom'''***=== 
São estruturas de dados probabilisticos que fornecem uma resposta que pode estar errada,
mas que provalvelmente estará correta.
Em vez de perguntar a uma hash, é possível perguntar a um filtro de bloom, se a
URL já foi rastreada antes.

- Falsos positivos são possíveis.
- Falsos negativos não são possíveis.

===***'''HyperLogLog'''***=== 
Ele aproxima o número de elementos únicos em um conjunto. Assim como o filtro de bloom,
ele não fornecerá uma resposta exata, mas se aproximará muito desta, usando apenas uma 
fração da memória de que a tarefa necessitaria se fosse implementada de maneira tradicional

===***'''Algortimos SHA'''***=== 
é uma função hash, ele gera um hash, que é apenas uma string curta
Faz a ligação entre string e string

Muito utilizado para fazer comparação de senhas, ao utilizar apenas a ligação feita pelas string hash

===***'''Prorgamação linear'''***=== 
Programação linear é usada para maximizar algo em relação a um limite

Todos os algoritmos de grafos podem ser feitos por meio de programação linear
Programção linear é um framework muito mais geral, enquanto o problema de grafos 
é apenas um subconjunto dela.

