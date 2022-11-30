def move_spaces(the_increment):
    player_1_side = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4}
    print(f"Original position:", player_1_side)

    # Move to the right by 3 spaces
    player_1_side['2'] = player_1_side['2'] + the_increment
    print(player_1_side)


move_spaces(2)
