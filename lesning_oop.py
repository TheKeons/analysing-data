import numpy as np
import matplotlib.pyplot as plt

with open(r'C:\Users\katie\OneDrive\Dokumenter\GitHub\analysing-data\norges-befolkning.csv', 'r') as f:
    data = np.genfromtxt(f, delimiter=';', dtype=int, skip_header=1, usecols=[0, 1], unpack=True) # returns a 2d array
    

class Placeholder:
    def __init__(self) -> None:
        self.x = data[0]
        self.y = data[1]
        self.x1 = self.x[-1]
        self.y1 = self.y[-1]
        self.average_growthrate_30 = (self.y[-1]- self.y[len(self.y) - 30]) / (self.x[-1] - self.x[len(self.y)-30])
        self.average_growthrate_15 = (self.y[-1] - self.y[len(self.y) - 15]) / (self.x[-1] - self.x[len(self.y)-15])
        self.average_growthrate_5 = (self.y[-1] - self.y[len(self.y) - 5]) / (self.x[-1] - self.x[len(self.y) - 5])
        self.x_prediction = range(2022, 2072)

    def der(self):
        return [(self.y[i+1] - self.y[i]) / (self.x[i+1] - self.x[i]) for i in range(len(self.y) - 1)]

    def point_slope_form(self, growthrate):
        return lambda x: growthrate * (x - self.x1) + self.y1

    def make_prediction(self):
        pred_30 = [self.point_slope_form(self.average_growthrate_30)(i) for i in self.x_prediction]
        pred_15 = [self.point_slope_form(self.average_growthrate_15)(i) for i in self.x_prediction]
        pred_5 = [self.point_slope_form(self.average_growthrate_5)(i) for i in self.x_prediction]
        return pred_30, pred_15, pred_5