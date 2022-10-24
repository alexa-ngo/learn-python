import pickle

names = ['place_holder','William', 'Patrick', 'Jon', 'Tom', 'Peter', 'Colin', 'Sylvester',
         'Paul', 'Chris', 'David', 'Matt', 'Peter', 'Jodie']
dict = {}

with open('names.pkl', 'wb') as outfile:
    for each in range(0,13):
        dict[each] = names[each]
    pickle.dump(dict, outfile)

with open('names.pkl', 'rb') as infile:
    restored_dictionary = pickle.load(infile)

# check the restored_list
print(restored_dictionary)
