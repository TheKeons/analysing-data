import numpy as np
import sys
import os
import matplotlib.pyplot as plt

os.chdir(sys.path[0])

# Gets norges-befolkning.csv and puts the information into a 2D array named "data"
with open('norges-befolkning.csv', 'r') as f:
    data = np.genfromtxt(f, delimiter=';', dtype=int, skip_header=1, usecols=[0, 1], unpack=True) # returns a 2d array
    

class Placeholder:
    def __init__(self, file) -> None:
        # Splits "data" into two lists
        self.x = file[0]
        self.y = file[1]
        # x1 og y1 are set to the last values in x and y
        self.x1 = self.x[-1]
        self.y1 = self.y[-1]

        # Finds average growth over the last 5, 15 and 30 years
        # Uses the derivative (Δy / Δx) to find the growth rate
        self.average_growthrate_30 = (self.y[-1]- self.y[len(self.y) - 30]) / (self.x[-1] - self.x[len(self.y)-30])
        self.average_growthrate_15 = (self.y[-1] - self.y[len(self.y) - 15]) / (self.x[-1] - self.x[len(self.y)-15])
        self.average_growthrate_5 = (self.y[-1] - self.y[len(self.y) - 5]) / (self.x[-1] - self.x[len(self.y) - 5])
        
        # Gets list of y-values to draw prediction lines
        self.x_prediction = range(2022, 2072)
        self.pred_30 = [self.point_slope_form(self.average_growthrate_30)(i) for i in self.x_prediction]
        self.pred_15 = [self.point_slope_form(self.average_growthrate_15)(i) for i in self.x_prediction]
        self.pred_5 = [self.point_slope_form(self.average_growthrate_5)(i) for i in self.x_prediction]

    # Returns the derivative for all values of x in a list
    def der(self):
        return [(self.y[i+1] - self.y[i]) / (self.x[i+1] - self.x[i]) for i in range(len(self.y) - 1)]

    # Returns a linear function using the point slope formula
    def point_slope_form(self, growthrate):
        return lambda x: growthrate * (x - self.x1) + self.y1

    # Chooses which type of graph to make
    def plot(self, graph_type, goal):  
        match graph_type:
            case 1:
                self.plot_prediction(goal)
            case 2:
                self.plot_derivative(goal)
            case 3:
                self.plot_population(goal)

    # Plots prediction for future population growth based on last few years of growth into a graph
    def plot_prediction(self, goal):
        plt.plot(self.x, self.y)
        plt.plot(self.x_prediction, self.pred_30, label='Prediction for based on last 30 years')
        plt.plot(self.x_prediction, self.pred_15, label='Prediction for based on last 15 years')
        plt.plot(self.x_prediction, self.pred_5, label='Prediction for based on last 5 years')
        plt.title('Population prediction for the next 50 years')
        plt.xlabel('Year')
        plt.ylabel('Population in milions')
        plt.legend()
        # Picks wether to save or show graph
        if goal == 'save':
            plt.savefig('prediction.png')
        else:
            plt.show()

    # Plots the growth rate of the population over time into a graph
    def plot_derivative(self, goal):
        plt.plot(self.x[1:], [i * 1000000 for i in self.der(self.x, self.y)]) # times with a milion so that the growth rate is acurate to the actual population
        plt.title('Population growth rate')
        plt.xlabel('Year')
        plt.ylabel('Population growth rate')
        # Picks wether to save or show graph
        if goal == 'save':
            plt.savefig('growthrate.png')
        else:
            plt.show()

    # Plots a graph of population over time
    def plot_population(self, goal):
        plt.plot(self.x, self.y)
        plt.title('Population')
        plt.xlabel('Year')
        plt.ylabel('Population in milions')
        # Picks wether to save or show graph
        if goal == 'save':
            plt.savefig('population.png')
        else:
            plt.show()

# Instantiates the class and picks a setting
def main():
    placeholder_2 = Placeholder(data)
    # Shows a graph of population over time with prediciton for future population
    placeholder_2.plot(1, 'plot')
    #placeholder_2.plot(2, 'didyoueverhearthetragedyofdarthplagueisthewise?Ithoughtnot.ItsnotastorytheJediwouldtellyou.ItsaSithlegend.DarthPlagueiswasaDarkLordoftheSith,sopowerfulandsowisehecouldusetheforcetoinfluencethemidichlorianstocreatelife...')


if __name__ == '__main__':
    main()
