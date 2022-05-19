import numpy as np
import matplotlib.pyplot as plt

with open(r'C:\Users\katie\OneDrive\Dokumenter\GitHub\analysing-data\norges-befolkning.csv', 'r') as f:
    data = np.genfromtxt(f, delimiter=';', dtype=int, skip_header=1, usecols=[0, 1], unpack=True) # returns a 2d array
    x = list(data[0]) # list of years
    y = [i / 1000000 for i in data[1]] # list of population devided by a milion so that it is easier to present
    

def der(x_list, y_list):
    return [(y_list[i+1] - y_list[i]) / (x_list[i+1] - x_list[i]) for i in range(len(y) - 1)]   # listcomp for the derivative


def one_point(x1, y1, growthrate):
    return lambda x: growthrate * (x - x1) + y1


def make_prediction(y, x):
    # predictions
    average_30 = (y[-1]- y[252]) / (x[-1] - x[252])
    average_15 = (y[-1] - y[267]) / (x[-1] - x[267])
    average_5 = (y[-1] - y[277]) / (x[-1] - x[277])

    x_prediction = [i for i in range(2022, 2072)]

    pred_30 = [one_point(x[-1], y[-1], average_30)(i) for i in x_prediction]
    pred_15 = [one_point(x[-1], y[-1], average_15)(i) for i in x_prediction]
    pred_5 = [one_point(x[-1], y[-1], average_5)(i) for i in x_prediction]

    return x_prediction, pred_30, pred_15, pred_5


def plot_population(x, y):
    # plotting the basic population graph
    plt.plot(x, y)
    plt.title('Population of Norway')
    plt.xlabel('Year')
    plt.ylabel('Population in milions')
    plt.show()


def plot_growthrate(x, y):
    # plotting the population growth rate
    plt.plot(x[1:], [i * 1000000 for i in der(x, y)]) # times with a milion so that the growth rate is acurate to the actual population
    plt.title('Population growth rate')
    plt.xlabel('Year')
    plt.ylabel('Population growth rate')
    plt.show()


def plot_prediction(x, y, x_prediction, pred_30, pred_15, pred_5):
    # plotting the population prediction
    plt.plot(x, y, label='Population')
    plt.plot(x_prediction, pred_30, label='Prediction for based on last 30 years')
    plt.plot(x_prediction, pred_15, label='Prediction for based on last 15 years')
    plt.plot(x_prediction, pred_5, label='Prediction for based on last 5 years')
    plt.title('Population prediction for the next 50 years')
    plt.xlabel('Year')
    plt.ylabel('Population in milions')
    plt.legend()
    plt.show()


def main():
    x_predicrion, pred_30, pred_15, pred_5 = make_prediction(y, x)
    plot_population(x, y)
    plot_growthrate(x, y)
    plot_prediction(x, y, x_predicrion, pred_30, pred_15, pred_5)


if __name__ == '__main__':
    main()
