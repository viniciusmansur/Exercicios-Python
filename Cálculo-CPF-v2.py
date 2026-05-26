cpf = input("Digite seu CPF: ")
reg = int(cpf[8])
regioes = ["de Rio Grande do Sul", "da região Centro-Oeste", "da região Norte",
           "do Ceará, Maranhão ou Piauí", "de Alagoas, Paraíba, Pernambuco ou Rio Grande do Norte",
           "da Bahia ou Sergipe", "de Minas Gerais", "de Espirito Santo ou Rio de Janeiro",
           "de São Paulo", "de Paraná ou Santa Catarina"]

def ver1(cpf):
    soma = 0
    cont = 10
    for i in range(0, 9):
        soma = soma + int(cpf[i]) * cont
        cont -= 1
    digver1 = soma % 11
    if digver1 == 1 or digver1 == 2:
        digver1 = 0
        return digver1
    elif digver1 >= 2:
        digver1 = 11 - digver1
        return digver1

def ver2(cpf):
    soma = 0
    cont = 11
    for i in range(0, 10):
        soma = soma + int(cpf[i]) * cont
        cont -= 1
    digver2 = soma % 11
    if digver2 == 1 or digver2 == 0:
        digver2 = 0
        return digver2
    elif digver2 >= 2:
        digver2 = 11 - digver2
        return digver2

digver1 = ver1(cpf)
digver2 = ver2(cpf)

def comparador(digver1, digver2, cpf):
    global reg
    if digver1 == int(cpf[9]) and digver2 == int(cpf[10]):
        val = 'Esse cpf é válido'
        for i in range(len(regioes)):
            if  i == reg:
                return f"{val}, você é {regioes[i]}"
    else:
        return 'Esse cpf é inválido'

print(comparador(digver1, digver2, cpf))