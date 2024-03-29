import requests
from bs4 import BeautifulSoup

from code_files.constant_values import *


page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")

def get_location():
    location = soup.find('h1',class_='CurrentConditions--location--1YWj_').text
    return location
def get_temp():
    temperature = soup.find('span', class_='CurrentConditions--tempValue--MHmYY').text
    return f'{temperature}c'
def get_max_low_temp():
    max_low_temp = soup.find('div', class_='WeatherDetailsListItem--wxData--kK35q').text
    return max_low_temp
def get_humidity():
    vlaznost = soup.find('span',attrs={'data-testid': 'PercentageValue'}).text
    return vlaznost

def get_air_press():
    tlak = soup.find('span',class_='Pressure--pressureWrapper--3SCLm undefined').text
    """
    if petlje i len metodu sam koristio jer mi 'SCRAPA' Arrow up i Arrow down uz vrijednosti tlaka
    ovisno da li raste ili pada tlak u tom momentu, pa sam morao uklonit znakove
    """
    if len(tlak) > 15 and len(tlak) < 18:
        return tlak[8:]
    elif len(tlak) > 17:
        return tlak[10:]
    return tlak

def get_weathr():
    prognoza = soup.find('div',class_='CurrentConditions--phraseValue--mZC_p').text
    return prognoza


def house_temp():
    return '18°c'

def house_humidty():
    return '50%'

temperature_degree = soup.find('span', class_='CurrentConditions--tempValue--MHmYY').text
TEMPERATURE = int(temperature_degree[:-1])
def clothing_wear():
    if TEMPERATURE > 21:
        return 'T-Shirt\nShorts\nFlip Flops'
    elif TEMPERATURE < 22 and TEMPERATURE > 14:
        return 'Light jacket\nT-Shirt\nJeans\nShoes'
    elif TEMPERATURE < 15 and TEMPERATURE > 9:
        return 'Light jacket\nSweatshirt/Hoodie\nJeans\nShoes'
    elif TEMPERATURE < 10 and TEMPERATURE > 0:
        return 'Winter jacket\nweatshirt\nJeans\nThick socks\nBoots'
    else:
        return 'Winter jacket\nweatshirt\nJeans\nThick socks\nBoots\nHat & Gloves'



def accessories():
    if get_weathr() == 'Kiša' or get_weathr() == 'Slaba kiša' or get_weathr() == 'Pljusak kiše' or get_weathr() == 'Pljuskovi u blizini':
        return 'Umbrella'
    elif get_weathr() == 'Sunčano' or get_weathr() == 'Svijetlo':
        return 'Sunglasses'
    elif get_weathr() == 'Oblačno' or get_weathr()=='Pretežito oblačno':
        return 'Sunglasses & Umbrella'
    elif get_weathr() == 'Snijeg':
        return 'Hat & Gloves'
    else:
        return 'None'



