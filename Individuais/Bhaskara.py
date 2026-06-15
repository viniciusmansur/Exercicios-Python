a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print(f"{a}x² + ({b}x) + {2}")

delta = b ** 2 - 4 * a * c

x1 = ((b * -1) + (delta**(1/2))) / (2*a)
x2 = ((b * -1) - (delta**(1/2))) / (2*a)

print(f"A primeira raiz é igual a {x1} e a segunda é igual a {x2} ")
