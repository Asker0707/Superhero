import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
data = response.json()

Hulk = {}
Captain_America = {}
Thanos = {}
for i in data:
    if i['name'] == "Hulk":
        Hulk['Hulk'] = (i['powerstats']['intelligence'])
    if i['name'] == "Captain America":
        Captain_America['Captain_Amercia'] = (i['powerstats']['intelligence'])
    if i['name'] == "Thanos":
        Thanos["Thanos"] = (i['powerstats']['intelligence'])
intelect_list = [Hulk, Captain_America, Thanos]

for i in intelect_list:
    winner = max(i.items())

print(f'Самый умный: {winner[0]} c интелектом {winner[1]}')

         