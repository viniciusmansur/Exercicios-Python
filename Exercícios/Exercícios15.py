#Exercício 1
lista = [i for i in range(1, 101)]
chave = 73

def binary_search(lista, chave):
    inicial = 0
    final = len(lista) - 1
    print(lista)

    while inicial <= final:
        meio = (final + inicial) // 2
        print(lista[meio])
        if chave == lista[meio]:    
            return meio
        elif chave > lista[meio]:
            inicial = meio + 1
        else:
            final = meio - 1
    return -1

#Exercício 2
def fatorial(n):
    #caso base (parada)
    if n == 1:
        return n
    #n-ésimo caso
    else:
        return n * fatorial(n-1)

#Exercício 3
def analise_combinatoria(m, n):
    if n == 0:
        return 1
    elif m == n:
        return 1
    elif m < n:
        return 0
    elif m > n and m > 0 and n > 0:
        return analise_combinatoria(m - 1, n) + analise_combinatoria(m - 1, n - 1)

#Exercício 4
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Exercício 5:
def potencia(a, n):
    if n == 0:
        return 1 
    else:
        return a * potencia(a, n - 1)
