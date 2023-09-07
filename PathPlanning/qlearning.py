import numpy as np
from math import floor
from random import randint


class QLearning:
    def __init__(self, col, row, epsilon, alpha, gamma, n_action=4):
        self.q_table = np.zeros([row * col, n_action])
        self.n_action = n_action
        self.col = col
        self.row = row
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def take_action(self, state):
        if np.random.random() < self.epsilon:
            action = np.random.randint(self.n_action)
        else:
            action = np.argmax(self.q_table[state])
        return action

    def take_action_heuristic(self, state, goal, pre_action):
        cur_x = floor(state / self.col)
        cur_y = state % self.col
        goal_x = floor(goal / self.col)
        goal_y = goal % self.col
        if np.random.random() < self.epsilon:
            #  heuristic policy
            if cur_x < goal_x and cur_y < goal_y:
                action = randint(0, 1)
            elif cur_x > goal_x and cur_y > goal_y:
                action = 2 + randint(0, 1)
            elif cur_x < goal_x and cur_y > goal_y:
                action = 1 + randint(0, 1)
            elif cur_x > goal_x and cur_y < goal_y:
                action = 3 * randint(0, 1)
            elif cur_x == goal_x:
                action = 2 * randint(0, 1)
            elif cur_y == goal_y:
                action = 1 + 2 * randint(0, 1)
            else:
                action = pre_action + randint(-1, 1)
                # action = randint(0, 3)
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

    def reach_end(self, start, end):
        distance = 0
        x = int(start / self.col)
        y = int(start % self.col)
        state = start
        change = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while distance < self.col + self.row:
            action = change[np.argmax(self.q_table[state])]
            x += action[0]
            y += action[1]
            distance += 1
            state = x * self.col + y
            if state == end:
                return True
        return False

