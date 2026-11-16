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
    resultado = radix_sort([9, 4, 7, 2, 6, 1])
    print(resultado)
