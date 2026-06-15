n1 = float(input("Digite o primeiro número da operação: "))
n2 = float(input("Digite o segundo número da operação: "))
print("Digite qual operação você deseja")
op = input("Soma (+), Subtração (-), Multiplicação (*) ou Divisão (/): ")
if op == '+':
    print(f"O resultado é {n1 + n2}")
elif op == '-':
    print(f"O resultado é {n1 - n2}")
elif op == '*':
    print(f"O resultado é {n1 * n2}")
elif op == '/':
    print(f"O resultado é {n1 / n2}")