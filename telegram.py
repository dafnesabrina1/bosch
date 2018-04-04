""" 
py -m pip install
apiai
config
requests
uber_rides

https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq

hacer rest api con python, quiero mandar mi ubicacion origen y ubicacion destino, que python me devuelva
la estacion de mi bici mas cercana de mi origen y la mas cercana de mi destino
"""

""" 
rest api con python y tener un caso base de cómo llegar a plaza sania desde la expo:
en mi base de datos tendré 3 paradas para que sirva, la de la expo, la otra y la de sania
base de datos:
tabla de paradas lat, longitud y id
tabla de camiones, ruta, id
tabla de rutas tiene el id de la parada y el id del camion

hacer request para obtener la parada que está más cerca de mi ubicación y la parada de destino mas cercanna
llamada a mi api manda mi ubicacion actual y ubicacion en destino

"""



"""
MOOVIT
https://moovit.com/?from=Expo%20Guadalajara&to=Plaza%20Sania
pongo el lugar en mis parametros con un parse url y me encargo de redireccionar
obtener tiempo estimado con google maps como si fuera en carro y le sumo 15 minutos :/ 
"""

"""from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token='XM-7Rk-kM9Ew3IU_zoZSqRe0ZC0qxqkjAPrif3F6')
client = UberRidesClient(session)

latitud=20.6529143
longitud=-103.39176399999997

response = client.get_price_estimates(
    start_latitude=latitud,
    start_longitude=longitud,
    end_latitude=20.675329,
    end_longitude=-103.393,
    seat_count=1
)

estimate = response.json.get('prices')

print(products)"""
"""
id de cliente 
vuNWyx9N2E40O3KV2eirVvF4LMwm-wWQ
token servidor
XM-7Rk-kM9Ew3IU_zoZSqRe0ZC0qxqkjAPrif3F6
cliente secreto
cebl6Pe9dF78Y25_UeDQf_cEQuzqsSJc7txWHzwF
"""

"""import json
import requests
import time
from urlparse import urlparse as ur
import config


TOKEN = "551850379:AAGYwr0L1z_X3OS-54ONBIPnOQA-Q0z3lG0"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = ur.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
    """
"""
import apiai


CLIENT_ACCESS_TOKEN = 'ba90fc40794c4fb2b14025d12926b0d1'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "58e3cb0e6d324c84b7bd093042b698f4"

    request.query = "Hello"

    response = request.getresponse()

    print (response.read())


if __name__ == '__main__':
    main()
    
Uber

id de cliente 
vuNWyx9N2E40O3KV2eirVvF4LMwm-wWQ
token servidor
XM-7Rk-kM9Ew3IU_zoZSqRe0ZC0qxqkjAPrif3F6
cliente secreto
cebl6Pe9dF78Y25_UeDQf_cEQuzqsSJc7txWHzwF
"""