import random
import time

from ####### import #######

lista = [random.randint(1, 100000) for i in range(100000)]

inicio = time.perf_counter()

resultado = #######(lista)

fim = time.perf_counter()

print("Quantidade:", len(resultado))
print("Tempo:", fim - inicio, "segundos")
