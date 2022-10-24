import json

with open('SuperSquad.json', 'r') as infile:
    squad = json.load(infile)
print(squad["members"][1]["powers"][2])