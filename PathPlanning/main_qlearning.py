import matplotlib.pyplot as plt
from environment import StandardEnv, print_agent
from qlearning import QLearning
from tqdm import tqdm
from random import randint



if __name__ == '__main__':
    col = 10
    row = 10
    obstacle = list()
    # obstacle = [7, 16, 22, 29, 34]  # row, col = 5, 10
    for i in tqdm(range(int(col * row * 0.1)), desc='Setting obstacle: '):
        obs = randint(0, col * row - 2)
        if obs not in obstacle:
            obstacle.append(obs)
    start = randint(0, col * row - 1)
    goal = randint(0, col * row - 1)
    if goal in obstacle:
        obstacle.remove(goal)
    if start in obstacle:
        obstacle.remove(start)

    #  create environment
    env = StandardEnv(col, row, obstacle, start, goal)
    env_heu = StandardEnv(col, row, obstacle, start, goal)
    epsilon = 0.1
    alpha = 0.1
    gamma = 0.9
    #  create agent
    agent = QLearning(col, row, epsilon, alpha, gamma)
    agent_heu = QLearning(col, row, epsilon, alpha, gamma)
    #  learning times
    num_episodes = col * row * 10
    reward_without_heuristic, reward_with_heuristic = list(), list()
    for i_episode in tqdm(range(num_episodes), desc='Episodes: '):
        #  Q-learning without heuristic policy
        episode_reward = 0
        state = env.reset()
        done = False
        while not done:
            action = agent.take_action(state)
            next_state, reward, done = env.step(action)
            episode_reward += reward
            agent.update(state, action, reward, next_state)
            state = next_state
        reward_without_heuristic.append(episode_reward)

        #  Q-learning with heuristic policy
        episode_reward_heu = 0
        state_heu = env_heu.reset()
        done = False
        action = randint(0, 3)
        while not done:
            action = agent_heu.take_action_heuristic(state_heu, goal, action)
            next_state_heu, reward, done = env_heu.step(action)
            episode_reward_heu += reward
            agent_heu.update(state_heu, action, reward, next_state_heu)
            state_heu = next_state_heu
        reward_with_heuristic.append(episode_reward_heu)
    
    # whether go to the end
    reach_end = agent.reach_end(start, goal)
    if reach_end:
        # print("Reach the end.")
        with open("./Data/if_or_not", "w") as file:
            file.write("Reach the end.")
    else:
        print("Not reach the end.")
        
    with open("./Data/reward_with_heuristic.txt", "w") as file:
        for item in reward_with_heuristic:
            file.write(str(item) + "\n")
    # show the first 10%
    num = int(num_episodes/10)
    # fig 1
    list_episodes = list(range(num_episodes))
    plt.subplot(2, 2, 1)
    plt.plot(list_episodes, reward_without_heuristic, label='without heuristic')
    plt.plot(list_episodes, reward_with_heuristic, label='with heuristic')
    plt.xlabel('Episodes')
    plt.ylabel('Rewards')
    plt.title('Q-learning with/without Heuristic Policy on Standard Environment')
    plt.legend()
    # fig 2
    plt.subplot(2, 2, 2)
    plt.plot(list_episodes[:num], reward_without_heuristic[:num], label='without heuristic')
    plt.plot(list_episodes[:num], reward_with_heuristic[:num], label='with heuristic')
    plt.xlabel('Episodes')
    plt.ylabel('Rewards')
    plt.title('Q-learning with/without Heuristic Policy on Standard Environment(First {})'.format(num))
    plt.legend()
    # fig 3
    plt.subplot(2, 2, 3)
    diff = list()
    zeros = list()
    up, down = 0, 0
    for i in range(num_episodes):
        diff.append(reward_with_heuristic[i] - reward_without_heuristic[i])
        zeros.append(0)
        if diff[i] > 0:
            up += 1
        else:
            down += 1
    print('up: {}'.format(up))
    print('down: {}'.format(down))
    plt.plot(list_episodes, diff)
    plt.plot(list_episodes, zeros)
    plt.xlabel('Episodes')
    plt.ylabel('Difference')
    plt.title('Difference between heuristic and no heuristic')
    # fig 4
    plt.subplot(2, 2, 4)
    plt.plot(list_episodes[:num], diff[:num])
    plt.plot(list_episodes[:num], zeros[:num])
    plt.xlabel('Episodes')
    plt.ylabel('Difference')
    plt.title('Difference between heuristic and no heuristic(First {})'.format(num))
    plt.show()

    # action_meaning = ['>', 'v', '<', '^']
    # print('Q-learning policy')
    # print_agent(agent, env, action_meaning, obstacle, start, goal)
    # print('\nQ-learning heuristic policy')
    # print_agent(agent_heu, env, action_meaning, obstacle, start, goal)
