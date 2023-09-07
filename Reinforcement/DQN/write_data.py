import csv


if __name__ == "__main__":
    list_data = list()
    with open("./DQN/Data/data1.txt", "r") as file:
        for data in file.readlines():
            data = data.strip()
            list_data.append(data)

    with open("./DQN/Data/data.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(list_data)