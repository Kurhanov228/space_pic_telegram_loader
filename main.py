import requests
from pprint import pprint
import telegram
import os, random
from time import sleep
api_key = "xJJxN6YcIogipDjWUaBalfQjKS8hdnH50exX9rcO"
params = {
        'api_key':'xJJxN6YcIogipDjWUaBalfQjKS8hdnH50exX9rcO',
}
while True:
    texnik_get_picture = f'https://api.nasa.gov/planetary/apod'
    response = requests.get(texnik_get_picture, params = params)
    download_picture_url = response.json()["url"]
    one_response = requests.get(download_picture_url)
    with open('imagest/моякартинка.jpg', "wb") as file:
        file.write(one_response.content)

    zapsuk = random.randint(1, 100)
    texnik_get_picture_space = f'https://api.spacexdata.com/v3/launches/{zapsuk}'
    print(zapsuk)
    two_response = requests.get(texnik_get_picture_space)
    number = 0
    for picture in two_response.json()['links']['flickr_images']:
        pprint(picture)
        texnik_get_picture_space = picture
        pictur = requests.get(texnik_get_picture_space)
        with open(f'imagest/моякартинка{number}.jpg', "wb") as file:
            number += 1
            file.write(pictur.content)


    bot = telegram.Bot(token= "5419320482:AAEnTVVK4k14CDCqqkKfdivGu-AsuaOoNwY")
    f = random.choice(os.listdir(f'imagest'))
    with open (f'imagest/{f}', "rb") as file:
        bot.send_photo("@nasddd", file)
    for phata in os.listdir(f'imagest'):
        os.remove(f'imagest/{phata}')
    sleep(120)
