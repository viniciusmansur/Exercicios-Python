#Exercício 1
a = int(input("Digite o número de dias: "))
b = int(input("Digite o número de horas: "))
c = int(input("Digite o número de minutos: "))
d = int(input("Digite o número de segundos: "))

print(f"{a} dia {b} horas {c} minutos {d} segundos")

s = (a * 24 * 3600) + (b * 3600) + (c * 60) + d

print(f"Isso equivale a {s} segundos")

#Exercício 2
s = int(input("Digite o número de segundos que deseja converter: "))

d = s // (24 * 3600)
x = s % (24 * 3600)
h = x // 3600
y = s % 3600
m = y // 60
z = s % 60
s = z
print(f"{s} segundos equivalem a {d} dias, {h} horas, {m} minutos e {s} segundos")