class Player:

    def __init__(self):
        self._player1 = [4, 4, 4, 4, 4, 4]

    def get_player(self):
        return self._player1

    def add_seeds_to_pit(self, start_pos, working_number_of_seeds):
        player1_pits = player1.get_player()
        remaining_difference = working_number_of_seeds - 6
        return remaining_difference

    def seed_in_store(self, remaining_difference):
        store_seed_amount = []
        if remaining_difference >= 1:
            store_seed_amount.append(remaining_difference)
            remainder_to_add_to_player2 = remaining_difference - 1
            return remainder_to_add_to_player2

    def add_seeds_to_player2(self, remainder_to_add_to_player2):
        print(remainder_to_add_to_player2)


player1 = Player()
remaining_difference = player1.add_seeds_to_pit(0, 10)
print(player1.seed_in_store(remaining_difference))
