import numpy as np
from tqdm import tqdm
from multiprocessing import mp


def prep_data(size=5000):
    x = np.random.normal(0, 1, size).T
    eps = np.random.normal(0, 0.25, size).T
    y = np.negative(np.ones((1, size))) + (0.5 * x) + (-2 * np.power(x, 2)) + (0.3 * np.power(x, 3)) + eps
    data = np.row_stack((x, y))
    return x, eps, y, data


def adaline(input, weight, learning_rate=0.00001, mode=0, size=5000):
    def bgd(input, w, learning_rate):
        w_out = dw = np.zeros((1, 4))
        for i in range(size):
            xi = input[0][i]
            yi = input[1][i]
            x = np.array([[1, xi, xi**2, xi**3]])
            y_pred = np.matmul(w, x.T)[0][0]
            for j in range(4):
                update = learning_rate * (yi - y_pred) * x[0][j]
                dw[0][j] = dw[0][j] + update
        for i in range(4):
            w_out[0][i] = w[0][i] + dw[0][i]
        return w_out

    def sgd(input, w, learning_rate):
        w_out = w
        for i in range(size):
            xi = input[0][i]
            yi = input[1][i]
            x = np.array([[1, xi, xi ** 2, xi ** 3]])
            y_pred = np.matmul(w, x.T)[0][0]
            for j in range(4):
                update = learning_rate * (yi - y_pred) * x[0][j]
                w_out[0][j] = w_out[0][j] + update
        return w_out

    wj = weight
    if mode == 0:
        wj = bgd(input, weight, learning_rate)
    elif mode == 1:
        wj = sgd(input, weight, learning_rate)
    else:
        exit(-1)
    return wj


def sigmoid():
    print("sigmoid")


def question_1(learning_rate=0.00001, rounds=1000, size=5000):
    # Prepare Data-points
    x, eps, y, data = prep_data(size)
    w_init = np.random.rand(1, 4)

    # Information (not required)
    print("learning rate = {}".format(learning_rate))
    print("rounds = {}".format(rounds))
    print("dataset size = {}".format(learning_rate))
    print("Beginning...")

    # Train Adaline
    wj = w_init
    w_true = np.array([-1, 0.5, -2, 0.3], np.float64)

    for i in tqdm(range(rounds), desc="(Adaline) Training..."):
        wj = adaline(data, wj, learning_rate, mode=0, size=size)
    print("Initial Weights: {}".format(w_init[0]))
    print("Final Weights: {}".format(wj[0]))
    print("True Weights: [-1, +0.5, -2, +0.3]")

    # Train SGD
    wj = w_init
    for i in tqdm(range(rounds), desc="(SGD) Training..."):
        wj = adaline(data, wj, learning_rate, mode=1, size=size)
    print("Initial Weights: {}".format(w_init[0]))
    print("Final Weights: {}".format(wj[0]))
    print("True Weights: [-1, +0.5, -2, +0.3]")

if __name__ == '__main__':
    learning_rate = 0
    training_rounds = 0
    '''
    while not(0 < learning_rate <= 1):
        try:
            learning_rate = float(input("Please enter a learning rate (larger than 0 and at most 1): "))
        except:
            print("Invalid input. I like floats.")
    while not(0 < training_rounds):
        try:
            training_rounds = int(input("Please enter the desired amount of training rounds (larger than 0): "))
        except:
            print("Invalid input. I like integers.")

    question_1(learning_rate, training_rounds)
    '''
    # Best Learning is 0.00001, 1000, 5000
    question_1(0.00001, 1000, 5000)