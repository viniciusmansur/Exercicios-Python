import requests

codclima = {
	"0": "Céu Limpo",
	"1": "Parcialmente Limpo",
	"2": "Pacialmente Nublado",
	"3": "Nublado",
	"45": "Nevoeiro",
	"48": "Nevoeiro de Geada",
	"51": "Garoa Leve",
	"53": "Garoa Moderada",
	"55": "Garoa Densa",
	"56": "Garoa Congelante Leve",
	"57": "Garoa Congelante Densa",
	"61": "Chuva Leve",
	"63": "Chuva Moderada",
	"65": "Chuva Forte",
	"66": "Chuva Congelante Leve",
	"67": "Chuva Congelante Forte",
	"71": "Neve Fraca",
	"73": "Neve Moderada",
	"75": "Neve Pesada",
	"77": "Neve em Grãos",
	"80": "Chuviscos Leves",
	"81": "Chuviscos Moderados",
	"82": "Chuviscos Pesados",
	"85": "Chuviscos de Neve Fracos",
	"86": "Chuviscos de Neve Pesados",
	"95": "Tempestade",
	"96": "Tempestade com Granizo Leve",
	"97": "Tempestade Pesada",
	"99": "Tempestade com Granizo Pesado"
}



def clima(codclima):
    local = input("Digite seu local no formato: Rua, Bairro, Cidade, País: ")
    urllocal = f"https://nominatim.openstreetmap.org/search?q={local}&format=json&limit=1"
    c = requests.get(urllocal, headers={"User-Agent": "MeuVerificadorDeClima/1.0"})
    d = c.json()
    lat = d[0]["lat"]
    lon = d[0]["lon"]

    urlclima = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,is_day&daily=temperature_2m_max,temperature_2m_min,weather_code'
    a = requests.get(urlclima)
    b = a.json()

    if b["current"]["is_day"]:
        dia = "Dia"
    else:
        dia = "Noite"

    print(f"Temperatura: {b["current"]["temperature_2m"]}°C\nUmidade do Ar: {b["current"]["relative_humidity_2m"]}%")
    print(f"Máxima/Mínima: {b["daily"]["temperature_2m_max"][0]}°C | {b["daily"]["temperature_2m_min"][0]}°C")
    print(f"Previsão de: {codclima[str(b["daily"]["weather_code"][0])]}\nÉ {dia} em {local}")

clima(codclima)
