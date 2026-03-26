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

#Exercício 8
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

s = n1 % 2 == n2 % 2

print(f"Os números {n1} e {n2} possuem paridade distinta? {s}")

#Exercício 9
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

if a > b:
    print("a é maior que b")
else:
    print("b é maior que a")

#Exercício 10
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    print(f'o maior valor é {n1}')
else:
    print(f"O maior valor é {n2}")

#Exercício 11
vel = int(input("Digite a velocidade que o carro estava trafegando: "))

if vel > 80:
    print("Você estava acima do limite de velocidade e foi multado")
    print(f'Você deverá pagar R${(vel - 80) * 5} como multa')
else:
    print("Você estava abaixo do limite de velociade, parabéns!")

#Exercício 12
sal = float(input("Digite seu salário: "))
if sal > 1250.00:
    print(f"Parabéns você recebeu um aumento de 10%! Seu salário agora será de {sal * 1.10}")
else:
    print(f"Parabéns você recebeu um aumento de 15%! Seu salário agora será de {sal *1.15}")

#Exercício 13
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b > c:
    print(a, c)
elif a > c > b:
    print(a, b)
elif b > a > c:
    print(b, c)

#Exercício 14
n = int(input("Digite o número: "))

if n % 2 == 0:
    if n < 100:
        print(f"o número {n} é par e menor que 100")
    else:
        print(f"O número {n}")
if n % 2 == 1:
    if n < 100:
        print(f"O número {n} é ímpar e menor que 100")
    else:
        print(f"O número {n} é ímpar e maior que 100")
        
#Exercício 15
n = int(input("Digite o número: "))

if n % 2 == 0 and n < 100:
    print(f"O número {n} é par e menor que 100")
elif n % 2 == 0 and n >= 100:
    print(f'O número {n} é par e maior ou igual que 100')
elif n % 2 == 1 and n < 100:
    print(f"O número {n} é impar e menor que 100")
elif n % 2 == 1 and n >= 100:
    print(f"O número {n} é impar e maior ou igual a 100")