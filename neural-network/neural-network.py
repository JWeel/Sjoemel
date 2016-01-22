from sklearn.neural_network import MLPRegressor
import numpy as np
import csv
from Car import *


############################################
# install latest version of scikit to use MPLRegressor
# http://scikit-learn.org/stable/developers/contributing.html#git-repo

class SKV(csv.excel):
    delimiter = ","

csv.register_dialect("SKV", SKV)

def getData(dataFile, hoofdbrandstof):
    cars = []
    with open(dataFile, "rU") as csvfile:
        reader = csv.reader(csvfile, "SKV")
        reader.next()   # skip titles
        for row in reader:
            car = Car()
            car.fillAspects(row)
            if car.Hoofdbrandstof == hoofdbrandstof:
                cars.append(car)
    return cars



# Multi-layer Perceptron Regressor (neural network)
# http://scikit-learn.org/dev/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor
def neuralNetwork(cars):

    x = []
    y = []
    for car in cars:
        x.append(car.returnLinRegList())
        y.append(float(car.CO2uitstootgecombineerd))

    mlpr = MLPRegressor(hidden_layer_sizes=(8, ), activation='logistic', 
        algorithm='l-bfgs', alpha=0.4, learning_rate='constant',
        max_iter=1000, random_state=None, tol=0.0001, verbose=False,
        validation_fraction=0.1)

    mlpr.fit(x, y)
    print cars[-2].printType()
    print mlpr.predict(x[-2])

    print "layers:", mlpr.n_layers_
    print "outputs:", mlpr.n_outputs_

if __name__ == '__main__':
    cars = getData("cleanDataDummy.csv", "Benzine") 
    neuralNetwork(cars)
