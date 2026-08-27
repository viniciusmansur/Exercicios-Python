#Exercício 1
listas = []

def main():
    for i in range(3):
        for j in range(3):
            print([i, j])
            listas.append([i, j])

    i = 0
    for lista in listas:
        print(lista, end='')
        i += 1
        if i % 3 == 0:
            print()

listas2 = [[i, j] for i in range(3) for j in range(3)]

def main1b():
    i = 0
    for lista in listas2:
        print(lista, end='')
        i += 1
        if i % 3 == 0:
            print()

#Exercício 2
def main2():
    dia = 1

    match dia:
        case 1:
            print("Sábado")
        case 2:
            print("Domingo")
        case 3:
            print("Segunda")
        case _:
            print("Outro dia")

#Exercício 3
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

def main3():
    plt.plot(x, y, marker='o', linestyle='-')

    plt.title("Gráfico de Coordenada x, y")
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    plt.grid(True)
    plt.show()

#Exercício 4
a = [i for i in range(-10, 11)]
b = [i**2 for i in a]

def main4():
    plt.plot(a, b, marker='o', linestyle='-')
    plt.show()

#Exercício 5
def main5():
    linhas = int(input("Digite a quantidade de linhas: "))
    colunas = int(input("Digite a quantidade de colunas: "))
    matriz = []

    for j in range(linhas):
        l = []
        for i in range(colunas):
            l.append(int(input(f"Digite o número para adicionar ao A{j},{i}: ")))
        print(l)
        matriz.append(l)
    print(matriz)

#Exercício 6
def main6():
    linhas = int(input("Digite a quantidade de linhas: "))
    colunas = int(input("Digite a quantidade de colunas: "))
    matriz = []

    for i in range(colunas):
        l = []
        for j in range(linhas):
            l.append(1 + j + i * colunas)
            
        print(l)
        matriz.append(l)
    print(matriz)

main6()

#Exercício 7
matriz = [[1, 2, 3]
          [4, 5, 6]
          [7, 8, 9]]

def main7():