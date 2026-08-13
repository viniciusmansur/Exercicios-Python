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

#Exercício 2
nomes = []
notas1 = []
notas2 = []
medias = []

def exibir_menu(nomes, notas1, notas2, medias):
    while True:
        print("Bem vindo ao sistema da escola")
        print("\n Escolha uma opção para acessar")
        print("1) Cadastrar aluno")
        print("2) Listar todas as médias cadastradas")
        print("3) Mostrar número de alunos")
        print("4) Quantidade de alunos aprovados/reprovados")
        print("5) Listar todos os alunos")
        print("6) Sair")
        op = input("- ")
        if op == '1':
            cadastrar_aluno(nomes, notas1, notas2)
        elif op == '2':
            calcular_media(nomes, medias)
        elif op == '3':
            total_alunos(nomes)
        elif op == '4':
            total_aprovados(nomes, medias)
        elif op == '5':
            listar_alunos(nomes, notas1, notas2)
        elif op == '6':
            break
        else:
            print("Opção inválida")

def cadastrar_aluno(nomes, notas1, notas2):
    print("====================")
    nomes.append(input("Digite o nome do aluno: "))
    n1 = float(input("Digite a primeira nota do aluno: "))
    notas1.append(n1)
    n2 = float(input("Digite a primeira nota do aluno: "))
    notas2.append(n2)
    medias.append((n1 + n2)/ 2)
    print("====================")
    return

def calcular_media(nomes, medias):
    print("====================")
    for nome in nomes:
        for media in medias:
            print(f"{nome:<12} - {media}")
    print("====================")

def total_alunos(nomes):
    print("====================")
    print(f"Número de alunos: {len(nomes)}")
    print("====================")

def total_aprovados(nomes, medias):
    contap = 0
    print("====================")
    for media in medias:
        if media >= 6:
            contap += 1
    print(f"Aprovados: {contap}")
    print(f"Reprovados: {abs(len(nomes) - contap)}")
    print("====================")

def listar_alunos(nomes, notas1, notas2):
    print("====================")
    for nome in nomes:
        for nota1 in notas1:
            for nota2 in notas2:
                print(f"{nome} - {nota1:.2f} | {nota2:.2f}")
    print("====================")                
    return

exibir_menu(nomes, notas1, notas2, medias)