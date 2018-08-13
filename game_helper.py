from game_rules import combos, hands
import numpy as np

def has_pair(row):

    # For each card number
    for i in range(13):

        # Compute number of times that card exists in row
        column_sum = int(np.sum(row[:, i]))

        # Check if pair of trip
        key = str((column_sum, i + 1))
        if column_sum == 2 and key in combos:
            return True, combos[key]

    return False, -1

def has_triple(row):

    # For each card number
    for i in range(13):

        # Compute number of times that card exists in row
        column_sum = int(np.sum(row[:, i]))

        # Check if pair of trip
        key = str((column_sum, i + 1))
        if column_sum == 3 and key in combos:
            return True, combos[key]

    return False, -1

def has_quad(row):

    # For each card number
    for i in range(13):

        # Compute number of times that card exists in row
        column_sum = int(np.sum(row[:, i]))

        if column_sum == 4:
            return True

    return False

def has_straight(row):

    # Get the sum of all columns
    col_sums = str(tuple(np.sum(row, axis=0)))

    if col_sums in hands:
        return True

    return False

def has_flush(row):

    # For each suit in row
    for suit in range(4):

        # If there are 5 cards of that suit, flush exists
        if np.sum(row[suit]) == 5:
            return True

    return False
