# Comparativo de Paradigmas: Programação Dinâmica vs. Algoritmo Guloso

---

## Programação Dinâmica

* **Conceito:** Resolve problemas complexos quebrando-os em subproblemas menores, armazenando a solução de cada subproblema para evitar recálculos e garantir a otimalidade global.
* **Tipos de Aplicações:** Problemas de otimização (encontrar o mínimo ou máximo), contagem de combinações e problemas onde a solução depende de soluções de etapas anteriores.
* **Quando é Aplicável:** Exclusivamente quando o problema possui **subestrutura ótima** (a solução ótima para o problema principal contém soluções ótimas para os subproblemas) e **subproblemas sobrepostos** (os mesmos subproblemas são resolvidos múltiplas vezes).
* **Vantagens:** Garante a **solução ótima** para o problema. É muito eficiente por evitar o recálculo de soluções já conhecidas (memoização).
* **Desvantagens:** Geralmente consome **mais memória** para armazenar a tabela de soluções dos subproblemas. Pode ser mais complexo de conceber a recorrência e a implementação.
* **Problemas Clássicos:**
    * Problema da Mochila (0/1 Knapsack Problem)
    * Problema da Linha de Montagem
    * Sequência Comum Mais Longa (LCS)
    * Multiplicação de Cadeia de Matrizes
* **Comentários Adicionais:** A programação dinâmica é exaustiva; ela explora todas as possibilidades (de forma inteligente) para garantir que a melhor solução seja encontrada. É uma abordagem "de baixo para cima" (bottom-up) ou "de cima para baixo" (top-down com memoização).

---

## Algoritmo Guloso

* **Conceito:** Toma a decisão que parece ser a melhor no momento atual (uma escolha localmente ótima), na esperança de que essa sequência de escolhas leve a uma solução globalmente ótima.
* **Tipos de Aplicações:** Problemas de otimização, agendamento de tarefas, construção de árvores geradoras mínimas e busca de caminhos mais curtos.
* **Quando é Aplicável:** Quando o problema possui a **propriedade da escolha gulosa**, ou seja, uma escolha localmente ótima sempre fará parte de uma solução globalmente ótima. Também requer subestrutura ótima, mas não necessariamente subproblemas sobrepostos.
* **Vantagens:** Geralmente **mais rápido** e mais **simples de implementar** do que a programação dinâmica. Requer menos memória.
* **Desvantagens:** **Não garante a solução ótima** para todos os problemas. Uma escolha que parece boa agora pode levar a uma solução final ruim.
* **Problemas Clássicos:**
    * Problema do Troco (para certos sistemas de moedas)
    * Algoritmo de Dijkstra (caminho mais curto)
    * Algoritmo de Kruskal e Prim (Árvore Geradora Mínima)
    * Código de Huffman (compressão de dados)
* **Comentários Adicionais:** A abordagem gulosa é "míope". Ela se compromete com uma escolha em cada passo e nunca a reconsidera. Se a propriedade da escolha gulosa for válida para o problema, o algoritmo será ótimo e muito eficiente.