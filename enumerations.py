import numpy as np

def enumerate_midgame_moves(new_cards, placed_cards, discard_pile):

    moves = []
    discards = []

    # For each card in new cards
    for i in range(3):

        # Discard the card
        cards = new_cards[:i] + new_cards[i + 1:]

        # For each combination of the rest of the cards
        for row1 in range(3):
            for row2 in range(3):

                new_move = [
                    placed_cards[0].copy(),
                    placed_cards[1].copy(),
                    placed_cards[2].copy(),
                ]

                # Break up the cards
                suit1, num1 = cards[0]
                suit2, num2 = cards[1]

                new_move[row1][suit1][num1] = 1
                new_move[row2][suit2][num2] = 1

                if np.sum(new_move[0]) > 3:
                    continue

                if np.sum(new_move[1]) > 5:
                    continue

                if np.sum(new_move[2]) > 5:
                    continue

                discard_suit, discard_num = new_cards[i]

                new_discard_pile = discard_pile.copy()
                new_discard_pile[discard_suit][discard_num] = 1

                moves.append(new_move)
                discards.append(new_discard_pile)

    return moves, discards

def enumerate_start_moves(new_cards):

    cards = [
        np.zeros((4, 13), dtype=np.int32),
        np.zeros((4, 13), dtype=np.int32),
        np.zeros((4, 13), dtype=np.int32),
    ]

    moves = []

    suit1, num1 = new_cards[0]
    suit2, num2 = new_cards[1]
    suit3, num3 = new_cards[2]
    suit4, num4 = new_cards[3]
    suit5, num5 = new_cards[4]

    # For each combination of rows
    for row1 in range(3):
        for row2 in range(3):
            for row3 in range(3):
                for row4 in range(3):
                    for row5 in range(3):

                        new_move = [
                            cards[0].copy(),
                            cards[1].copy(),
                            cards[2].copy(),
                        ]

                        new_move[row1][suit1][num1] = 1
                        new_move[row2][suit2][num2] = 1
                        new_move[row3][suit3][num3] = 1
                        new_move[row4][suit4][num4] = 1
                        new_move[row5][suit5][num5] = 1

                        if np.sum(new_move[0]) > 3:
                            continue

                        if np.sum(new_move[1]) > 5:
                            continue

                        if np.sum(new_move[2]) > 5:
                            continue

                        moves.append(new_move)

    return moves
