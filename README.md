# 📚 Estruturas de Dados
As estruturas de dados representam um conjunto de dados armazenados na memória. Esse conjunto precisa ser organizado de forma eficiente para oferecer uma melhor manipulação dos dados armazenados, o que tende a otimizar processos e operaçoes. A manipulação dessas estruturas através de declarações e instruções definem a parte dinâmica de um algoritmo, e o conjunto de estruturas de dados constituem formalmente um algoritmo para a resolução de problemas.

Estruturas de dados podem ser ***Lineares*** e ***Não-Lineares***.


# 📚 Tipos Abstratos de Dados
Um Tipo de Dado Abstrato (TAD) estabelece o conceito de tipo de dado separado da sua representação. Ou seja, requer que operações sejam definidas sobre os dados sem estarem atreladas a uma representação específica.

### Para definir um TAD
O programador descreve o TAD em dois módulos separados:
- Um módulo contém a definicação do TAD, onde encontra-se a representação da estrutura de dados e implementação de cada operação suportada;
- O outro módulo contém a interface de cada operação suportada.

Desta forma, outros programadores podem, por meio da interface de acesso, utilizar o TAD sem precisar conhecer os detalhes representacionais e sem acessar o módulo de definição.

Além disso, os módulos (ou units) são instalados em uma biblioteca e podem ser reutilizados por diversos programas. 

Portanto, a característica essencial de TAD é a separação entre a definição conceitual de um par de conjunto de valores com o conjunto de operações sobre esses valores, e a implementação com uma estrutura de dados específica.

Logo, uma estrutura de dados pode ser vista, então, como uma implementação de um TAD.

### Vantagens do uso de TAD
- Reuso: uma vez definido, implementado e testado, o TAD pode ser acessado por diferentes programas;
- Manutenção: mudanças na implementação do TAD não afetam o código fonte dos programas que o utilizam;
- Correção: o TAD é testado e funciona corretamente.
