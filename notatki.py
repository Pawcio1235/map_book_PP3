import requests
from bs4 import BeautifulSoup

users: list[dict] = [
    {'name': 'Paweł', 'surname': 'Paszkowski', 'posts': 13},
    {'name': 'Janek', 'surname': 'Mielec', 'posts': 20},
    {'name': 'Maciej', 'surname': 'Przybytek', 'posts': 45},
    {'name': 'Bartosz', 'surname': 'Pietrasik', 'posts': 60},
    {'name': 'Tymoteusz', 'surname': 'Miszczak', 'posts': 21},
    {'name': 'Mateusz', 'surname': 'Matysiak', 'posts': 33},
    {'name': 'Jakub', 'surname': 'Orłowski', 'posts': 9},
]

miasto=input("podaj nazwę miejscowości")
def get_coords(miasto: str) ->list:
    adres_url=('https://pl.wikipedia.org/wiki/Bydgoszcz')
    response=requests.get(adres_url)
    response_html=BeautifulSoup(response.text,'html.parser')
    # print(response_html)
    latitude=float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude=(response_html.select('.longitude')[1].text.replace(',', '.'))
    print([latitude,longitude])
    return latitude,longitude
get_coords(miasto)

