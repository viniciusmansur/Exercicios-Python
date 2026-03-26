#Exercício 1
idade = int(input("Digite sua idade: "))
sal = int(input("Digite seu salário: "))
amgdono = str(input("Você é amigo do dono? (s ou n): "))

x = 18 < idade < 60
y = sal >= 1500
cond = x and y or amgdono == "s"

print("Pode pegar salário?", cond)

#Exercício 2
x = input("Digite seu nome: ")

print(f"Bem vindo, {x}!")

#Exercício 3
x = input("Digite seu nome: ")
y = int(input("Digite sua idade: "))

print(f"Olá meu nome é {x} e tenho {y} anos")

#Exercício 4
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("digite o segundo o número: "))

print(f"A soma de {n1} e {n2} é igual a {n1 + n2}")

#Exercício 5
anos = int(input("Digite o número de anos que vc trabalhou: "))

bonus = anos * 400

input(f"Como trabalhou por {anos} anos, você tem direito a R${bonus},00 de bônus")

#Exercício 6
merc = float(input("Digite o valor da mercadoria: "))
disc = float(input("Digite o valor do desconto: "))

soma = merc * (1 - disc/100)

print(f"A compra de {merc} com o desconto de {disc}% saíra por {soma}")

#Exercício 7
km = int(input("Digite o número de quilômetros rodados: "))
dia = int(input("Digite o número de dias que o carro foi alugado: "))

soma = km * 0.15 + 60 * dia

print(f'O carro alugado por {dia} dias e rodado por {km} Km, sairá por R${soma}')