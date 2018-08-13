from random import randint

class RandomAgent:

    def __init__(self):
        pass

    def get_action(self, choices):
        return randint(0, len(choices) - 1)
