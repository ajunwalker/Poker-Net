from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
import numpy as np

from random import random

from statistics import mean

from game import Game

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) # only difference

class Agent(object):

    def __init__(self, input_dim, hidden_dims=[32, 32]):

        self.model = Sequential()
        self.model.add(Dense(hidden_dims[0], input_dim=input_dim))

        for dim in hidden_dims[1:]:
            self.model.add(Activation('relu'))
            self.model.add(Dense(dim))

        self.model.add(Activation('relu'))
        self.model.add(Dense(1))
        self.model.add(Activation('sigmoid'))
        self.model.compile(loss='binary_crossentropy', optimizer=Adam(1e-3))
        self.model.summary()

        self.randomness = 0.5

    def get_action(self, state):

        action_prob = []

        count = 0
        for s in state:
            action_prob.append(self.model.predict(np.array([s]))[0][0])
            count += 1

        #idx = np.random.choice(np.arange(count), p=softmax(np.array(action_prob)))

        rand = random()
        if rand < self.randomness:
            idx = np.random.choice(np.arange(count))

            if self.randomness > 0.01:
                self.randomness *= 0.995

        else:
            idx = np.argmax(action_prob)

        return idx, state[idx]


def run_episode(env, agent):

    done = False
    S = []

    enumerations = env.reset()

    total_reward = 0

    while not done:

        idx, selection = agent.get_action(enumerations)

        enumerations, reward, done = env.step(idx)

        if done:

            if reward > 0:
                agent.model.fit(np.array(S), np.ones(4), verbose=0)

            elif reward < 0:
                agent.model.fit(np.array(S), np.zeros(4), verbose=0)

        else:
            S.append(selection)

    return reward

def main():

    hidden_dims = [256, 64]

    env = Game()
    input_dim = 364
    output_dim = 1
    agent = Agent(input_dim, hidden_dims)
    score = []

    for episode in range(100000):
        reward = run_episode(env, agent)

        if reward > 0:
            score.append(1)

        elif reward < 0:
            score.append(0)

        if len(score) > 50:
            score.pop(0)

        if len(score) > 0 and episode % 100 == 0:
            print('Episode:', episode, 'Average Wins:', mean(score))


if __name__ == '__main__':
    main()
