import json

names = ['place_holder','William', 'Patrick', 'Jon', 'Tom', 'Peter', 'Colin', 'Sylvester',
         'Paul', 'Chris', 'David', 'Matt', 'Peter', 'Jodie']
dict = {}

with open('names.json', 'w') as outfile:
    for each in range(0,13):
        dict[each] = names[each]
    json.dump(dict, outfile)

with open('names.json', 'r') as infile:
    restored_dictionary = json.load(infile)

# check the restored_list
print(restored_dictionary)
