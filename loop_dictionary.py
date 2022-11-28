# Make an empty list to store the points for Player1.
player_1_list = []

# Make the pits and the list for Player1.

for pits in range(0, 6):
    new_pits = {pits: 1}
    print(new_pits)
    player_1_list.append(new_pits)
print(player_1_list)
