import json

rent = [2000, 3000, 5000, 7000, 11000, 13000]

filename = 'rent.json'
with open(filename, 'w') as f:
    json.dump(rent, f)