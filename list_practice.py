def motivation(girls):
    if girls:
        for each_woman in girls:
            if each_woman == 'Olympians':
                print("Alexa will be physically strong like an Olympian")
            else:
                print(f'Alexa will be better than {each_woman}.')
    else:
        print("Please choose some people to compare to.")


girls = []
# girls = ['Pris', 'Shirley', 'Olympians', 'Dana', 'Lin', 'Shawn', 'Olympians']
motivation(girls)
