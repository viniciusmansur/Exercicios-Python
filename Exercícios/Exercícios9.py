#Exercício 1
def soma (*args):
    soma = 0 
    for arg in args:
        soma += arg
    return soma

print(soma(10, 20, 30, 5 , 5))

#Exercício 2
def media (*args):#ars[0],
    return soma(*args)/len(args)

print(media(5, 10, 3, 2, 1))

#Exercício 3
def string (*args):
    x = ''
    for arg in args:
        x += arg + ' '

    return x

print(string('oi', 'tudo', 'bem?'))

#Exercício 4
def main():
    while True:
        print("Bem vindo ao supermercado genério")
        print("Selecione a opção que deseja acessar")
        print("1 - Adicionar produto ao carrinho")
        print("2 - Remover produto do carrinho")
        print("3 - Ver carrinho")
        print("4 - Sair")
        op = input("- ")
        if op == '1':
            produto = input("Digite o produto que deseja adicionar: ")
            adicionar_produto(produto)
        elif op == '2':
            produto = input("Digite o produto que deseja remover: ")
            remover_produto(produto)
        elif op == '3':
            ver_carrinho()
        elif op == '4':
            break
        else:
            print("Opção inválida")

def adicionar_produto(produto):
    carrinho.append(produto)
    return

def remover_produto(produto):
    for x in carrinho:
        for i in range(len(carrinho)):
            if produto in x:
                carrinho.pop(i)
                break

def ver_carrinho():
    print(carrinho)

carrinho = ['Banana', 'Maçã', "Queijo"]

main()