import random
import time

# Vantagem: faz poucas trocas e nao precisa de uma lista auxiliar.
# Desvantagem: sempre faz O(n^2) comparacoes e nao e estavel.

def selection_sort(lista):
    n = len(lista)

    for j in range(n):
        indice_menor = j

        for i in range(j + 1, n):
            if lista[i] < lista[indice_menor]:
                indice_menor = i

        lista[j], lista[indice_menor] = lista[indice_menor], lista[j]

    return lista


if __name__ == "__main__":
    # Gera exatamente 100.000 numeros aleatorios para o teste.
    gerador = random.Random(42)
    lista = [gerador.randint(-50000, 50000) for _ in range(100000)]

    # Mantem um resultado de referencia para conferir a ordenacao.
    esperado = sorted(lista)

    inicio = time.perf_counter()
    resultado = selection_sort(lista)
    fim = time.perf_counter()

    print("Algoritmo: selection_sort")
    print("Quantidade de elementos:", len(resultado))
    print("Ordenacao correta:", resultado == esperado)
    print("Primeiros 10 elementos:", resultado[:10])
    print("Tempo de execucao:", round(fim - inicio, 4), "segundos")
