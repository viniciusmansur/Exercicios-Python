#Exercício 1
def addtuple(tupla):
    lista = list(tupla)
    lista.append("Item")
    tupla = tuple(lista)
    return tupla

#Exercício 2
def remtuple(tupla, index):
    lista = list(tupla)
    lista.pop(index)
    tupla = tuple(lista)
    return tupla

#Exercício 3
def listfrase(frase):
    dic = {}
    for i in frase:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    print(dic)
    return dic


#Exercício 4
def anagrama(frase1, frase2):
    frase1 = listfrase(frase1)
    frase2 = listfrase(frase2)

    if frase1 == frase2:
        return "É um anagrama"
    else:
       return "Não é anagrama"

#Exercício 5
def comparlist(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)

    comum = set1 & set2
    primeira = set1 - set2
    segunda = set2 - set1
    naorep = set1 ^ set2

    return comum, primeira, segunda, naorep

print(comparlist([1, 4, 5, 10, 12], [2, 4, 7, 9, 12]))
