# Exercício 1
# n = int(input("Digite um número: "))
# i = 1
# primo = 0
# while i <= n:
#     if n % i == 0:
#         primo = primo + 1
#     if primo > 2:
#         break
#     i += 1

# if primo > 2:
#     print("Esse número não é primo")
# else:
#     print("Esse número é primo")

# Exercício 2
# l = [1, 10, 4.6, 7.7, 2, 20, 3.77]
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# Exercício 3
# fila = ['Marcos', 'Isabela', 'Carlos', 'Eduardo']
# print("Boas vindas à fila do site genêrico!")

# while True:
#     op = input("Digite en para entrar, at para atender ou sa para sair: ")
#     if op == 'en':
#         nome = input("Digite seu nome: ")
#         fila.append(nome)
#         print(f"Seu lugar na fila: {fila}")
#     elif op == 'at':
#         nome = fila.pop(0)
#         print(f"Você atendeu {nome}. Nova fila: {fila}")
#     elif op == 'sa':
#         print("Encerrado por hoje")
#         break
#     else:
#         print("Opção inválida")

# Exercício 4
a = int(input("Digite o começo do intervalo: "))
b = int(input("Digite o final do intervalo: "))

while a <= b:
    print(a)
    a += 1

for i in range(a, b):
    print(i)