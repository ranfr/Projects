import matplotlib.pyplot as plt


# read file, and return list()
def read_file(filename):
    data = list()
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def plot_fig(list_data):
    len_data = len(list_data)
    plt.plot(range(len_data), list_data)
    plt.xlabel("Episodes")
    plt.ylabel("Rewards")
    plt.title("DQN on CartPole-v1")
    plt.show()

if __name__ == "__main__":
    data1 = read_file("./DQN/Data/data1.txt")
    plot_fig(data1)

    data2 = read_file("./DQN/Data/data2.txt")
    plot_fig(data2)
    