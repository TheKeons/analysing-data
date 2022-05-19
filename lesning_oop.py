import numpy as np
import sys
import os
import matplotlib.pyplot as plt

os.chdir(sys.path[0])

with open('norges-befolkning.csv', 'r') as f:
    data = np.genfromtxt(f, delimiter=';', dtype=int, skip_header=1, usecols=[0, 1], unpack=True) # returns a 2d array
    

class Placeholder:
    def __init__(self, file) -> None:
        self.x = file[0]
        self.y = file[1]
        self.x1 = self.x[-1]
        self.y1 = self.y[-1] / 1000000
        self.average_growthrate_30 = (self.y[-1]- self.y[len(self.y) - 30]) / (self.x[-1] - self.x[len(self.y)-30])
        self.average_growthrate_15 = (self.y[-1] - self.y[len(self.y) - 15]) / (self.x[-1] - self.x[len(self.y)-15])
        self.average_growthrate_5 = (self.y[-1] - self.y[len(self.y) - 5]) / (self.x[-1] - self.x[len(self.y) - 5])
        self.x_prediction = range(2022, 2072)
        self.pred_30 = [self.point_slope_form(self.average_growthrate_30)(i) for i in self.x_prediction]
        self.pred_15 = [self.point_slope_form(self.average_growthrate_15)(i) for i in self.x_prediction]
        self.pred_5 = [self.point_slope_form(self.average_growthrate_5)(i) for i in self.x_prediction]

    def der(self):
        return [(self.y[i+1] - self.y[i]) / (self.x[i+1] - self.x[i]) for i in range(len(self.y) - 1)]

    def point_slope_form(self, growthrate):
        return lambda x: growthrate * (x - self.x1) + self.y1

    def plot(self, graph_type, goal):  
        match graph_type:
            case 1:
                self.plot_prediction(goal)
            case 2:
                self.plot_derivative(goal)
            case 3:
                self.plot_population(goal)

    def plot_prediction(self, goal):
        plt.plot(self.x, self.y)
        plt.plot(self.x_prediction, self.pred_30, label='Prediction for based on last 30 years')
        plt.plot(self.x_prediction, self.pred_15, label='Prediction for based on last 15 years')
        plt.plot(self.x_prediction, self.pred_5, label='Prediction for based on last 5 years')
        plt.title('Population prediction for the next 50 years')
        plt.xlabel('Year')
        plt.ylabel('Population in milions')
        plt.legend()
        if goal == 'save':
            plt.savefig('prediction.png')
        else:
            plt.show()

    def plot_derivative(self, goal):
        plt.plot(self.x[1:], [i * 1000000 for i in self.der()]) # times with a milion so that the growth rate is acurate to the actual population
        plt.title('Population growth rate')
        plt.xlabel('Year')
        plt.ylabel('Population growth rate')
        if goal == 'save':
            plt.savefig('growthrate.png')
        else:
            plt.show()

    def plot_population(self, goal):
        plt.plot(self.x, self.y)
        plt.title('Population')
        plt.xlabel('Year')
        plt.ylabel('Population in milions')
        if goal == 'save':
            plt.savefig('population.png')
        else:
            plt.show()


def main():
    placeholder_2 = Placeholder(data)
    placeholder_2.plot(2, 'plot')


if __name__ == '__main__':
    main()
