----------------------------- '''ALGORITMOS E LÓGICA DE PROGRAMAÇÃO''' ------------------------------------

===================================================** ''' CAPITULO 1 ''' **===================================================

===***'''Desenvolvimento de um Software'''***===
Diferença entre dado e informação:
- Dados por si só é um valor qualquer armazenado em um computador
- informação representa a interpretação desse dado, ou seja, qual o seu significado

=*'Processo de Desenvolvimento de um Software'*=
1º Definição de requisistos
2º Desenvolvimento
3º Entrega

Tipica divido nas seguintes etapas:
- Análise: Criam-se especificações que detalham como o software vai funcionar;
- Projeto: Criam-se especificações que detalham o resultado da Análise em termos mais próximos da implementação do software.
- implementação: Utilizando-se uma linguagem de programção e as especificações de projeto, o software é construído;
- Testes: Após a construção do software, são realizados testes para conferir sua conformidade com os requisitos inciais. O software deve satisfazer a todas as especificações do cliente

=*'Significado de um Algoritmo'*=
Um algortimo representa um conjunto de regras para a solução de um problema. Essa é uma Definição geral.

algortimo especifica com clareza e de forma correta as intruções que um software deverá conter para que,
ao ser executado, forneça resultados esperados.

Modelagem do problema é resultante de um processo mental de abstração - Modelagem do problema:
Extrair todas as informações a respeito desse problema (dados e operações) e relacioná-las com o conhecimento atual que se tem do assunto.

Regras de sintaxe:
Necessário definir um conjunto de regras que regulem a escrita do algoritmo.

Semânticas:
É preciso estabelecer as regras que permitam interpretar um algortimo.

=*'Sintaxe de um Algortimo'*=
Tipos de comandos de um algoritmo são também denominados estruturas de programação.

Existem apenas trÇes tipos de estruturas que podem ser utilizadas para escrever qualquer programa:
1º Estruturas sequenciais
2º De Decisão
3º De Repetição

Manipulação desses dados é feita por meio de variáveis e valores constantes.
Para escrever as expressões corretamente, é necessario também uma sintaxe,
essa sintaxe depende do tipo de variáveis envolvidas e determina quais são os operadores que podem ser aplicados.
Além dos operadores propriamente ditos, especificam-se algumas funções e procedimentos predefinidos úteis.

Importância de formalização de um algoritmo, sua sintaxe e semântica resumidas em:
1- Envitar ambiguidades, pois definem regras sintáticas e semânticas que sempre são interpretadas da mesma forma
2- Impedir a criação de símbolos ou comandos desnecessários na criação de um algoritmo: representam um conjunto
mínimo de regras que pode ser utilizado em qualquer algoritmo.
3- Permitir uma aproximação com as regras de uma linguagem de programação, fazendo, assim, uma fácil tradução
de um algortimo para sua implementação no computador

O papel da lógica em programação de computadores está relacionado com a correta sequência de instruções que
devem ser definidas para que o programa atinja seu objetivo

=*'Como se portar em um curso de computação'*=
É um erro decorar as soluções em computação, pois podem não servir para outros problemas, que com certeza
serão diferentes. O que deve ser procurado é o entendimento de como foi obtida uma solução, e armazená-la na memória
e então utilizar essa experiência adptando-a em outras situações, por analogia, generalização e especialização.

1- O que se deve descobrir ou calcular? Qual é o objetivo?
2- QUais são os dados disponiveis? São suficientes?
3- Quais as condições ncessárias e suficientes para resolver o problema?
4- Faça um esboço informal de como ligar os dados com as condições
5- Se possível, modele o problema de forma matemática
6- Consulte sua memória e verifique se você já resolveu algum problema similar
7- Verifique se é necessario introduzir algum elemento novo no problema, como um problema auxiliar
8- Se o problema for muito complicado, tente quebrá-lo em partes menores e solucionar essas partes
9- Tente enxergar de outra forma de modo que o entendimento se torne mais simples

Otimização:
1- É possível melhorar o algoritmo?
2- É possível reduzir o número de passos ou dados?
3- É Possível conseguir uma solução ótima?


===================================================** ''' CAPITULO 2 ''' **===================================================
===***'''Conceitos de Computação e Computadores'''***===

==*'Maquina analítica'*== # A maquina foi descrita pela primeira vez em 1837
inha como princípio básico a programação: Utilizando o conceito de cartões perfurados de Jacquard,
a máquina seria alimentada com cartões contendo intruções e dados que seriam, então, processados por ela.

Foi com esse projeto que Charles Babbage(1791 1871) ficou conhecido como o pai da computação

Ada augusta(1815 1852) - Primeira programadora 
Ada augusta King, a condessa de Lovelace, além de ter traduzido o projeto conceitual da máquina
para a língua inglesa, propôs programas de exemplo e ainda discutiu técnicas de programação para aquela máquina

George Boole foi o contribuidor de caráter matemático, desenvolvendo um sistema de lógica simbólica e de
raciocínio em 1854. a lógica booleana, como ficou conhecida, e até hoje usada para projeto de circuitos
digitais utilizados no computadores.

Chegando próximo ao século XX, em 1890, o norte-americano Hermann Hollerith projetou um equipamento para auxiliar
na realização do censo  daquele ano. A máquina, chamada tabulador eletromecânico, processava automaticamente cartões perfurados.

==*'Primeira Geração - Computadores e válvula e Relé'*==
Os primeiros computadores eletrônicos começam a surgir na década de 1930.  Entre 1935 e 1938, Konrad Zuse,
em Berlim, projetou e construiu uma série  de máquinas eletromecânicas baseadas em relés.

relés. Relé é um dispositivo que,  se excitado por uma corrente elétrica, é capaz de fechar um contato,
servindo  assim como uma chave “liga-desliga”.


Nessa época, uma grande contribuição teórica foi dada pelo matemático  inglês Alan Turing. Ele definiu o conceito
intitulado Máquina Universal de Turing, estabelecendo um dispositivo teórico capaz de executar qualquer algoritmo descrito,
definindo assim as bases para o estudo da computabilidade: um  algoritmo computável é aquele que pode ser executado por uma máquina de  Turing. 

Nos Estados Unidos, destaca-se nesse período o computador eletromecânico Harvard Mark-1 de 1944,
concebido por Howard Aiken e implementado pela IBM como ASCC 

Um projeto secreto de computador denominado Colossus foi desenvolvido entre 1940 e 1944 com
o intuito de auxiliar na  quebra de códigos da máquina alemã Enigma e foi revelado somente em 1970. 

Essa arquitetura dividia o computador em unidade central de processamento, memória principal e dispositivos
de entrada e saída, e ficou conhecida  como arquitetura de Von Neumann,

microprocessador mais poderoso, o 8008,  de 1972. Foi com esse microprocessador que surgiu o primeiro
microcomputador do mundo, na França, o Micral, de 1973, que não obteve êxito.
O Micral  era programado diretamente com números binários, não possuindo nenhum  periférico de entrada
ou saída. As versões posteriores contavam com um software montador (assembler) desenvolvido por Philippe Kahn,

==*'A Representação da informação em um computador'*==

manipulação de números binários são similares aos dos números decimais.
Aplica-se o mesmo conceito do sistema decimal, em que a posiçãoção de cada dígito de um número
representa a potência da base.

número binário 10101 base 2 corresponde ao número decimal  21 base 10. De forma semelhante, pode-se converter
um número decimal em binário  dividindo esse número sucessivamente por dois até que o quociente seja zero. 

Os múltiplos do byte também são utilizados para representar as quantidades manipuladas e,
geralmente, são o quilobyte (KB), o  megabyte (MB) e o gigabyte (GB).

original é a ASCII estendida, que possui 256 elementos e cada elemento ainda  ocupa um byte.


==*'O Projeto Lógico Na Construção de Programas'*==

Um programa é, para o computador, um conjunto de instruções de máquina armazenadas na memória.
Porém, normalmente essas instruções são  geradas indiretamente, via arquivo de texto contendo
essas mesmas instru-  ções em código de montagem (assembly), que são instruções mnemônicas,
como ADD, MOV e outras mais fáceis de lembrar que simples sequências de  zeros e uns.

Uma linguagem de montagem não é produtiva  no sentido de criar programas em tempo hábil.
Seu uso é destinado principalmente à programação de software de sistema (sistema operacional, por exemplo)
e de softwares que operarão em tempo real, tais como drivers de vídeo,  sistemas de controle industrial e outros.

===================================================** ''' CAPITULO 3 ''' **===================================================
===***'''Revisão do conceito de algoritmo'''***===

Processo de cálculo, ou de resolução  de um grupo de problemas semelhantes, em que se estipulam,
com generalidade e sem restrições, regras formais para a  obtenção do resultado, ou da solução do problema.

Existem diversas maneiras de formalizar a representação de um algoritmo. Entre as diversas formas de representação
de um algoritmo, este livro foca  principalmente o Diagrama de Blocos e o Português Estruturado.

===***'''Diagrama de Blocos - Fluxogramas'''***===
Diagrama para representação de  um algoritmo. 
2. Representação gráfica, por símbolos especiais, da definição,
análise ou método de solução de um problema.

Os símbolos que denotam o início e o fim de um fluxograma são representados por “retângulos arredondados”,
conhecidos como terminadores, contendo,  respectivamente, os textos Início e Fim.


