import threading
import random
import time

DISTANCIA_MAXIMA = 50 # cm

def sapo_correndo(nome):
    percorrido = 0
    while percorrido < DISTANCIA_MAXIMA:
        pulo = random.randint(1, 5)
        percorrido += pulo
        print(f"Sapo {nome} saltou {pulo}cm. Total: {percorrido}/{DISTANCIA_MAXIMA}cm")
        time.sleep(0.1)
    
    print(f"--- O Sapo {nome} CHEGOU! ---")

sapos = ["Verde", "Boi", "Cururu", "Martelo", "Folha"]
for nome in sapos:
    threading.Thread(target=sapo_correndo, args=(nome,)).start()