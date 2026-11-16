# Trabalho P2 — Algoritmos de Ordenacao em Python

Repositorio com os nove algoritmos: Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix e Bucket Sort.

## Teste com 100.000 elementos

O arquivo `teste_100000.py` gera exatamente **100.000 inteiros aleatorios**, incluindo negativos e repetidos. Cada algoritmo recebe uma copia da mesma lista, e o resultado e conferido com `sorted()`. O tempo e medido por `time.perf_counter()`.

No terminal desta pasta:

```bash
python teste_100000.py
```

Por padrao, roda os seis algoritmos mais adequados para 100.000 elementos: Merge, Quick, Heap, Counting, Radix e Bucket.

Para testar um algoritmo especifico com 100.000 elementos:

```bash
python teste_100000.py radix_sort
python teste_100000.py bubble_sort
```

Para testar os nove com 100.000 elementos (pode demorar muito):

```bash
python teste_100000.py todos
```

Para ensaiar os nove rapidamente, com uma entrada menor:

```bash
python teste_100000.py todos --tamanho 1000
```

**Importante:** Bubble, Selection e Insertion Sort possuem tempo quadratico `O(n²)` no caso medio e podem demorar muitos minutos com 100.000 elementos. O parametro `--tamanho 1000` serve apenas para ensaio, nao substitui o teste de 100.000.

Os nove arquivos mantem a mesma implementacao e os exemplos originais, agora protegidos com `if __name__ == "__main__":`, para que nao sejam executados ao importar as funcoes.

Nao requer bibliotecas externas.
