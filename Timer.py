import time

tempo = int(input("Digite quantos segundos o timer irá contar: "))

for i in range(tempo, -1, -1):
    seg = i % 60
    minutos = int(i / 60) % 60
    horas = int(i / 3600)

    print(f"{horas:02}:{minutos:02}:{seg:02}")
    time.sleep(1)
