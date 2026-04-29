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

# Exercício 9
print(f'{'Maquina registradora'}')
print("Código  |  Preço ")
print('1       |   0,50')
print('2       |   1,00')
print('3       |   4,00')
print('5       |   7,00')
print('9       |   8,00')
print('Digite 0 para finalizar')

soma = 0
cod1 = 0.5
cod2 = 1
cod3 = 4
cod5 = 7
cod9 = 8

while True:
    prod = int(input("Digite o código do produto: "))
    if prod == 0:
        print(f"Sua compra ficou R${soma:.2f}")
        break
    if prod == 1:
        tx = cod1
    elif prod == 2:
        tx = cod2
    elif prod == 3:
        tx = cod3
    elif prod == 5:
        tx = cod5
    elif prod == 9:
        tx = cod9
    else:
        print("Código Inválido")
        continue
    qtd = int(input("Digite a quantidade de produtos: "))
    print("----------------")
    soma = soma + tx*qtd

# Exercício 10
n = int(input("Digite um número: "))
soma = 0

while n != 0:
    soma = soma + n
    n = n - 1
print(f'{soma}')