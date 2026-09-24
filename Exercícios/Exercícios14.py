lista = [12, 68, 95, 41, 10, 71]
lista2 = [10, 12, 18, 11]

#Exercício 1
def bubblesort():
    for i in range(len(lista) - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                c = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = c

    print(lista)

#Exercício 2
def selectionsort():
    for j in range(len(lista)):
        menorindex = j
        menornum = lista[menorindex]
        for i in range(j):
            if menornum < lista[i]:
                menornum = lista[i]
                c = lista[i]  
                lista[i] = lista[menorindex]
                lista[menorindex] = c

    print(lista)

#Exercício 3
def insertionsort():
    for i in range(1, len(lista2)):
        c = lista2[i] # c -> 11
        j = i - 1 # j -> 2
    while j >= 0 and lista2[j] > c:
        lista2[j+1] = lista2[j]
        j = j - 1
        print(lista2)
    lista2[j+1] = c

insertionsort()