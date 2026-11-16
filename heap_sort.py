import random
import time

# Vantagem: tempo O(n log n) garantido e memoria auxiliar O(1).
# Desvantagem: nao e estavel e sua implementacao e mais complexa.

def ajustar_heap(lista, n, raiz):
    while True:
        maior = raiz
        esquerda = 2 * raiz + 1
        direita = 2 * raiz + 2

        if esquerda < n and lista[esquerda] > lista[maior]:
            maior = esquerda
        if direita < n and lista[direita] > lista[maior]:
            maior = direita

        if maior == raiz:
            break

        lista[raiz], lista[maior] = lista[maior], lista[raiz]
        raiz = maior


def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        ajustar_heap(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        ajustar_heap(lista, i, 0)

    return lista


if __name__ == "__main__":
    # Gera exatamente 100.000 numeros aleatorios para o teste.
    gerador = random.Random(42)
    lista = [gerador.randint(-50000, 50000) for _ in range(100000)]

    # Mantem um resultado de referencia para conferir a ordenacao.
    esperado = sorted(lista)

    inicio = time.perf_counter()
    resultado = heap_sort(lista)
    fim = time.perf_counter()

    print("Algoritmo: heap_sort")
    print("Quantidade de elementos:", len(resultado))
    print("Ordenacao correta:", resultado == esperado)
    print("Primeiros 10 elementos:", resultado[:10])
    print("Tempo de execucao:", round(fim - inicio, 4), "segundos")
