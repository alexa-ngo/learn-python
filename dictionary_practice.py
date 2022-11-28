girls = {'Pris': 'well rounded', 'Shirley': 'pretty', 'Olympians': 'strong', 'Dana': 'motivated', 'Lin': 'driven',
         'Shawn': 'smart', 'Alexa': 'super crafty', 'Alexa': 'super fast', 'Alexaz': 'super crafty',
         'Alexa': 'super fast'}
check_girls = {'Sabrina': 'diligent', 'Claire': 'creative', 'Alexa': "crafty"}

print('Dictionary before:', girls)
for key in girls.keys():
    print(key)

print('Dictionary after:', girls)
for key in sorted(girls.keys()):
    print(key)

# for keys in girls():
#     if keys not in girls:
#         print(keys, 'is not in the list of girls.')  # expect to see Sabrina and Claire
