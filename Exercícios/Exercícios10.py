import matematica
import matematica2

#Exercício 1
def main():
    while True:
        print("Calculadora")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        op = input("- ")
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if op == '1':
            print(f"{a} + {b} = {matematica.soma(a, b)}")
        elif op == '2':
            print(f"{a} - {b} = {matematica.subtracao(a, b)}")
        elif op == '3':
            print(f"{a} - {b} = {matematica2.multiplicacao(a, b)}")
        elif op == '4':
            print(f"{a} - {b} = {matematica2.divisao(a, b)}")
        elif op == '0':
            break
        else:
            print("Opção inválida")

#Exercício 2
import utils

def main2():
    while True:
            print("Utilidades palavras")
            print("1. Contar vogais")
            print("2. Reverter palavras")
            print("3. Contar palavras")
            print("4. Verificação palíndromo")
            print("0. Sair")
            op = input("- ")
            palavra = input("Digite a palavra: ")
            if op == '1':
                print(utils.contvog(palavra))
            elif op == '2':
                print(utils.revpala(palavra))
            elif op == '3':
                print(utils.contpal(palavra))
            elif op == '4':
                res = utils.verpali(palavra)
                if res:
                    print("É palíndromo")
                else:
                    print("Não é palíndromo")
            elif op == '0':
                break
            else:
                print("Opção inválida")

#Exercício 3
print([i ** 2 for i in range(1, 11)])

#Exercício 4
print([i for i in range(1, 21) if i % 2 == 0])

#Exercício 5
palavras = ["Python", "List", "Comprehension", "Exercícios"]

print([len(palavra) for palavra in palavras])

#Exercício 6
temperaturas = [0, 10, 20, 30, 40]

print([(temperatura * (9/5) + 32) for temperatura in temperaturas])

#Exercício 7
frutas = ["maçã", "banana", "uva", "morango", "abacaxi"]

print([fruta for fruta in frutas if len(fruta) > 5])

#Exercício 8
print(["Fizz" if i % 3 == 0 else i for i in range(1, 21)])