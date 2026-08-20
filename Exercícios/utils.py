def contvog(texto):
    cont = 0
    for letra in texto:
        if letra in "AEIOUaeiou":
            cont += 1
    return cont

def revpala(texto):
    return texto[::-1]

def contpal(texto):
    cont = 1
    for letra in texto:
        if letra == ' ':
            cont += 1
    return cont

verpali = lambda texto: texto == texto[::-1]