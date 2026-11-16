import random
import time

# Vantagem: ordena inteiros em O(n + k), sendo k o intervalo de valores.
# Desvantagem: usa O(k) de memoria e nao serve para qualquer tipo de dado.
# O deslocamento permite ordenar tambem numeros inteiros negativos.

def counting_sort(lista):
    n = len(lista)

    if n <= 1:
        return lista

    menor = min(lista)
    maior = max(lista)
    contagem = [0] * (maior - menor + 1)

    for numero in lista:
        contagem[numero - menor] += 1

    j = 0

    for i in range(len(contagem)):
        while contagem[i] > 0:
            lista[j] = i + menor
            contagem[i] -= 1
            j += 1

    return lista


if __name__ == "__main__":
    # Gera exatamente 100.000 numeros aleatorios para o teste.
    gerador = random.Random(42)
    lista = [gerador.randint(-50000, 50000) for _ in range(100000)]

    # Mantem um resultado de referencia para conferir a ordenacao.
    esperado = sorted(lista)

    inicio = time.perf_counter()
    resultado = counting_sort(lista)
    fim = time.perf_counter()

    print("Algoritmo: counting_sort")
    print("Quantidade de elementos:", len(resultado))
    print("Ordenacao correta:", resultado == esperado)
    print("Primeiros 10 elementos:", resultado[:10])
    print("Tempo de execucao:", round(fim - inicio, 4), "segundos")
