# Author: Alexa Ngo
# GitHub username: @alexa-ngo
# Date: 12-4-2022
# Description: Portfolio Project for the Mancala Game

from portfolio_project import Player

class Mancala:

    """ The class controls the functions of the game. """

    def __init__(self):
        """ The constructor makes a Mancala object with the data members of Player 1, Player 2, is_it_player_1_turn,
        and is_the_game_over. """
        self._player1 = None
        self._player2 = None
        self._is_the_game_over = False
        self._is_the_turn_over = None
        self._current_player = None
        self._opposing_player = None

    def create_player(self, name):
        """ Creates the player. The name is a string. If Player 1 does not exit yet, the name is first assigned to
        Player 1. If Player 1 already exists, the name is assigned to Player 2. If a third name is input, an Exception
        will be raised. """
        if self._player1 is None:
            self._player1 = Player(name)
        elif self._player2 is None:
            self._player2 = Player(name)
        else:
            raise Exception("Sorry, this is not valid.")

    def get_player(self, player_num):
        """ Returns the player number or an Exception message. """
        if player_num == 1:
            return self._player1
        elif player_num == 2:
            return self._player2
        else:
            raise Exception("Sorry, this is not valid.")

    def get_is_the_game_over(self):
        """ Returns whether the game is over. """
        return self._is_the_game_over

    def get_is_the_turn_over(self):
        """ Returns whether the turn is over. """
        return self._is_the_turn_over

    def play_game(self, player_index, pit_index):

        # is_game_over =  sum(current_player.get_pit()) == 0
        # is_turn_over = current_player.get_seeds_in_hand() == 0

        if player_index == 1:
            current_player = self.get_player(1)
            opposing_player = self.get_player(2)
        else:
            current_player = self.get_player(2)
            opposing_player = self.get_player(1)

        if pit_index <= 0 or pit_index > 6:
            return "Invalid number for pit index"
            is_game_over = True

        is_game_over = False

        while is_game_over is False:

            if is_game_over is True:
                break

            is_turn_over = False

            while is_turn_over is False:

                print('Initial pit list of opposing player:', opposing_player.get_pit())
                print('Initial pit list of current player:', current_player.get_pit())
                print('Current Player Store:', current_player.get_store())

                current_pit_index = pit_index - 1 # converts to zero based index
                # print(current_player.get_pit()[current_pit_index])

                value_in_current_pit_index = current_player.get_pit()[current_pit_index]
                for current_pit in range(0, value_in_current_pit_index):
                    current_player.remove_one_seed_from_current_player_pit_list(current_pit_index)
                    current_player.add_one_seed_to_player_hand()

                while current_player.get_player_hand != 0:

                    # Current Player Side
                    for current_pit in range(current_pit_index + 1, 6): # range goes from 0-6
                        if current_player.get_player_hand() == 0:
                            break
                        #
                        # if current_player.get_pit()[current_pit_index] == 0 and current_player.get_player_hand() == 1:
                        #     current_player.add_one_seed_to_current_player_pit_list(current_pit_index)
                        #     index_of_opponent = 5 - current_pit_index
                        #     while opposing_player.get_pit()[current_pit] != 0:
                        #         opposing_player.remove_one_seed_from_current_player_pit_list(index_of_opponent)
                        #         current_player.add_one_seed_to_store
                        #     current_player.remove_one_seed_from_current_player_pit_list(current_pit)
                        #
                        #     print('Initial pit list of opposing player:', opposing_player.get_pit())
                        #     print('Initial pit list of current player:', current_player.get_pit())
                        #     print('Current Player Store:', current_player.get_store())
                        #     print('Current Player Hand:')

                        #     print('\n')
                        #     print('Current_pit_index', current_pit_index)
                        #     print('Working pit list of current player:', current_player.get_pit())
                        #     print('Current Player Store:', current_player.get_store())
                        #     print('The opposing player pit index', opposing_player_pit_index)
                        #     print('Num of seeds in the opponent index', num_of_seeds_in_opponent_pit_index)

                        # # Removing seeds from the opponent index and adding seeds to own store:
                        #
                        # for current_pit in range(0, num_of_seeds_in_opponent_pit_index + 1):
                        #     current_player.add_one_seed_to_store()
                        #     opposing_player.remove_one_seed_from_current_player_pit_list(opposing_player_pit_index)
                        #
                        # print('\n')
                        # print('After removing: ')
                        # print('Working pit list of opponent player:', opposing_player.get_pit())
                        # print('Working pit list of current player:', current_player.get_pit())
                        # print('Current Player Store:', current_player.get_store())
                        # print('The opposing player pit index', opposing_player_pit_index)
                        # print('Num of seeds in the opponent index', num_of_seeds_in_opponent_pit_index)


                        # # current_player.remove_one_seed_from_current_player_pit_list(current_pit)

                        current_player.add_one_seed_to_current_player_pit_list(current_pit)
                        current_player.remove_one_seed_from_player_hand()

                    # Current Player Store
                    current_player.add_one_seed_to_store()
                    current_player.remove_one_seed_from_player_hand()
                    if current_player.get_player_hand() == 0:  # this is where we break out and start the loop again
                        break

                    if current_player.get_player_hand() == 0:
                        temp_player = current_player
                        current_player = opposing_player
                        opposing_player = temp_player
                        break  # This break will end up at the next line after the loop

                    print('\n')
                    # Opponent Side
                    if current_player.get_player_hand() > 0:
                        if current_player.get_player_hand() <= 6:  # 1-6 Seeds
                            num_of_seeds_for_range = 5 - current_player.get_player_hand()

                        if current_player.get_player_hand() > 6:
                            num_of_seeds_for_range = -1
                            num_of_seed_after_opponent_pit_list = current_player.get_player_hand() - 6

                        for current_pit in range(5, num_of_seeds_for_range, -1):
                            opposing_player.add_one_seed_to_current_player_pit_list(current_pit)
                            current_player.remove_one_seed_from_player_hand()

                    if current_player.get_player_hand() == 0:
                        temp_player = current_player
                        current_player = opposing_player
                        opposing_player = temp_player
                        break  # This break will end up at the next line after the loop
                    # print('Current pit list of opposing player:', opposing_player.get_pit())
                    # print('Current pit list of current player:', current_player.get_pit())
                    # print('Current Player Store:', current_player.get_store())
                    # print('Current Player Hand:', current_player.get_player_hand())

                    print('\n')
                    # Current Side Again
                    if current_player.get_player_hand() > 0:
                        print('The current player hand has this many seeds: ', current_player.get_player_hand())
                        if current_player.get_player_hand() <= 6:
                            num_of_seeds_for_range = 5 - current_player.get_player_hand()
                        if current_player.get_player_hand() > 6:
                            num_of_seeds_for_range = 6
                            num_of_seed_after_opponent_pit_list = current_player.get_player_hand() - 6

                        for current_pit in range(0, num_of_seeds_for_range):
                            current_player.add_one_seed_to_current_player_pit_list(current_pit)
                            current_player.remove_one_seed_from_player_hand()
                        print('Seeds in player hand after the second current loop: ', current_player.get_player_hand()) # expect 10

                    # Current Store Again
                    current_player.add_one_seed_to_store()
                    current_player.remove_one_seed_from_player_hand()
                    if current_player.get_player_hand() == 0:  # this is where we break out and start the loop again
                        break

                    if current_player.get_player_hand() == 0:
                        temp_player = current_player
                        current_player = opposing_player
                        opposing_player = temp_player
                        break  # This break will end up at the next line after the loop

                    print('\n')
                    # Opponent Side
                    if current_player.get_player_hand() > 0:
                        if current_player.get_player_hand() <= 6:  # 1-6 Seeds
                            num_of_seeds_for_range = 5 - current_player.get_player_hand()

                        if current_player.get_player_hand() > 6:
                            num_of_seeds_for_range = -1
                            num_of_seed_after_opponent_pit_list = current_player.get_player_hand() - 6

                        for current_pit in range(5, num_of_seeds_for_range, -1):
                            opposing_player.add_one_seed_to_current_player_pit_list(current_pit)
                            current_player.remove_one_seed_from_player_hand()
                    print('Current pit list of opposing player:', opposing_player.get_pit())
                    print('Current pit list of current player:', current_player.get_pit())
                    print('Current Player Store:', current_player.get_store())
                    print('HIIICurrent Player Hand:', current_player.get_player_hand())

                    print('\n')
                    # Current Side Again
                    if current_player.get_player_hand() > 0:
                        print('The current player hand has this many seeds: ', current_player.get_player_hand())
                        if current_player.get_player_hand() <= 6:
                            num_of_seeds_for_range = 5 - current_player.get_player_hand()
                        if current_player.get_player_hand() > 6:
                            num_of_seeds_for_range = 6
                            num_of_seed_after_opponent_pit_list = current_player.get_player_hand() - 6

                        for current_pit in range(0, num_of_seeds_for_range):
                            current_player.add_one_seed_to_current_player_pit_list(current_pit)
                            current_player.remove_one_seed_from_player_hand()

                    current_player.add_one_seed_to_store()
                    current_player.remove_one_seed_from_player_hand()
                    if current_player.get_player_hand() == 0:  # this is where we break out and start the loop again
                        break
                    break

                    print('Current pit list of opposing player:', opposing_player.get_pit())
                    print('Current pit list of current player:', current_player.get_pit())
                    print('Current Player Store:', current_player.get_store())
                    print('Current Player Hand:', current_player.get_player_hand())

                    #Current Player Side
                    print('Number of seeds in hand', current_player.get_player_hand())
                    if current_player.get_player_hand() > 0:
                        if current_player.get_player_hand() <= 6:
                            num_of_seeds_for_range = 5 - current_player.get_player_hand()
                            print('num_of_seeds_for_range when less than 6: ', num_of_seeds_for_range)

                        if current_player.get_player_hand() > 6:
                            num_of_seeds_for_range = -1
                            num_of_seed_after_current_pit_list = current_player.get_player_hand() - 6

                        for current_pit in range(0, num_of_seeds_for_range):  # range goes from 0-6
                            current_player.add_one_seed_to_current_player_pit_list(current_pit)
                            current_player.remove_one_seed_from_player_hand()

                        print('Current pit list of opposing player:', opposing_player.get_pit())
                        print('Current pit list of current player:', current_player.get_pit())
                        print('Current Player Store:', current_player.get_store())
                        print('Current Player Hand:', current_player.get_player_hand())

                # print('Current Player Side')
                # print('Pit list of opposing player:', opposing_player.get_pit())
                # print('Initial pit list of current player:', current_player.get_pit())
                # print('Current Player Store:', current_player.get_store())
                # print('Current number of seeds', current_player.get_player_hand())
                # print('\n')
                #
                #     #
                    #         if current_player.get_player_hand() == 0:
                    #             break
                    #
                    #         print('num_of_seeds_for_range when greater than 6: ', num_of_seeds_for_range)
                    #         print('num_of_seeds_for_range for current_pit_list when greater than 6: ', num_of_seed_after_current_pit_list)
                    #         print('Current_player hand', current_player.get_player_hand())
                    # current_player.get_player_hand = 0


                break
                # Execute a while loop to remove the seeds from the index
                # print(current_player.remove_one_seed_from_current_player_pit_list(current_pit_index))
                # print(current_player.get_pit())
                is_turn_over = True
            is_game_over = True


    #             for current_pit in range(pit_index, 6):
    #                 if current_player.get_player_hand() == 0:
    #                     break
    #                 current_player.add_one_seed_to_current_player_pit_list(current_pit)
    #                 current_player.remove_one_seed_from_player_hand()
    #
    #             if current_player.get_player_hand() == 0:
    #                 is_turn_over = True
    #                 temp_player = current_player
    #                 current_player = opposing_player
    #                 opposing_player = temp_player
    #                 break
    #
    #             if current_player.get_player_hand() >= 1:
    #                 current_player.add_one_seed_to_store()
    #
    #                 if self.player_get_extra_turn() is True:
    #                     current_player.place_seed_into_player_pit(pit_index)
    #
    #                 if current_player.get_player_hand() == 0:
    #                     #check to see if the game is over and update
    #                     self.is_the_game_over()
    #                     is_turn_over = True
    #                     break
    #
    #                 # if current_player._last_pit_index_landed_on != 99:
    #                 #     current_player.set_last_pit_index_landed_on_as_zero()
    #
    #             if is_game_over is True:
    #                 break
    #
    #             number_of_seeds_left = 5 - current_player.get_player_hand()
    #             if current_player.get_player_hand() > 0:
    #                 for current_pit in range(5, 1, -1):
    #                     print('hello')
    #                     break
    #              #       opposing_player.add_one_seed_into_opponent_pit_list(current_pit)
    #               #      current_player.deduct_one_seed_from_current_player_hand()
    #                     if current_player.get_player_hand() == 0:
    #                         is_turn_over = True
    #                         # temp_player = current_player
    #                         # current_player = opposing_player
    #                         # opposing_player = temp_player
    #                         break
    #
    #             for current_pit in range(pit_index + 1, 6):
    #                # self.process_last_seed_in_player_hand(pit_index)  # CHECK TO SEE IF IT IS THE LAST SEED
    #                # current_player.add_one_seed_to_pit_list(current_pit)
    #                 if current_player.get_player_hand() == 0:
    #                     break
    #
    #        # self.print_board()
    #             is_turn_over = True
    #         is_game_over = True



    # def withdraw_from_pit_into_player_hand(self,
    #                                        pit_index):  # player_index (1 or 2) and pit_index (1 or 2.. or 6)
    #     """ Withdraw from pit into player hand. """
    #
    #     if self._is_it_player_1_turn is True:
    #         self.get_player(1).withdraw_from_pit_into_player_hand(pit_index)
    #     else:
    #         self.get_player(2).withdraw_from_pit_into_player_hand(pit_index)
    #
    # def place_seed_into_player_pit(self, pit_index):
    #     """ Places seed into the specified player pit. """
    #
    #     if self._is_it_player_1_turn is True:
    #         self.get_player(1).add_one_seed_to_pit_list(pit_index)
    #     else:
    #         self.get_player(2).add_one_seed_to_pit_list(pit_index) # this might be the problem area
    #
    # def add_one_seed_to_player_store(self):
    #     """ Adds one seed to player store. """
    #     if self._is_it_player_1_turn is True:
    #         self.get_player(1).add_one_seed_to_store()
    #     else:
    #         self._is_it_player_1_turn is False
    #         self.get_player(2).add_one_seed_to_store()

    # def is_current_player_turn_change_to_opponent_turn(self):
    #     ## might have to change the logic here. I am thinking that after the player turn, it will be needed to be changed to False
    #     """ Checks to see if it is the current player turn. """
    #     if self._is_it_player_1_turn is True and self.get_player(1).get_player_hand() == 0:
    #         self.set_player1_turn('false')
    #     else:
    #         if self._is_it_player_1_turn is False and self.get_player(2).get_player_hand() == 0:
    #             self.set_player1_turn('true')
    #
    # def player_get_extra_turn(self):
    #     """ Player gets extra turn if the last seed lands in their own store.
    #     After the player turn, their turn should be set to false.
    #     The last pit visited should be 99. """
    #     if self.get_player(1).get_last_pit_index_landed_on() == 99 and \
    #             self.get_player(1)._has_last_touched_the_store_or_the_pit == 'Store' and \
    #             self._player2.get_the_last_pit_index_landed_on_with_displacement != 1 or 2 or 3 or 4 or 5 or 6:
    #     #       self._has_last_touched_the_store_or_the_pit == 'Store':
    #        # self.set_player1_turn('true')
    #         return 'player 1 take another turn'
    #
    #     if self.get_player(2).get_last_pit_index_landed_on() == 99 and \
    #             self.get_player(2)._has_last_touched_the_store_or_the_pit == 'Store' and \
    #             self._player1.get_the_last_pit_index_landed_on_with_displacement != 1 or 2 or 3 or 4 or 5 or 6:
    #    # if self._is_it_player_1_turn is True and self.get_player(2).get_last_pit_index_landed_on() == 99 and \
    #    #         self._has_last_touched_the_store_or_the_pit == 'Store':
    #        # self.set_player1_turn('false')
    #         return 'player 2 take another turn'
    #
    #     else:
    #         return 'the player does not get an extra turn'

    def process_last_seed_in_player_hand(self, pit_index):
        """ If the last seed in player hand is deposited into an empty pit, add the number of seeds in the opponent
        pit to store of the player to the store of the current player.
        """

        # if self.get_is_it_player1_turn is True:
        #     current_player = self.get_player(1)
        #     opposing_player = self.get_player(2)
        # else:
        #     current_player = self.get_player(2)
        #     opposing_player = self.get_player(1)

        if current_player.get_player_hand() != 1 or opposing_player.get_player_hand() != 1:
            return

        if sum(current_player.get_pit()) != 0 or sum(opposing_player.get_pit()) != 0:
            return

        current_player.place_seed_into_player_pit(pit_index)

        index_of_opponent_pit_index = current_player.get_the_index_across_the_added_seed()
        number_of_seeds_into_the_pit = opposing_player.get_pit[index_of_opponent_pit_index]

        for each_seed in range(0, number_of_seeds_into_the_pit):
            opposing_player.withdraw_from_pit_into_player_hand(index_of_opponent_pit_index)

        for each_seed in range(0, number_of_seeds_into_the_pit):
            current_player.add_one_seed_to_player_store

       # opposing_player.get_pit[index_of_opponent_pit_index] = 0 ### CHECKKK THIS

       # current_player.withdraw_from_pit_into_player_hand(pit_index) ## CHECK THISS

    def print_board(self):
        """ Prints the board in the specified results. """
        print('player1:')
        print('store:', self.get_player(1).get_store())
        print(self.get_player(1).get_pit())
        print('player2:')
        print('store:', self.get_player(2).get_store())
        print(self.get_player(2).get_pit())

    def return_winner(self):
        """ Returns the winner. The results may still be ongoing, there is a tie, and if there is a Winner. """
        the_game_ended = sum(self.get_player(1).get_pit()) == 0 or sum(self.get_player(2).get_pit()) == 0
        total_of_player1 = sum(self.get_player(1).get_pit()) + self.get_player(1).get_store()
        total_of_player2 = sum(self.get_player(2).get_pit()) + self.get_player(2).get_store()

        if sum(self.get_player(1).get_pit()) != 0 and sum(self.get_player(2).get_pit()) != 0:
            return 'Game has not ended'
        if the_game_ended and total_of_player1 == total_of_player2:
            return 'It is a tie'
        if the_game_ended and total_of_player1 > total_of_player2:
            return 'Winner is player 1:', self.get_player(1).get_name()
        else:
            return 'Winner is player 2:', self.get_player(2).get_name()

    def is_the_game_over(self):
        """ Returns 'Game is ended' if the game is over. """
        if sum(self._player1.get_pit()) == 0 or sum(self._player2.get_pit()) == 0:
            self._is_the_game_over = True
            return "Game is ended"
        else:
            self._is_the_game_over = False
        return self._is_the_game_over