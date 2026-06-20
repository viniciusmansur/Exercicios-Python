from time import sleep

div = '-----------------------------'

infos = [
    {"nome": "Carlos", "id": 2234},
    {"nome": "Felipe", "id": 2060},
    {"nome": "Isabela", "id": 1286}]

filmes = {
    "Star Wars": 12,
    "Titanic": 15,
    "De Volta para o Futuro": 10,
    "Forrest Gump": 8}

def main (filmes, infos):
    while True:
        print(div)
        print("Bem vindo a locadora Sessão Filmes!")
        print(div)
        print("Filmes disponíveis:\n")
        for filme, preco in filmes.items():
            print(f"{filme}: R${preco:.2f}")
        print(div)
        print("1. Alugar filme\n2. Sair")
        print("Digite a opção que deseja acessar")
        op = input('- ')
        if op == '1':
            while True:
                print(div)
                print(f"{'Acesse sua conta para alugar um filme':^2s}")
                print("\n1. Acessar conta\n2. Cadastrar conta\n3. Voltar")
                print("Digite a opção que deseja acessar")
                op = input("- ").lower()
                if op == '1':
                    login(filmes, infos)
                    break
                elif op == '2':
                    cadastro(infos)
                elif op == '3':
                    break
                else:
                    print("Opção inválida")
                    sleep(1)
        elif op == '2':
            break
        else:
            print("Opção inválida")
            sleep(1)


def login(filmes, infos):
    while True:
        print(div)
        print("Digite seu nome")
        nome = input("- ").capitalize()
        print("\nDigite seu id")
        id = int(input("- "))
        for i in infos:
            if nome == i.get("nome") and id == i.get("id"):
                print("Dados confirmados")
                sleep(1)
                processamento(filmes)
                return
        print("Nome ou id inválidos")

def processamento(filmes):
    total = 0
    loop = 0
    while True:
        print(div)
        print("Filmes desponíveis hoje:")
        for filme, preco in filmes.items():
            print(f"{filme} - R${preco:.2f}")
        if loop > 0:
            print("\nDigite 0 para retornar.")
            print("Digite 1 para alugar.")
        print("Digite o nome do filme que deseja alugar:")
        filme = input("- ")
        if filme == '0':
            return
        elif filme == '1':
            pagamento(total)
            return
        total += filmes.get(filme.title())
        print(f"Total até agora: {total}")
        loop += 1

def pagamento(total):
    ponto = '.'
    print(div)
    print("Seu total ficou:")
    print(f"R${total:.2f}")
    print("\nOpções de pagamento:")
    print("1. Dinheiro\n2. Cartão de Crédito\n3. Cartão de Débito")
    print("Digite qual opção usará:")
    input("- ")
    for c in range(10):
        if len(ponto) == 4:
            ponto = '.'
        print('Processando'+ponto)
        ponto+='.'
        sleep(1)
    print("Obrigado por escolher a locadora Sessão Filmes!")
    sleep(2)
    return


def cadastro(infos):
    while True:
        print(div)
        nome = input("Digite seu nome: ").capitalize()
        id = input("Digite o id que deseja cadastrar (4 números): ")
        if not id.isnumeric():
            print("id inválido, digite apenas números.")
        elif len(id) != 4:
            print("id inválido, digite apenas 4 números")
        else:
            infos.append({"nome": nome, "id": int(id)})
            print("Cadastro criado!")
            sleep(1)
            return infos
        

main(filmes, infos)