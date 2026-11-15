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


resultado = bucket_sort([9, 4, 7, 2, 6, 1])
print(resultado)
