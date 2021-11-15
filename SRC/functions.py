import requests
from dotenv import load_dotenv
import os 
from functools import reduce
import operator

def geocode(direccion):
    """
    Esta función saca las coordenadas de la dirección que le pases
    """
    data = requests.get(f"https://geocode.xyz/{direccion}?json=1").json()
    try:
        return {"type": "Point", "coordinates": [data["latt"], data["longt"]]}
    except:
        return data

def get_parameters(city, *queries):
    """
    I have built this function to get the parameters of each query I want to see
    for each city
    """
    url_query = 'https://api.foursquare.com/v2/venues/explore'
    client_id = os.getenv("tok1")
    client_secret = os.getenv("tok2")
    d = {}
    for i in queries:
        parameters = {
            'client_id': client_id,
            'client_secret': client_secret,
            'v': '20180323',
            'll': f"{city[0]}, {city[1]}",
            'query': i,
            'radius': '5000'
        }
       
        resp = requests.get(url_query, params = parameters).json()
        d[i] = resp
    
    return d

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,diccionario)

def type_point(lista):
    return {"type":"Point", "coordinates": lista}

def clean_data(json, lista):
    info = {"nombre": "name", "latitud": ["location", "lat"], "longitud": ["location", "lng"], "categoría": ["categories", "shortName"]} 
    total = []
    
    for elemento in json:
        place = {}
        # for key, value in info.items():
        place["name"] = json.get("name")
        place["lat"] = json["location"]["lat"]
        place["lng"] = json["location"]["lng"]
        place["shortName"] = json["categories"][0]["shortName"]
            #place = {key: getFromDict(json, value) for key,value in info.items()}
    
        place["location"] = type_point([place['lat'], place['lng']])
        total.append(place)
    return place