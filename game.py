from game_helper import *
import numpy as np
from random import shuffle, randint
from random_agent import RandomAgent
from enumerations import enumerate_start_moves, enumerate_midgame_moves

class Game:

    def __init__(self):

        self.opponent = RandomAgent()
        self.total_turns = 5

    def reset(self):

        # Initialise player boards
        self.player_one = [
            np.zeros((4, 13), dtype=np.int32),
            np.zeros((4, 13), dtype=np.int32),
            np.zeros((4, 13), dtype=np.int32),
        ]

        self.player_two = [
            np.zeros((4, 13), dtype=np.int32),
            np.zeros((4, 13), dtype=np.int32),
            np.zeros((4, 13), dtype=np.int32),
        ]

        self.one_discard_pile = np.zeros((4, 13), dtype=np.int32)
        self.two_discard_pile = np.zeros((4, 13), dtype=np.int32)

        self.players = [self.player_one, self.player_two]
        self.turns = [0, 0]

        self.cards = [(i, j) for i in range(4) for j in range(13)]
        shuffle(self.cards)

        self.start_player = randint(0, 1)

        if self.start_player != 0:

            next_cards = []

            for i in range(5):
                idx = randint(0, len(self.cards) - 1)
                num = self.cards[idx]
                self.cards.pop(idx)
                next_cards.append(num)

            enumerations = enumerate_start_moves(next_cards)
            action = self.opponent.get_action(enumerations)
            self.players[1] = enumerations[action]
            self.turns[1] = 1

        next_cards = []

        for i in range(5):
            idx = randint(0, len(self.cards) - 1)
            num = self.cards[idx]
            self.cards.pop(idx)
            next_cards.append(num)

        self.enumerations = enumerate_start_moves(next_cards)
        available_actions = []

        for enumeration in self.enumerations:
            x_flat = np.array(self.players[0]).flatten()
            y_flat = np.array(enumeration).flatten()
            discard_flat = np.zeros((4, 13)).flatten()
            available_actions.append(np.append(np.append(x_flat, y_flat), discard_flat))
        return available_actions


    def step(self, action):

        self.players[0]  = self.enumerations[action]
        self.turns[0] += 1

        if self.turns[0] > 1:
            self.one_discard_pile = self.discards[action]

        if self.turns == [5, 5]:
            player_one_score = self.calculate_royalty(0)
            player_two_score = self.calculate_royalty(1)
            res = np.append(np.array(self.players[0]).flatten(), np.array(self.players[1]).flatten())
            return res, player_one_score - player_two_score, True

        next_cards = []

        for i in range(5):
            idx = randint(0, len(self.cards) - 1)
            num = self.cards[idx]
            self.cards.pop(idx)
            next_cards.append(num)

        if self.turns[1] == 0:
            enumerations = enumerate_start_moves(next_cards)
        else:
            enumerations, discards = enumerate_midgame_moves(next_cards, self.players[1], self.two_discard_pile)

        action = self.opponent.get_action(enumerations)
        self.players[1] = enumerations[action]
        self.turns[1] += 1

        if self.turns == [5, 5]:
            player_one_score = self.calculate_royalty(0)
            player_two_score = self.calculate_royalty(1)
            res = np.append(np.array(self.players[0]).flatten(), np.array(self.players[1]).flatten())
            return res, player_one_score - player_two_score, True

        next_cards = []

        for i in range(3):
            idx = randint(0, len(self.cards) - 1)
            num = self.cards[idx]
            self.cards.pop(idx)
            next_cards.append(num)

        self.enumerations, self.discards = enumerate_midgame_moves(next_cards, self.players[0], self.one_discard_pile)

        available_actions = []

        for enumeration, discard in zip(self.enumerations, self.discards):
            x_flat = np.array(self.players[0]).flatten()
            y_flat = np.array(enumeration).flatten()
            discard_flat = discard.flatten()
            available_actions.append(np.append(np.append(x_flat, y_flat), discard_flat))
        return available_actions, 0, False


    def play(self, player, row, suit, number):
        self.players[player][row][suit, number] = 1


    def calculate_royalty(self, player):

        row_points = [0, 0, 0]

        # Extract player
        player = self.players[player]

        # Check for pair on top row
        exists, score = has_pair(player[0])
        if exists:
            row_points[0] = score

        # Check for triple on top row
        exists, score = has_triple(player[0])
        if exists:
            row_points[0] = score

        # For middle and bottom rows
        for row in range(1, 3):

            pair, triple, straight, flush = False, False, False, False

            # Check for pair
            exists, _ = has_pair(player[row])
            if exists:
                pair = True

            # Check for triple
            exists, _ = has_triple(player[row])
            if exists:
                triple = True
                row_points[row] = 2 if row == 1 else 0

            # Check for straight
            if has_straight(player[row]):
                straight = True
                row_points[row] = 4 if row == 1 else 2

            # Check for flush
            if has_flush(player[row]):
                flush = True
                row_points[row] = 8 if row == 1 else 4

            # Check for full house
            if pair and triple:
                row_points[row] = 12 if row == 1 else 6

            # Check for quad
            if has_quad(player[row]):
                row_points[row] = 20 if row == 1 else 10

            # Check if straight flush
            if straight and flush:

                # Check if royal flush
                col_sums = str(tuple(np.sum(player[row], axis=0)))
                if col_sums == '(1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1)':
                    row_points[row] = 50 if row == 1 else 25

                else:
                    row_points[row] = 30 if row == 1 else 15

        return sum(row_points)

    def display(self, player):

        suits = {0: 'S', 1: 'H', 2: 'C', 3: 'D'}

        player = self.players[player]

        for row in range(3):
            print(str(row + 1) + ':', end='')
            for num in range(13):
                for suit in range(4):
                    if player[row][suit, num] == 1:
                        print(str(num + 1) + str(suits[suit]), end=' ')
            print()
