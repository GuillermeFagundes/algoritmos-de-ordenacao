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


resultado = counting_sort([9, 4, 7, 2, 6, 1])
print(resultado)
