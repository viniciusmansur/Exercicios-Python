# Exercício 1
lin = int(input("Digite o número de linhas: "))
inicio = ""
 
for i in range(1, lin+1):
    inicio += str(i)
    print(inicio)
 
# Exercício 2
lista = []
qtd = int(input("Digite quantas notas serão contadas: "))
soma = 0
 
for i in range (0, qtd + 1):
    nota = float(input("Digite sua nota: "))
    lista.append(nota)
 
for c in range(len(lista)):
    soma = soma + lista[c]
    media = soma / qtd
 
print(f'A média das notas é {media}')
print(f'Notas: {lista}')
 
# Exercício 3
#timer.py
 
# Exercício 4
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
 
def Ex4():
    if x > y:
        print(f'{x} é maior que {y}')
    else:
        print(f'{y} é maior que {x}')
   
 
Ex4()
 
# Exercício 5
n = int(input("Digite um número: "))
 
def Ex5 (n):
    if n > 0:
        return 'P'
    elif n == 0:
        return 'Z'
    else:
        return 'N'
   
print(Ex5(n))
 
# Exercício 6
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
 
def Ex6 ():
    if n1 % n2 == 0:
        return 'True'
    elif n2 % n1 == 0:
        return 'True'
    else:
        return 'False'
   
print(Ex6())
 
# Exercício 7
la = int(input("Digite um lado do retângulo: "))
lb = int(input("Digite outro lado do retângulo: "))
 
def Ex7 ():
    return la * lb
 
print(f'A área do retângulo é {Ex7()}')
 
# Exercício 8
 
n = int(input("Digite o quantas vezes será preciso o valor final: "))
 
 
# Exercício 9
n = int(input("Digite o número para realizar fatorial: "))
 
def fatorialWhile ():
    i = 1
    fat = 1
    while i <= n:
        fat = fat * i
        i += 1
    return fat
 
def fatorialFor ():
    fat = 1
    for i in range(1, n+1):
        fat = fat * i
    return fat
 
print(fatorialWhile())
print(fatorialFor())
