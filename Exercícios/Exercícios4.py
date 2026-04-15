#Exercício 1
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