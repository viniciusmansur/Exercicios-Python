# Exercício 1
vf = 0

while True:
    op = input("Digite o código da fruta desejada: ")
    if op == '1':
        pkg = 12.90
    elif op == '2':
        pkg = 9.30
    elif op == '3':
        pkg = 3.50
    elif op == '4':
        pkg = 7
    elif op == '5':
        pkg = 37.5
    elif op == '0':
        print("Encerrando a compra!")
        break
    else:
        print("Código inválido")
    if op == '1' or op == '2' or op == '3' or op == '4' or op == '5':
        kg = float(input("Digite a quantidade desejada em kg: "))
        vf = vf + kg*pkg
print(f"O valor final da compra é R$ {vf:.2f}")

# Exercício 2
n = int(input('Digite o valor para o fatorial:'))
i = 1
fat = 1
while i <= n:
    fat = fat * i
    i = i + 1

print(fat)

# Exercício 3
nome = input("Digite seu nome: ")
cp1 = float(input("Digite o valor da nota 1: "))
cp2 = float(input("Digite o valor da nota 2: "))
cp3 = float(input("Digite o valor da nota 3: "))
falta = int(input("Digite a quantidade de faltas: "))

if cp1 >= 0 and cp2 >= 0 and cp3 >= 0 and cp1 <= 10 and cp2 <= 10 and cp3 <= 10 and falta >= 0:
    media = (cp1 + cp2 + cp3) / 3
    if falta > 20:
        a = 'Reprovado por falta!'
    elif media >= 7:
        a = 'Aprovado!'
    elif 7 >= media >= 5:
        a = 'Recuperação!'
    else:
        a = 'Reprovado'

    if media >= 9 and falta <= 5:
        destaque = 'Você é um aluno de destaque!'
    else:
        destaque = ''

    print(f'{nome}, com notas {cp1}, {cp2}, {cp3} e {falta} faltas. Vc está: {a}')
    print(f'{destaque}')

else:
    print("Dados inválidos")

# Exercício 4
frase = input("Digite uma frase: ")
i = 0
vog = 0
while i < len(frase):
    if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
        vog = vog + 1
    print(frase[i])
    i = i + 1

print(f"A quantidade de vogais é {vog}")

# Exercício 5
frase = input("Digite uma frase: ")
i = 0
txt = ''
while i < len(frase):
    if frase[i] != '-' and frase[i] != ',' and frase[i] != ' ' and frase[i] != '.':
        txt = txt + frase[i]
    i = i + 1

if txt == txt[::-1]:
    print(f"{frase} é um palíndromo")