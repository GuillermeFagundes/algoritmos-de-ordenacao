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
    resultado = selection_sort([15, 8, 23, 4, 12, 7])
    print(resultado)
