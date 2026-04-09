#Exercício 1
kwh = float(input("Digite a quantidade de kWh consumidos: "))
print("Residencial  R")
print("Industrial   I")
print("Comercial    C")
tipo = input("Digite o tipo da sua instalação: ")

if kwh <= 500 and tipo == 'R':
    val = kwh * 0.4
elif kwh > 500 and tipo == 'R':
    val = kwh * 0.65
elif kwh <= 1000 and tipo == 'C':
    val = kwh * 0.55
elif kwh > 1000 and tipo == 'C':
    val = kwh * 0.6
elif kwh <= 5000 and tipo == 'I':
    val = kwh * 0.55
elif kwh > 5000 and tipo == 'I':
    val = kwh * 0.6

print(f"O valor da conta ficou em R${val}")

#Exercício 2
nome = input("Digite seu nome: ")
print(f'Seu nome tem {len(nome)} e a primeira letra é {nome[:1]}')

#Exercício 3
pal = input("Digite uma palavra: ")
print(pal[::2])

#Exercício 4
pal = input("Digite uma palavra: ")
print(pal[1::2])

#Exercício 5
fra1 = input("Digite uma frase: ")
fra2 = input("Digite outra frase: ")
print(fra1[1:] + fra2[1:])

#Exercício 6
pal = input("Digite uma palavra: ")
x = pal[::-1]
print(f"Essa palavra ao contrário é: {pal[::-1]}")
if pal == x:
    print("Essa palavra é um palíndromo!")

#Exercício 7
pal = input("Digite uma palavra: ")
x = pal[::-1]
print(f"Essa palavra ao contrário é: {pal[::-1]}")
if pal == x:
    print("Essa palavra é um palíndromo!")