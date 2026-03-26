# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot_phase.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/26 11:32:54 by guilmira          #+#    #+#              #
#    Updated: 2026/03/26 14:14:36 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
import pandas
import matplotlib.pyplot as plt
from prediction_phase import theta_reader

class dotPlotter:
    #Constructor
    def __init__(self, dataset):
        self._dataset = dataset
        self._x = []
        self._y = []        
        
    def file_reader(self):
        print(f"Loading data from {self._dataset} into object")
        dataFrame = pandas.read_csv(self._dataset)
        
        self._x = dataFrame.iloc[:,0].tolist()
        self._y = dataFrame.iloc[:,1].tolist()
    
    def cloud_generator(self):
        plt.plot(self._x, self._y, "go")
    
    def line_generator(self, slope=None, intercept=None):
        if slope is not None and intercept is not None:
            x_line = [min(self._x), max(self._x)]
            y_line = [x_line[0] * slope + intercept, x_line[1] * slope + intercept]
    
        plt.plot(x_line, y_line, "r-")
        
    def generate_file(self):
        plt.savefig("result.png")

if __name__ == '__main__' :
    plotter = dotPlotter("data.csv")
    
    theta_set, slope, intercept = theta_reader("theta.txt")

    plotter.file_reader()
    plotter.cloud_generator()
    if theta_set is not False:
        plotter.line_generator(slope, intercept)
    plotter.generate_file()
   