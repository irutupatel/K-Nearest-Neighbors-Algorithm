import sys
from math import sqrt


def getHackerrankInput():
    """
    :return:
    """
    input = list()
    train_data = list()
    test_data = list()
    for line in sys.stdin.readlines():
        sample = line.strip().split()
        refined_sample = list()
        for index, item in enumerate(sample):
            if index == 0:
                label = int(sample[0])
                refined_sample.append(label)
            else:
                attribute_to_value = item.split(":")
                value = float(attribute_to_value[1])
                refined_sample.append(value)
        if int(sample[0]) == 0:
            test_data.append(refined_sample)
        else:
            train_data.append(refined_sample)
    return train_data, test_data


def euclidean_distance(sample1, sample2):
    distance = float(0.0)
    # Index 0 column is label; so skip it
    for whichAttribute in range(1, len(sample1)):
        distance += (sample1[whichAttribute] - sample2[whichAttribute])**2
    return sqrt(distance)


def manhattan_distance(sample1, sample2):
    distance = float(0.0)
    for whichAttribute in range(1, len(sample1)):
        distance += abs(sample1[whichAttribute]-sample2[whichAttribute])
    return distance

def get_neighbors(test_sample, train_data, k=5):

    distances = list()
    for training_data in train_data:
        distance = euclidean_distance(sample1=test_sample, sample2=training_data)
        # distance = manhattan_distance(sample1=test_sample, sample2=training_data)
        label = training_data[0]
        distances.append((distance, training_data))
    distances.sort(key=lambda tup:tup[0])

    neighbors = list()
    for whichK in range(k):
        neighbors.append(distances[whichK][1])
    return neighbors


def KNN(train_data, test_data):
    """
    :param train_data:
    :param test_data:
    :return:
    """
    for testing_sample in test_data:
        neighbors = get_neighbors(test_sample=testing_sample,train_data=train_data)
        labels = [neighbor[0] for neighbor in neighbors]
        prediction = max(set(labels), key=labels.count)
        testing_sample[0] = prediction
    return testData


def get_input():
    # train_data = [[-1, -1, 1], [-1, 0, 1], [-1, 0, 2], [-1, 1, -1], [-1, 1, 0], [1, 1, 2], [1, 2, 2], [-1, 2, 3]]
    # test_data = [[0, 2, 1]]

    # train_data = [[1, 1.0, 1.0], [1, 1.0, 2.0], [1, 2.0, 1.0], [3, 2.0, 2.0], [1, 3.0, 1.0], [3, 3.0, 2.0],
    #               [3, 3.0, 3.0], [3, 4.5, 3.0]]
    # test_data = [[0, 1.0, 2.2], [0, 4.5, 1.0]]

    # train_data = [[2, 3, 3, 3, 2], [1, 3, 2, 4, 2], [2, 1, 2, 2, 2],
    #               [3, 1, 4, 2, 4], [2, 1, 2, 2, 2], [3, 2, 3, 4, 3],
    #               [3, 1, 5, 2, 1], [1, 3, 2, 3, 4], [2, 2, 5, 4, 3],
    #               [2, 2, 4, 3, 3], [2, 3, 5, 3, 4], [3, 2, 3, 2, 3],
    #               [3, 1, 5, 2, 2]]
    # test_data = [[0, 1, 2, 4, 4],[0, 3, 3, 1, 4]]

    train_data = [[4, 3, 3, 3, 3, 3], [3, 1, 3, 3, 3, 2], [3, 1, 3, 3, 3, 2],
                  [4, 3, 3, 3, 3, 3], [1, 1, 1, 3, 4, 3], [4, 3, 5, 3, 2, 2],
                  [3, 1, 3, 1, 4, 3], [3, 1, 5, 1, 2, 3], [4, 2, 2, 4, 4, 2],
                  [4, 2, 2, 3, 4, 2], [4, 1, 4, 4, 4, 3], [3, 1, 3, 3, 3, 2],
                  [3, 1, 3, 3, 3, 2], [3, 1, 3, 3, 3, 2]]
    test_data = [[0, 2, 3, 1, 1, 2], [0, 3, 5, 1, 4, 1], [0, 1, 3, 1, 2, 2],
                 [0, 2, 5, 2, 2, 3], [0, 3, 4, 2, 1, 3], [0, 2, 3, 4, 4, 2]]

    return train_data, test_data


if __name__ == '__main__':

    # trainData, testData = getHackerrankInput()
    trainData, testData = get_input()
    test_data_predicted = KNN(trainData,testData)
    for testSample in test_data_predicted:
        print(testSample[0])