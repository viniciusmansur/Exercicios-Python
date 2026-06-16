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
        print("1. Alugar filme")
        print("2. Sair")
        print("Digite a opção que deseja acessar")
        op = input('- ')
        if op == '1':
            while True:
                print("\n1. Acessar conta")
                print("2. Cadastrar conta")
                print("3. Voltar")
                print("Digite a opção que deseja acessar")
                op = input("- ").lower()
                if op == '1':
                    processamento()
                elif op == '2':
                    cadastro(infos)
                elif op == '3':
                    break
                else:
                    print("Opção inválida")
        elif op == '2':
            break
        else:
            print("Opção inválida")


def processamento():
    print("Tudo certin")

def cadastro(infos):
    while True:
        print(div)
        nome = input("Digite seu nome: ")
        id = input("Digite o id que deseja cadastrar (4 números): ")
        if not id.isnumeric():
            print("id inválido, digite apenas números.")
        elif len(id) != 4:
            print("id inválido, digite apenas 4 números")
        else:
            infos.append({"nome": nome, "id": id})
            return infos
        

main(filmes, infos)