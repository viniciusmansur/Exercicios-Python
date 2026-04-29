cpf = input("Digite seu CPF: ")
reg = cpf[8:9]

# Obtenção dígito verificador 1 (do penúltimo número do cpf)
digver1 = (int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2) % 11
if digver1 == 1 or digver1 == 2:
    digver1 = 0
elif digver1 >= 2:
    digver1 = 11 - digver1

# Obtenção dígito verificador 2 (último númeor do cpf)
digver2 = (int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + int(cpf[9]) * 2) % 11
if digver2 == 1 or digver2 == 0:
    digver2  = 0
elif digver2 >= 2:
    digver2 = 11 - digver2

# Comparação verificadores com CPF
if digver1 == int(cpf[9]) and digver2 == int(cpf[10]):
    print("Este CPF é válido!")

    if reg == '0':
        print("Você é de Rio Grande do Sul")
    elif reg == '1':
        print("Você é da região Centro-Oeste")
    elif reg == '2':
        print("Você é da região Norte")
    elif reg == '3':
        print("Você é do Ceará, Maranhão ou Piauí")
    elif reg == '4':
        print("Você é de Alagoas, Paraíba, Pernambuco ou Rio Grande do Norte")
    elif reg == '5':
        print("Você é da Bahia ou Sergipe")
    elif reg == '6':
        print("Você é de Minas Gerais")
    elif reg == '7':
        print("Você é de Espirito Santo ou Rio de Janeiro")
    elif reg == '8':
        print("Você é de São Paulo")
    elif reg == '9':
        print("Você é de Paraná ou Santa Catarina")

else:
    print("Este CPF é inválido")