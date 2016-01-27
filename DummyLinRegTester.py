# Universiteit van Amsterdam - Kunstmatige Intelligentie BSc
# Leren en Beslissen Project - Sjoemel
# Jelmer Alphenaar, Tjalling Haije, Joseph Weel & Roderick van der Weerdt
# 27 januari 2016

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
    print "using Linear Regression for predictions..."
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

def dummyCO2(percentage, oldCO2):
    return float(oldCO2) * (1.0 - (percentage / 100.0))

def makeDummies(cars):
    nDummies = 21
    deviation = 5
    for i in range(0, nDummies):
        randomInt = np.random.randint(0,len(cars))
        cars[randomInt].Handelsbenaming = "Dummy" + str(deviation + i)
        cars[randomInt].CO2uitstootgecombineerd = str(dummyCO2((deviation + i), cars[randomInt].CO2uitstootgecombineerd))
    print "created", nDummies, "dummies in the dataset"  
    return cars

if __name__ == '__main__':
    cars = getData("benzineData.csv", "Benzine")
    data = getCarsList(cars)

    cars = makeDummies(cars)

    regressionModel = linreg(cars)
    predictions = predictionLinReg(cars)

    foundDummies = []
    for i in range(0, len(predictions)):
        prediction = predictions[i]
        if i > 20:
            break
        if prediction.car.Handelsbenaming.startswith("Dummy"):
            foundDummies.append(prediction.car.Handelsbenaming)
    for foundDummy in foundDummies:
        print foundDummy, "found"
    print len(foundDummies), "dummies found"