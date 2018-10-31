
# coding: utf-8

# Consulta Latitude Longitude
# 
# O código retorna a latitude e longitude.
# Para que o código funcione é necessário:
# 1. Instalar a lib googlemaps: pip install googlemaps
# 2. Criar uma **APY Key** no google: https://console.developers.google.com/apis/dashboard?pli=1
# 3. Como parâmetro pode ser passado: O endereço completo ou somente o cep

import googlemaps

def get_latitude_Longitude(cep):
    # Passando a APY KEY
    gmaps = googlemaps.Client(key='')
    
    try:
        # Efetua a localização da latitude e da longitude
        geocode_result = gmaps.geocode(cep)

        local = geocode_result[0]['geometry']['location']
        lat = local['lat']
        lng = local['lng']

        print(lat, lng)
    except:
        print('Erro ao localizar a Latitude/Longitude para o Cep: ' + cep)
        

get_latitude_Longitude('26600-000')

