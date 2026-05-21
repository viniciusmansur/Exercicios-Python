#Exercício 1
loop = input("Digite o loop que você deseja: ")
n1 = int(input("Digite o começo do intervalo: "))
n2 = int(input("Digite o final do intervalo: "))
media = 0

def calculo(fun, inicio, fim):
    soma = 0
    cont = 0
    if fun == 'while':
        while inicio <= fim:
            soma = soma + inicio
            inicio += 1
            cont += 1
        media = soma / cont
        return soma, media
    elif fun == 'for':
        for i in range(inicio, fim + 1):
            soma = soma + i
            cont = i
        media = soma / cont
        return soma, media
    return None

print(calculo(loop, n1, n2))

#Exercício 2
lista = ['Fazer x', 'Fazer y', 'Fazer z']

def main():
    while True:
        print("Digite 1 para armazenar\nDigite 2 para remover uma tarefa\nDigite 3 para mostrar a lista\nDigite 4 para sair")
        op = input('- ')
        if op == '1':
            novo = input("Digite uma tarefa: ")
            armazenar(lista, novo)
        elif op == '2':
            print(remover(lista))
        elif op == '3':
            imprimir(lista)
        elif op == '4':
            return
        else:
            print("Opção inválida")

def armazenar(lista, novo):
    return lista.append(novo)

def remover(lista):
    removido = lista.pop(0)
    return removido, lista

def imprimir(lista):
    for i in range(len(lista)):
        print(f'{lista[i]} - {i}')
    return

main()