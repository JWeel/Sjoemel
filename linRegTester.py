# ignore deprecated warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import numpy as np
from sklearn.cluster import KMeans
from Car import *
import csv

from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.neighbors import kneighbors_graph

from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

from sklearn import linear_model
from sklearn.cross_validation import train_test_split

class carPrediction:
    def __init__(self, car, CO2):
        self.car = car
        self.CO2 = CO2
        self.difference = ((float(self.car.CO2uitstootgecombineerd) - float(self.CO2)) / float(self.car.CO2uitstootgecombineerd)) * 100.0

    def returnKey(self):
        return self.difference


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

def getCarsList(cars):
    carsList = []
    for car in cars:
        carsList.append(car.returnList())
    return carsList

def linreg(cars):
    x = []
    y = []
    for car in cars:
        x.append(car.returnLinRegList())
        y.append(float(car.CO2uitstootgecombineerd))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1, random_state=42)
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    return regr

def multreg(cars):
    x = []
    y = []
    for car in cars:
        x.append(car.returnMultRegList())
        y.append(float(car.CO2uitstootgecombineerd))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1, random_state=42)
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    return regr

def clusterData(cars, clusters, nClusters):
    clusteredData = makeListOfLists(nClusters)
    for i in range(len(clusters)):
        clusteredData[clusters[i]].append(cars[i])
    return clusteredData

def predictionLinReg(cars):
    predictions = []
    predCumalative = 0
    for car in cars:
        #[predictionCO2] = regressionModel.predict(car.returnLinRegList())
        #predictions.append(predictionCO2)
        cars2 = list(cars)
        cars2.remove(car)
        [soloPredictionCO2] = (linreg(cars2).predict(car.returnLinRegList()))
        #[soloPredictionCO2] = (multreg(cars2).predict(car.returnMultRegList()))
        newCar = carPrediction(car, soloPredictionCO2)
        predictions.append(newCar)
        predCumalative += np.abs(newCar.difference)
    print len(predictions), "predictions made."
    pred = sorted(predictions, key = carPrediction.returnKey)
    print "average prediction Error:", predCumalative / float(len(predictions))
    return pred

if __name__ == '__main__':
    cars = getData("benzineDataDummys.csv", "Benzine")
    data = getCarsList(cars)

    print "looking for anomalies with Linear Regression"
    #regressionModel = linreg(cars)
    predictions = predictionLinReg(cars)
    #predictions = predictionLinReg(cars[0:100])

    for i in range(0, len(predictions)):
        prediction = predictions[i]
        if i > 20:
            break
        print prediction.car.printType(), "&", prediction.car.CO2uitstootgecombineerd, "&", prediction.CO2, "&", prediction.difference, """\\\\"""

    #print cars[-1].printType(), cars[-1].CO2uitstootgecombineerd