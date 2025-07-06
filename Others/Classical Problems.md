# Resumo Comparativo de Algoritmos

---

### 1. Programação Dinâmica para Linhas de Montagem

* **Paradigma:** Programação Dinâmica.
* **Problema:** Encontrar o caminho mais rápido (de menor custo) para montar um produto passando por uma de duas linhas de montagem paralelas.
* **Aplicabilidade:** Usado em problemas de otimização onde a solução ótima pode ser construída a partir de soluções ótimas de subproblemas, como planejamento de produção e otimização de rotas sequenciais.
* **Vantagens:** Garante a solução ótima global, evitando a armadilha de decisões "gulosas" que parecem boas a curto prazo, mas não são as melhores no final.
* **Desvantagens:** Requer mais memória para armazenar os resultados dos subproblemas em tabelas. Pode ser mais complexo de implementar do que uma abordagem gulosa.
* **Complexidade:** **$\Theta(n)$**, onde *n* é o número de estações. É linear e muito eficiente.
* **Comentários:** É um exemplo clássico para demonstrar a diferença entre programação dinâmica (que resolve todos os os subproblemas) e algoritmos gulosos (que fazem uma escolha local ótima).

---

### 2. Código de Huffman (Huffman Coding)

* **Paradigma:** Algoritmo Guloso.
* **Problema:** Criar um código de prefixo ótimo (sem que o código de um caractere seja o início do código de outro) para compressão de dados, onde os caracteres mais frequentes recebem os códigos binários mais curtos.
* **Aplicabilidade:** Ideal para compressão de dados sem perdas. É a base para formatos de compressão como **JPEG**, **MP3** e **ZIP**.
* **Vantagens:** Produz um código de prefixo ótimo, garantindo a melhor taxa de compressão possível para um dado conjunto de frequências. É conceitualmente simples e eficiente.
* **Desvantagens:** Requer duas passadas sobre os dados: uma para calcular as frequências e outra para a compressão real. A tabela de frequências (ou a árvore de Huffman) precisa ser armazenada junto com os dados comprimidos, o que pode anular a compressão para arquivos muito pequenos.
* **Complexidade:** **$O(n \log n)$**, onde *n* é o número de caracteres únicos. A ordenação inicial dos nós ou o uso de uma fila de prioridade domina a complexidade.
* **Comentários:** A escolha gulosa é construir a árvore binária combinando sempre os dois nós (caracteres ou sub-árvores) de menor frequência. 🌳

---

### 3. Algoritmo de Kruskal

* **Paradigma:** Algoritmo Guloso.
* **Problema:** Encontrar uma **Árvore Geradora Mínima (MST)** em um grafo conectado e não direcionado, ou seja, um subconjunto de arestas que conecta todos os vértices sem formar ciclos e com o menor custo total possível.
* **Aplicabilidade:** Usado no projeto de redes, como redes de computadores, elétricas ou de telecomunicações, para conectar todos os pontos com o mínimo de cabo ou custo.
* **Vantagens:** Relativamente fácil de entender e implementar. Sua eficiência depende da estrutura de dados usada para detectar ciclos (Union-Find), que é extremamente rápida na prática.
* **Desvantagens:** Precisa de todas as arestas ordenadas por peso, o que pode ser um gargalo para grafos muito grandes.
* **Complexidade:** **$O(E \log E)$** ou **$O(E \log V)$**, onde *E* são as arestas e *V* são os vértices. A complexidade é dominada pela ordenação das arestas.
* **Comentários:** Sua estratégia gulosa é simples: sempre adicione a próxima aresta de menor peso que **não** forma um ciclo com as arestas já selecionadas.

---

### 4. Algoritmo de Dijkstra

* **Paradigma:** Algoritmo Guloso.
* **Problema:** Encontrar o caminho mais curto de um único vértice de origem para todos os outros vértices em um grafo ponderado onde os pesos das arestas são **não negativos**.
* **Aplicabilidade:** Fundamental em protocolos de roteamento de redes (como OSPF), sistemas de GPS e qualquer problema de busca de caminho mais curto em grafos sem custos negativos. 🗺️
* **Vantagens:** Muito eficiente para encontrar o caminho mais curto em seu domínio de aplicação. É a base para muitos outros algoritmos mais complexos.
* **Desvantagens:** **Não funciona corretamente se o grafo tiver arestas com pesos negativos**. Essa é sua principal limitação.
* **Complexidade:** **$O(E \log V)$** com o uso de uma fila de prioridade (heap binário), que é a implementação padrão.
* **Comentários:** A escolha gulosa é sempre explorar o próximo vértice não visitado que está mais próximo da origem.