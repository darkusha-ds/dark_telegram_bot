import json

with open('num1.json', 'r') as j:
    data = json.load(j)

for person in data['people']:
    print(person['name'])