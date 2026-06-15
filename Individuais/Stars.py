alt = int(input("Digite o tamanho da pirâmide: "))
a = '*'

for i in range (0, alt):
    print(f"{a:^200}")
    a = a + '*' * 2