def funcao(x):
    x = float(input("Digite o valor de x: "))
    if x <= 2:
        y = x
    elif 2 < x <= 3.5:
        y = 2    
    elif 3.5 < x <= 5:
        y = 3
    elif x > 5:
        y = (x ** 2) - (10 * x) + 28
    else:
        return 'X inválido'
    return y

nomes = []
notas1 = []
notas2 = []

def exibir_menu():
    while True:
        print("Bem vindo ao sistema da escola")
        print("\n Escolha uma opção para acessar")
        print("1) Cadastrar aluno")
        print("2) Listar todos os alunos cadastrados")
        print("3) Mostrar estatísticas da turma")
        print("4) Sair")
        op = input("- ")
        if op == '1':
            cadastrar_aluno(nomes, notas1, nostas2)

def cadastrar_aluno(nomes, notas1, notas2):
    