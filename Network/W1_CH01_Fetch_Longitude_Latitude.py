from geopy.geocoders import Nominatim
import requests


def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    # user_agent = '' # 빈칸으로 놓으면 안된다. 빈칸 아닌 어떤 값도 가능
    user_agent = 'David'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print(reply[0]['lat'], reply[0]['lon'])


if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    user_agent = 'David'
    location = Nominatim(user_agent=user_agent).geocode(address)
    print(location.latitude, location.longitude)
    geocode(address)

    address = 'Soongsil University'
    user_agent = 'David'
    location = Nominatim(user_agent=user_agent).geocode(address)
    print(location.latitude, location.longitude)
    geocode(address)

    address = 'Seoul City Hall'
    geocode(address)
