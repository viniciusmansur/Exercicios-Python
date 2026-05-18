import time
import random

din = float(random.randint(1000, 2000))

usuarios = [
    {"nome": "Carlos", "id": '12345'},
    {"nome": "Cleber", "id": '98765'},
    {"nome": "Jonas", "id": '24680'}
]

def opcoes():
    while True:
        print("-----------------------------------")
        print("Digite 1 para registrar uma conta \nDigite 2 para acessar sua conta \nDigite 3 para sair")
        op = input("- ")
        print("-----------------------------------")
        if op == '1':
            registrar()
        elif op == '2':
            login()
        elif op == '3':
            return
        else:
            print("Opção inválida")


def registrar():
    while True:
        nome = input("Digite seu nome: ")
        id = input("Digite sua senha (5 números): ")
        
        if not isinstance(nome, str):
            print("Digite um nome válido")

        elif len(id) != 5:
            print("Senha inválida, digite uma senha de 5 números")

        else:
            break
    usuarios.append({"nome": nome, "id": id})


def login():
    tentativas = 0
    while tentativas < 4:
        senha = input("Digite sua senha: ")
        for i in usuarios:
            if i["id"] == senha:
                print(f"Seja bem vindo, {i["nome"]}")
                time.sleep(1.3)
                main()
        else:
            tentativas += 1
            print(f"Senha não encontrada. Tentativas: {tentativas}")

        if tentativas == 4:
            print("Número de tentativas excedido")


def main():
    global din
    while True:
        print('============================  \n  Seja bem vindo\n============================')
        print(f"R$ {din}\n============================")
        print("Digite + para adicionar um valor a conta")
        print("Digite - para retirar um valor da conta")
        print("Digite . para sair")
        op = input("- ")
        if op == '+':
            din = din + int(input("Digite a quantia que deseja adicionar: "))
        elif op == '-':
            din = din - int(input("Digite a quantia que deseja retirar: "))
        elif op == '.':
            time.sleep(1.2)
            opcoes()
        else:
            print("Opção invalida")


opcoes()