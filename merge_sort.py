import random
import time

# Vantagem: tempo O(n log n) garantido e ordenacao estavel.
# Desvantagem: precisa de memoria auxiliar O(n).

def merge_sort(lista):
    n = len(lista)

    if n <= 1:
        return lista

    meio = n // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    i = 0
    j = 0
    k = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1

    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1

    return lista


if __name__ == "__main__":
    # Gera exatamente 100.000 numeros aleatorios para o teste.
    gerador = random.Random(42)
    lista = [gerador.randint(-50000, 50000) for _ in range(100000)]

    # Mantem um resultado de referencia para conferir a ordenacao.
    esperado = sorted(lista)

    inicio = time.perf_counter()
    resultado = merge_sort(lista)
    fim = time.perf_counter()

    print("Algoritmo: merge_sort")
    print("Quantidade de elementos:", len(resultado))
    print("Ordenacao correta:", resultado == esperado)
    print("Primeiros 10 elementos:", resultado[:10])
    print("Tempo de execucao:", round(fim - inicio, 4), "segundos")
