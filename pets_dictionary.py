pet_1_dict = {'Animal Type': 'Monkey',
              'Owner': 'Dennis'}
pet_2_dict = {'Animal Type': 'Horse',
              'Owner': 'Riley'}
pet_3_dict = {'Animal Type': 'Dragon',
              'Owner': 'Alexa'}
pet_4_dict = {'Animal Type': 'Panther',
              'Owner': 'Roger'}

pets = [pet_1_dict, pet_2_dict, pet_3_dict, pet_4_dict]

for each in pets:
    print('The', each['Animal Type'], 'belongs to', each['Owner'] + '.')
