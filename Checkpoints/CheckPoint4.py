# Exercício 1
def f(x):
    if x <= -2:
        return x ** 3 + 3 * x - 4
    elif x < 0:
        return 2 * x + 5
    elif x < 4:
        return  x ** (1/2)
    elif x < 6:
        return x ** 3 - 3 * x ** 2 - 10 * x
    elif x < 8:
        return x ** 2 - 4 * x - 20
    else:
        return 20

# Exercício 2
def matriz(c, l):
    m = []

    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(i * c + j + 1)
        m.append(linha)

# Exercício 3
def dimensao(matriz):
    return len(matriz), len(matriz[0])

# Exercício 4
def maior(matriz):
    max = matriz[0][0]
    imax = 0
    jmax = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > max:
                max = j
                jmax = j
                imax = i

    return [max, imax, jmax]

# Exercício 5
# a)
desc = lambda x: x * 0.9

# b)
precos = [10.0, 23.5, 7.99, 100.0]
precos2 = [desc(i) for i in precos]

# c)
precos3 = [desc(i) for i in precos if desc(i) > 20]