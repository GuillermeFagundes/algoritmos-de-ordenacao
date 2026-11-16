import random
import time

# Vantagem: eficiente em listas pequenas ou quase ordenadas; e estavel.
# Desvantagem: pode fazer muitos deslocamentos; pior caso O(n^2).

def insertion_sort(lista):
    n = len(lista)

    for i in range(1, n):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista


if __name__ == "__main__":
    # Gera exatamente 100.000 numeros aleatorios para o teste.
    gerador = random.Random(42)
    lista = [gerador.randint(-50000, 50000) for _ in range(100000)]

    # Mantem um resultado de referencia para conferir a ordenacao.
    esperado = sorted(lista)

    inicio = time.perf_counter()
    resultado = insertion_sort(lista)
    fim = time.perf_counter()

    print("Algoritmo: insertion_sort")
    print("Quantidade de elementos:", len(resultado))
    print("Ordenacao correta:", resultado == esperado)
    print("Primeiros 10 elementos:", resultado[:10])
    print("Tempo de execucao:", round(fim - inicio, 4), "segundos")
