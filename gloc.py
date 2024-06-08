import requests, json, click, time
from os import name, system

def c():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

@click.command()
@click.option('-ip', help='IP address to geolocate.', required=True)

def geolocate(ip):
    r = requests.get('http://ip-api.com/json/' + ip)
    j = r.json()
    c()
    print('Geolocating {}'.format(j['query']))
    time.sleep(1)
    c()
    print('Latitude: {}'.format(str(j['lat'])))
    print('Longitude: {}'.format(str(j['lon'])))
    print('City: {}'.format(j['city']))
    print('Region/State: {}'.format(j['region']))
    print('Country: {}'.format(j['country']))
    print('Zip code: {}'.format(j['zip']))
    print('Timezone: {}'.format(j['timezone']))
    print('ISP: {}'.format(j['isp']))
    print('ORG: {}'.format(j['org']))
    print('AS: {}'.format(j['as']))

if __name__ == '__main__':
    geolocate()
