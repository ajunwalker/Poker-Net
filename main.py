from game import Game
from network import Agent

def main():

    hidden_dims = [16, 16]

    env = Game()
    input_dim = env.observation_space.shape[0]
    output_dim = env.action_space.n
    agent = Agent(input_dim, output_dim, hidden_dims)

    for episode in range(2000):
        reward = run_episode(env, agent)
        print(episode, reward)




if __name__ == '__main__':
    main()
