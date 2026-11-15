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


resultado = quick_sort([9, 4, 7, 2, 6, 1])
print(resultado)
