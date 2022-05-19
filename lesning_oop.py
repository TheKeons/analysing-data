import numpy as np
import sys
import os
import matplotlib.pyplot as plt

os.chdir(sys.path[0])

# Gets norges-befolkning.csv and puts the information into a 2D array named "data"
with open('norges-befolkning.csv', 'r') as f:
    norway = np.genfromtxt(f, delimiter=';', dtype=int, skip_header=1, usecols=[0, 1], unpack=True)   # returns a 2d array
    
with open('sveriges-befolkning.csv', 'r') as f:
    sweden = np.genfromtxt(f, delimiter=';', dtype=int, skip_header=1, usecols=[0, 1], unpack=True)   # returns a 2d array

class Placeholder:
    def __init__(self, file, file2) -> None:
        # Splits "data" into two lists
        self.x = file[0]
        self.t = file2[0]
        self.y = file[1] / 1000000
        self.k=file2[1] / 1000000
        # x1 og y1 are set to the last values in x and y
        self.x1 = self.x[-1]
        self.t1 = self.t[-1]
        self.y1 = self.y[-1]
        self.k1 = self.k[-1]

        # Finds average growth over the last 5, 15 and 30 years
        # Uses the derivative (Δy / Δx) to find the growth rate
        self.average_growth_rate_30 = (self.y[-1] - self.y[len(self.y) - 30]) / (self.x[-1] - self.x[len(self.y) - 30])
        self.average_growth_rate_15 = (self.y[-1] - self.y[len(self.y) - 15]) / (self.x[-1] - self.x[len(self.y) - 15])
        self.average_growth_rate_5 = (self.y[-1] - self.y[len(self.y) - 5]) / (self.x[-1] - self.x[len(self.y) - 5])

        self.average_growth_rate_30_2 = (self.k[-1] - self.k[len(self.k) - 30]) / (self.t[-1] - self.t[len(self.k) - 30])
        self.average_growth_rate_15_2 = (self.k[-1] - self.k[len(self.k) - 15]) / (self.t[-1] - self.t[len(self.k) - 15])
        self.average_growth_rate_5_2 = (self.k[-1] - self.k[len(self.k) - 5]) / (self.t[-1] - self.t[len(self.k) - 5])
        
        # Gets list of y-values to draw prediction lines
        self.x_prediction = range(2022, 2072)
        self.pred_30 = [self.point_slope_form(self.average_growth_rate_30, self.x1, self.y1)(i) for i in self.x_prediction]
        self.pred_15 = [self.point_slope_form(self.average_growth_rate_15, self.x1, self.y1)(i) for i in self.x_prediction]
        self.pred_5 = [self.point_slope_form(self.average_growth_rate_5, self.x1, self.y1)(i) for i in self.x_prediction]

        self.pred_30_2 = [self.point_slope_form(self.average_growth_rate_30_2, self.t1, self.k1)(i) for i in self.x_prediction]
        self.pred_15_2 = [self.point_slope_form(self.average_growth_rate_15_2, self.t1, self.k1)(i) for i in self.x_prediction]
        self.pred_5_2 = [self.point_slope_form(self.average_growth_rate_5_2, self.t1, self.k1)(i) for i in self.x_prediction]

    # Returns the derivative for all values of x in a list
    def der(self, x, y):
        return [(y[i+1] - y[i]) / (x[i+1] - x[i]) for i in range(len(y) - 1)]

    # Returns a linear function using the point slope formula
    def point_slope_form(self, growth_rate, x1, y1):
        return lambda x: growth_rate * (x - x1) + y1

    # Chooses which type of graph to make
    def plot(self, graph_type, goal, populations, names):  
        match graph_type:
            case 1:
                self.plot_prediction(goal, populations, names)
            case 2:
                self.plot_derivative(goal, populations, names)
            case 3:
                self.plot_population(goal, populations, names)

    # Plots prediction for future population growth based on last few years of growth into a graph
    def plot_prediction(self, goal, populations, names):
        match populations:
            case 'uno':
                plt.plot(self.x, self.y)
                plt.plot(self.x_prediction, self.pred_30, label=f'Next 30 years {names[0]}')
                plt.plot(self.x_prediction, self.pred_15, label=f'Next 15 years {names[0]}')
                plt.plot(self.x_prediction, self.pred_5, label=f'Next 5 years {names[0]}')

            case 'dos':
                plt.plot(self.t, self.k)
                plt.plot(self.x_prediction, self.pred_30_2, label=f'Next 30 years {names[1]}')
                plt.plot(self.x_prediction, self.pred_15_2, label=f'Next 15 years {names[1]}')
                plt.plot(self.x_prediction, self.pred_5_2, label=f'Next 5 years {names[1]}')
            
            case 'both':
                plt.plot(self.x, self.y, label=names[0])
                plt.plot(self.t, self.k, label=names[1])
                plt.plot(self.x_prediction, self.pred_30, label=f'Next 30 years {names[0]}')
                plt.plot(self.x_prediction, self.pred_30_2, label=f'Next 30 years {names[1]}')
                plt.plot(self.x_prediction, self.pred_15, label=f'Next 15 years {names[0]}')
                plt.plot(self.x_prediction, self.pred_15_2, label=f'Next 15 years {names[1]}')
                plt.plot(self.x_prediction, self.pred_5, label=f'Next 5 years {names[0]}')
                plt.plot(self.x_prediction, self.pred_5_2, label=f'Next 5 years {names[1]}')
        plt.title('Population prediction for the next 50 years')
        plt.xlabel('Year')
        plt.ylabel('Population in millions')
        plt.legend()
        # Picks whether to save or show graph
        if goal == 'save':
            plt.savefig('prediction.png')
        else:
            plt.show()

    # Plots the growth rate of the population over time into a graph
    def plot_derivative(self, goal, populations, names):
        match populations:
            case 'uno':
                plt.plot(self.x[1:], [i * 1000000 for i in self.der(self.x, self.y)])
            
            case 'dos':
                plt.plot(self.t[1:], [i * 1000000 for i in self.der(self.t, self.k)])
            
            case 'both':
                plt.plot(self.x[1:], [i * 1000000 for i in self.der(self.x, self.y)], label=names[0])
                plt.plot(self.t[1:], [i * 1000000 for i in self.der(self.t, self.k)], label=names[1])
        # times with a million so that the growth rate is accurate to the actual population
        plt.title('Population growth rate')
        plt.xlabel('Year')
        plt.ylabel('Population growth rate')
        plt.legend()
        # Picks whether to save or show graph
        if goal == 'save':
            plt.savefig('growth_rate.png')
        else:
            plt.show()

    # Plots a graph of population over time
    def plot_population(self, goal, populations, names):
        match populations:
            case 'uno':
                plt.plot(self.x, self.y)
            
            case 'dos':
                plt.plot(self.t, self.k)

            case 'both':
                plt.plot(self.x, self.y, label=names[0])
                plt.plot(self.t, self.k, label=names[1])

        plt.title('Population')
        plt.xlabel('Year')
        plt.ylabel('Population in millions')
        plt.legend()
        # Picks whether to save or show graph
        if goal == 'save':
            plt.savefig('population.png')
        else:
            plt.show()


# Instantiates the class and picks a setting
def main():
    placeholder_2 = Placeholder(norway, sweden)
    # Shows a graph of population over time with prediction for future population
    placeholder_2.plot(1, 'plot', 'uno', ('Norway', 'Sweden'))
    placeholder_2.plot(2, 'plot', 'both', ('Norway', 'Sweden'))
    placeholder_2.plot(3, 'plot', 'both', ('Norway', 'Sweden'))
    # placeholder_2.plot(2,
    # 'didyoueverhearthetragedyofdarthplagueisthewise?
    # Ithoughtnot.ItsnotastorytheJediwouldtellyou.ItsaSithlegend.DarthPlagueiswasaDarkLordoftheSith,
    # sopowerfulandsowisehecouldusetheforcetoinfluencethemidichlorianstocreatelife...')


if __name__ == '__main__':
    main()
