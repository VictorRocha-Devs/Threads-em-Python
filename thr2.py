import threading
import time
import random

def somar_vetor(id_linha, valores):
    soma = 0
    for v in valores:
        soma += v
        time.sleep(0.2)
    print(f"Linha {id_linha} - Resultado da Soma: {soma}")

for i in range(3):
    valores = [random.randint(1, 100) for _ in range(5)]
    t = threading.Thread(target=somar_vetor, args=(i, valores))
    t.start()