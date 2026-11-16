import random
import time

# Vantagem: tempo medio O(n log n), sem criar sublistas auxiliares.
# Desvantagem: nao e estavel e pode chegar a O(n^2) no pior caso.
# A pilha guarda intervalos para evitar o limite de recursao do Python.

def quick_sort(lista):
    n = len(lista)
    intervalos = [(0, n - 1)]

    while intervalos:
        inicio, fim = intervalos.pop()

        if inicio >= fim:
            continue

        pivo = lista[(inicio + fim) // 2]
        i = inicio
        j = fim

        while i <= j:
            while lista[i] < pivo:
                i += 1
            while lista[j] > pivo:
                j -= 1

            if i <= j:
                lista[i], lista[j] = lista[j], lista[i]
                i += 1
                j -= 1

        if inicio < j:
            intervalos.append((inicio, j))
        if i < fim:
            intervalos.append((i, fim))

    return lista


if __name__ == "__main__":
    # Gera exatamente 100.000 numeros aleatorios para o teste.
    gerador = random.Random(42)
    lista = [gerador.randint(-50000, 50000) for _ in range(100000)]

    # Mantem um resultado de referencia para conferir a ordenacao.
    esperado = sorted(lista)

    inicio = time.perf_counter()
    resultado = quick_sort(lista)
    fim = time.perf_counter()

    print("Algoritmo: quick_sort")
    print("Quantidade de elementos:", len(resultado))
    print("Ordenacao correta:", resultado == esperado)
    print("Primeiros 10 elementos:", resultado[:10])
    print("Tempo de execucao:", round(fim - inicio, 4), "segundos")
