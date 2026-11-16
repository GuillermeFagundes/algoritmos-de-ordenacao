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
    resultado = insertion_sort([5, 2, 4, 1, 3])
    print(resultado)
