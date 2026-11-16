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


resultado = merge_sort([9, 4, 7, 2, 6, 1])
print(resultado)
