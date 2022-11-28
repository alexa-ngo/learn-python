dmv_information = {'name': 'Alexa',
                   'height': 'short',
                   'city': 'SunnyTown',
                   'occupation': 'future programmer'}

for information, data in dmv_information.items():
    print(f"{information.title()} has the following information: {data.title()}.")
