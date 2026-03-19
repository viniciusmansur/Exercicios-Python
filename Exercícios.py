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

#Exercício 3
n1 = int(input("Digite sua nota em matemática: "))
n2 = int(input("Digite sua segunda em biologia: "))
n3 = int(input("Digite sua terceira história: "))

r1 = n1 >= 6
r2 = n2 >= 6
r3 = n3 >= 6

print(f"Foi aprovado em matemática? {r1}")
print(f"Foi aprovado em biologia? {r2}")
print(f"Foi aprovado em história? {r3}")

#Exercício 4
sal = int(input("Digite seu salário: "))
cond = 1600

res = sal >= cond

print(f"Pode contratar nossos serviços? {res}")

#Exercício 5
n = int(input("Digite seu número: "))

r = n % 2 == 0

print(f"Esse número é par? {r}")

#Exercício 6
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

r1 = (n1 % 2) != (n2 % 2)

print(f"Os números {n1} e {n2} estão em paridade distinta? {r1}")