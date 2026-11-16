"""Testa os algoritmos com uma lista de 100.000 inteiros aleatorios.

Uso:
    python teste_100000.py               # seis algoritmos mais rapidos
    python teste_100000.py radix_sort    # um algoritmo
    python teste_100000.py todos         # nove algoritmos: pode demorar muito
"""

import argparse
import importlib
import random
import time

ALGORITMOS = [
    "bubble_sort", "selection_sort", "insertion_sort", "merge_sort",
    "quick_sort", "heap_sort", "counting_sort", "radix_sort", "bucket_sort",
]
LENTOS = {"bubble_sort", "selection_sort", "insertion_sort"}


def testar(nome, numeros, esperado):
    funcao = getattr(importlib.import_module(nome), nome)
    copia = numeros.copy()  # Mesmos valores e mesma ordem para todos.

    inicio = time.perf_counter()
    resultado = funcao(copia)
    tempo = time.perf_counter() - inicio

    correto = resultado == esperado
    print(f"{nome:16} | correto: {correto!s:5} | {tempo:.4f} segundos", flush=True)
    if not correto:
        raise AssertionError(f"Resultado incorreto: {nome}")


def main():
    parser = argparse.ArgumentParser(description="Testar algoritmos com 100.000 elementos")
    parser.add_argument("algoritmo", nargs="?", default="rapidos",
                        choices=["rapidos", "todos"] + ALGORITMOS)
    parser.add_argument("--tamanho", type=int, default=100_000)
    parser.add_argument("--semente", type=int, default=42)
    args = parser.parse_args()

    if args.tamanho < 1:
        parser.error("O tamanho deve ser maior que zero")

    gerador = random.Random(args.semente)
    numeros = [gerador.randint(-50_000, 50_000) for _ in range(args.tamanho)]
    esperado = sorted(numeros)  # Conferencia do resultado.

    if args.algoritmo == "rapidos":
        selecionados = [nome for nome in ALGORITMOS if nome not in LENTOS]
    elif args.algoritmo == "todos":
        selecionados = ALGORITMOS
    else:
        selecionados = [args.algoritmo]

    print(f"Elementos: {len(numeros)} | intervalo de valores: -50000 a 50000")
    if args.tamanho >= 100_000 and any(nome in LENTOS for nome in selecionados):
        print("AVISO: Bubble, Selection e Insertion podem demorar muito com 100.000 elementos.", flush=True)

    for nome in selecionados:
        testar(nome, numeros, esperado)

    print("Todos os testes selecionados passaram.")


if __name__ == "__main__":
    main()
