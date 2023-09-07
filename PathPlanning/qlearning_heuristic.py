from environment import StandardEnv, print_agent
import matplotlib.pyplot as plt
import numpy as np


class QLearningHeuristic:
    def __init__(self, col, row, epsilon, alpha, gamma, n_action=4):
        self.q_table = np.zeros([row * col, n_action])
        self.n_action = n_action
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def take_action(self, state, goal):
        if np.random.random() < self.epsilon:
            # heuristic policy
            choice = np.random.randint(2)
            if state < goal:
                action = 2 * choice
            else:
                action = 2 * choice + 1
        else:
            action = np.argmax(self.q_table[state])
        return action

    def best_action(self, state):
        arg_q_max = np.argmax(self.q_table[state])
        a = [0 for _ in range(self.n_action)]
        a[arg_q_max] = 1
        return a

    def update(self, s0, a0, r, s1):
        td_error = r + self.gamma * np.max(self.q_table[s1]) - self.q_table[s0, a0]
        self.q_table[s0, a0] += self.alpha * td_error


if __name__ == '__main__':
    col = 10
    row = 5
    obstacle = [7, 16, 22, 29, 34]
    goal = 49
    env = StandardEnv(col, row, obstacle, goal)
    np.random.seed(0)
    epsilon = 0.1
    alpha = 0.1
    gamma = 0.9
    agent = QLearningHeuristic(col, row, epsilon, alpha, gamma)
    num_episodes = 500
    return_list = []
    for i_episode in range(num_episodes):
        episode_return = 0
        state = env.reset()
        done = False
        while not done:
            action = agent.take_action(state, goal)
            next_state, reward, done = env.step(action)
            episode_return += reward
            agent.update(state, action, reward, next_state)
            state = next_state
        return_list.append(episode_return)

    episodes_list = list(range(len(return_list)))
    plt.plot(episodes_list, return_list)
    plt.xlabel('Episodes')
    plt.ylabel('Returns')
    plt.title('Q-learning on {}'.format('Standard Environment'))
    plt.show()

    action_meaning = ['^', 'v', '<', '>']
    print('Q-learning heuristic policy')
    print_agent(agent, env, action_meaning, obstacle, [goal])