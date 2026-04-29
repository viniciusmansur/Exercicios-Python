# Exercício 1
flag = True
print(f'{'Produtos':-^10s}')
print(f'{'Produto 1':<3s} | R$ 5,00')
print(f'{'Produto 2':<3s} | R$ 10,00')
print(f'{'Produto 3':<3s} | R$ 3,00')
prod1 = 5
prod2 = 10
prod3 = 3

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
prod = int(input("Digite o produto que deseja: "))

if prod == '1':
    prod = 5
elif prod == '2':
    prod = 10
elif prod == '3':
    prod = 3
else:
    flag = False
    print("Produto inválido")

if flag:
    print(f"Olá {nome}, você tem {idade} anos e sua compra saiu por R${prod:.2f}")

# Exercício 2
num = 1

while num <= 100:
    print(num)
    num += 1

# Exercício 3
num = 50

while num <= 100:
    print(num)
    num += 1

# Exercício 4
num = 10

while num >= 0:
    print(num)
    num -= 1
print('Fogo!')

# Exercício 5
num = int(input("Digite um número: "))
numver = 1

while numver <= num:
    print(numver)
    numver += 1
    if numver % 2 == 1:
        numver += 1

# Exercício 6
num = int(input("Digite um número: "))
numver = 1

while numver <= num:
    print(numver)
    numver += 2

# Exercício 7
comeco = int(input("Digite um número: "))
fim = int(input("Digite outro número maior que o outro: "))
soma = 0


while comeco <= fim:
    if comeco % 2 == 0:
        soma = comeco + soma
    comeco += 1

print(f'A soma dos números pares desse intervalo é {soma}')

# Exercício 8
num = int(input("Digite um número: "))
soma = 0
while num != 0:
    soma = num + soma
    num = int(input("Digite um número: "))
print(f"você digitou 0! A soma dos números digitados foram: {soma}")