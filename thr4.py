import threading
import subprocess
import platform
import re

def realizar_ping(nome_amigavel, url):
    so = platform.system()
    if so == "Windows":
        comando = ["ping", "-4", "-n", "10", url]
    elif so == "Linux":
        comando = ["ping", "-4", "-c", "10", url]
    else:
        return 

    processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    tempos = []
    for linha in processo.stdout:
        busca = re.search(r'(?:time|tempo)[=<](\d+\.?\d*)', linha)
        if busca:
            tempo = float(busca.group(1))
            tempos.append(tempo)
            print(f"[{nome_amigavel}] Iteração: {tempo}ms")

    if tempos:
        media = sum(tempos) / len(tempos)
        print(f"\n>>> FINAL {nome_amigavel}: Média = {media:.2f}ms\n")

servidores = [
    ("UOL", "www.uol.com.br"),
    ("Terra", "www.terra.com.br"),
    ("Google", "www.google.com.br")
]

for nome, url in servidores:
    threading.Thread(target=realizar_ping, args=(nome, url)).start()