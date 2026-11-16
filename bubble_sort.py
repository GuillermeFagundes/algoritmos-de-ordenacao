# Vantagem: simples de entender e nao precisa de uma lista auxiliar.
# Desvantagem: faz muitas comparacoes e trocas; tempo O(n^2).

def bubble_sort(lista):

    n = len(lista)

    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

if __name__ == "__main__":
    resultado = bubble_sort([9, 4, 7, 2, 6, 1])
    print(resultado)
