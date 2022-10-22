import json

filename = 'rent.json'
with open(filename) as f:
    rent = json.load(f)

print(rent)