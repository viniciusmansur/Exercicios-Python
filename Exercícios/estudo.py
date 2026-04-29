#Exercício 1
# sum = 0
# while sum <= 100:
#     print(sum)
#     sum += 1

#Exercício 2
# lim = int(input("Digite um número: "))
# sum = 0
# while sum <= lim:
#     print(sum)
#     sum += 1

#Exercício 3
# print("Operação - Adição")
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))
# sum = n1 + n2

# print(f"{n1} + {n2} = {sum}")
# while True:
#     con = input("Deseja realizar mais uma operação? [S ou N]:  ")
#     print(f"Resposta: {con}")
#     if con == 'S' or con == 's':
#         n1 = int(input("Digite um número: "))
#         n2 = int(input("Digite outro número: "))
#         sum = n1 + n2
#         print(f"{n1} + {n2} = {sum}")
#     else:
#         break

#Exercício 4
# print("Tabuada!")
# n = int(input("Digite o número que queira saber a tabuada: "))
# i = 0
# while i <= 10:
#     s = n * i
#     print(f"{n} X {i} = {s}")
#     i += 1

#Exercício 5

while True:
    string = input("Digite uma palavra: ")
    if string[::-1] == string:
        print("Essa palavra é um palíndromo")
        break
    else:
        print("Essa palavra não é um palíndromo")