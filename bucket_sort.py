import random
import time

# Vantagem: pode se aproximar de O(n) com valores bem distribuidos.
# Desvantagem: usa memoria auxiliar e pode chegar a O(n^2) com baldes desiguais.
# Cada balde e ordenado por insercao, sem usar sort() ou sorted().
# Esta versao foi feita para listas de numeros inteiros.

def bucket_sort(lista):
    n = len(lista)

    if n <= 1:
        return lista

    menor = min(lista)
    maior = max(lista)

    if menor == maior:
        return lista

    quantidade = n
    baldes = [[] for i in range(quantidade)]

    for numero in lista:
        indice = (numero - menor) * (quantidade - 1) // (maior - menor)
        baldes[indice].append(numero)

    k = 0

    for balde in baldes:
        for i in range(1, len(balde)):
            atual = balde[i]
            j = i - 1

            while j >= 0 and balde[j] > atual:
                balde[j + 1] = balde[j]
                j -= 1

            balde[j + 1] = atual

        for numero in balde:
            lista[k] = numero
            k += 1

    return lista


if __name__ == "__main__":
    # Gera exatamente 100.000 numeros aleatorios para o teste.
    gerador = random.Random(42)
    lista = [gerador.randint(-50000, 50000) for _ in range(100000)]

    # Mantem um resultado de referencia para conferir a ordenacao.
    esperado = sorted(lista)

    inicio = time.perf_counter()
    resultado = bucket_sort(lista)
    fim = time.perf_counter()

    print("Algoritmo: bucket_sort")
    print("Quantidade de elementos:", len(resultado))
    print("Ordenacao correta:", resultado == esperado)
    print("Primeiros 10 elementos:", resultado[:10])
    print("Tempo de execucao:", round(fim - inicio, 4), "segundos")
