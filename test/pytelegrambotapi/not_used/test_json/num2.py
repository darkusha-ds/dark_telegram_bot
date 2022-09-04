import json

with open('num2.json', 'r') as e:
    data = json.load(e)

for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)