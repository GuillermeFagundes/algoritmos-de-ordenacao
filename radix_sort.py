import random
import time

# Vantagem: ordena inteiros por digitos em O(d * (n + 10)).
# Desvantagem: precisa de memoria auxiliar O(n) e depende do numero de digitos.
# O deslocamento permite ordenar tambem numeros inteiros negativos.

def radix_sort(lista):
    n = len(lista)

    if n <= 1:
        return lista

    menor = min(lista)
    valores = [numero - menor for numero in lista]
    maior = max(valores)
    casa = 1

    while maior // casa > 0:
        contagem = [0] * 10
        saida = [0] * n

        for numero in valores:
            digito = (numero // casa) % 10
            contagem[digito] += 1

        for i in range(1, 10):
            contagem[i] += contagem[i - 1]

        for i in range(n - 1, -1, -1):
            digito = (valores[i] // casa) % 10
            saida[contagem[digito] - 1] = valores[i]
            contagem[digito] -= 1

        valores = saida
        casa *= 10

    for i in range(n):
        lista[i] = valores[i] + menor

    return lista


if __name__ == "__main__":
    # Gera exatamente 100.000 numeros aleatorios para o teste.
    gerador = random.Random(42)
    lista = [gerador.randint(-50000, 50000) for _ in range(100000)]

    # Mantem um resultado de referencia para conferir a ordenacao.
    esperado = sorted(lista)

    inicio = time.perf_counter()
    resultado = radix_sort(lista)
    fim = time.perf_counter()

    print("Algoritmo: radix_sort")
    print("Quantidade de elementos:", len(resultado))
    print("Ordenacao correta:", resultado == esperado)
    print("Primeiros 10 elementos:", resultado[:10])
    print("Tempo de execucao:", round(fim - inicio, 4), "segundos")
