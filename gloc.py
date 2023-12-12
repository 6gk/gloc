import requests
import json
import click
import time
from os import name, system

def c():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

@click.command()
@click.option('--ip', '-ip', help='IP address to geolocate.', required=True)

def geolocate(ip):
    r = requests.get('http://ip-api.com/json/' + ip)
    c()
    print('Geolocating {}'.format(r.json()['query']))
    time.sleep(1.5)
    print('Latitude: {}'.format(str(r.json()['lat'])))
    print('Longitude: {}'.format(str(r.json()['lon'])))
    print('City: {}'.format(r.json()['city']))
    print('Region/State: {}'.format(r.json()['region']))
    print('Country: {}'.format(r.json()['country']))
    print('Zip code: {}'.format(r.json()['zip']))
    print('Timezone: {}'.format(r.json()['timezone']))
    print('ISP: {}'.format(r.json()['isp']))
    print('ORG: {}'.format(r.json()['org']))
    print('AS: {}'.format(r.json()['as']))

if __name__ == '__main__':
    geolocate()
