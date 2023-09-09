import matplotlib.pyplot as plt


# read file, and return list()
def read_file(filename):
    data = list()
    with open(filename, "r") as file:
        for line in file:
            data.append(float(line.strip()))
    return data


def plot_fig(list_data):
    len_data = len(list_data)

    plt.plot(list(range(len_data)), list_data)
    plt.xlabel("Episodes")
    plt.ylabel("Rewards")
    plt.title("DQN on CartPole-v1")
    plt.show()

if __name__ == "__main__":
    data1 = read_file("/home/ranfr/Projects/Reinforcement/DQN/Data/data1_.txt")
    plot_fig(data1)
