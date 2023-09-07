from math import floor


class CliffWalkingEnv:
    def __init__(self, col, row):
        self.row = row
        self.col = col
        self.x = 0
        self.y = self.row - 1

    def step(self, action):
        # up, down, left, right
        change = []
        self.x = min(self.col - 1, max(0, self.x + change[action][0]))
        self.y = min(self.row - 1, max(0, self.y + change[action][1]))
        next_state = self.y * self.col + self.x
        reward = -1
        done = False
        if self.x == self.row - 1 and self.x > 0:
            done = True
            if self.x != self.col - 1:
                reward = -100
        return next_state, reward, done

    def reset(self):
        self.x = 0
        self.y = self.row - 1
        return self.y * self.col + self.x


class StandardEnv:
    def __init__(self, col, row, obstacle, start, goal):
        self.row = row
        self.col = col
        self.x = floor(start / col)
        self.y = start % col
        self.obstacle = obstacle
        self.start = start
        self.goal = goal

    def step(self, action):
        # right, down, left, up
        change = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        before_x = self.x
        before_y = self.y
        self.x = min(self.row - 1, max(0, self.x + change[action][0]))
        self.y = min(self.col - 1, max(0, self.y + change[action][1]))
        next_state = self.x * self.col + self.y
        if next_state in self.obstacle:  # hit obstacle
            done = True
            reward = -10
        elif self.x == before_x and self.y == before_y:  # hit the boundary
            done = True
            reward = -10
        elif next_state == self.goal:  # reach the goal
            done = True
            reward = 10
        else:
            done = False
            reward = -1
        return next_state, reward, done

    def reset(self):
        self.x = floor(self.start / self.col)
        self.y = self.start % self.col
        return self.start


def print_agent(agent, env, action_meaning, obstacle, start, end):
    for i in range(env.row):
        for j in range(env.col):
            if i * env.col + j == start:
                a = agent.best_action(i * env.col + j)
                pi_str = ''
                for k in range(len(action_meaning)):
                    pi_str += action_meaning[k] if a[k] > 0 else 'S'
                print(pi_str, end=' ')
            elif (i * env.col + j) in obstacle:
                print('XXXX', end=' ')
            elif (i * env.col + j) == end:
                print('EEEE', end=' ')
            else:
                a = agent.best_action(i * env.col + j)
                pi_str = ''
                for k in range(len(action_meaning)):
                    pi_str += action_meaning[k] if a[k] > 0 else 'o'
                print(pi_str, end=' ')
        print()
        