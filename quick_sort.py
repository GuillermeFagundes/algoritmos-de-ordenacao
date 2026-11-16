# Vantagem: tempo medio O(n log n), sem criar sublistas auxiliares.
# Desvantagem: nao e estavel e pode chegar a O(n^2) no pior caso.
# Esta versao e recursiva: a funcao ordenar chama a si mesma.

def quick_sort(lista):

    def ordenar(inicio, fim):
        if inicio >= fim:
            return

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
            ordenar(inicio, j)

        if i < fim:
            ordenar(i, fim)

    ordenar(0, len(lista) - 1)
    return lista


resultado = quick_sort([9, 4, 7, 2, 6, 1])
print(resultado)
