# Exercício 1
dados = [
    {"dia": 12, "mes": 2, "ano": 2019, "temp": 30.5},
    {"dia": 18, "mes": 3, "ano": 2019, "temp": 29.5},
    {"dia": 22, "mes": 4, "ano": 2019, "temp": 28.5},
    {"dia": 17, "mes": 5, "ano": 2019, "temp": 26.4}
]
def main():
    for dado in dados:
        print(f"{dado["dia"]}/{dado["mes"]:02d}/{dado["ano"]}: Temperatura: {dado["temp"]}°C")

# Exercício 2
frutas = {
    "banana": "amarelo",
    "melancia": "verde",
    "mexirica": "laranja"
}
def main2():
    print(frutas["banana"])

    frutas["morango"] = "vermelho"
    print(frutas)

    frutas["banana"] = "roxo"
    print(frutas["banana"])

    frutas.pop("mexirica")
    print(frutas)

    for fruta in frutas.keys():
        print(fruta)

    print('---------')

    for fruta in frutas.values():
        print(fruta)

    if 'mexirica' in frutas:
        print("Fruta existente")
    else:
        print("Fruta não encontrada")

#Exercício 3
pessoas = {

}

def main3():
    qtd = int(input("Digite a quantidade de cadastro: "))
    for _ in range(qtd):
        nome = input("Digite o nome a pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        altura = float(input("Digite a  altura da pessoa: "))
        pessoas[nome] = [idade, altura]

    print(pessoas)

#Exercício 4
import requests

url = 'https://viacep.com.br/ws/01001000/json/'

a = requests.get(url)
b = a.json()

# print(b)

#Exercício 5
def main5():
    cep = input("Digite seu CEP: ")
    url = 'https://viacep.com.br/ws/'+cep+'/json/'

    resposta = requests.get(url)
    dicionario = resposta.json()
    print(f"O CEP {dicionario["cep"]} diz\nRua: {dicionario["logradouro"]}\nComplemento: {dicionario["complemento"]}\nUnidade: {dicionario["unidade"]}")
    print(f"Bairro: {dicionario["bairro"]}\nCidade: {dicionario["localidade"]}\nUF: {dicionario["uf"]}\nEstado: {dicionario["estado"]}")
    print(f"Região: {dicionario["regiao"]}")

#Exercício 6
def main6():
    pokemon = 'charizard'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    resposta = requests.get(url)
    dic = resposta.json()
    print(f"Nome do pokemon: {dic["name"]}\nTipo: {dic["types"][0]["type"]["name"]} | {dic["types"][1]["type"]["name"]}\nID: {dic["id"]}")

main6()