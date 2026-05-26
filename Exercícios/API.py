import requests

base_url = 'https://pokeapi.co/api/v2/pokemon/'

pokemon = input("Digite o pokemon que deseja ver: ").lower()

def process(name):
    url = f'{base_url}{name}'
    response = requests.get(url)
    if response.status_code == 200:
        poke = response.json()
        return poke
    else:
        return 'Erro ao conectar'


poke_info = process(pokemon)

print(f'Pokemon: {poke_info["name"]}\nId: {poke_info["id"]}\nTipo: {poke_info["types"]}')