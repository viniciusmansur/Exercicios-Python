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