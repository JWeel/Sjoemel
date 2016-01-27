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
from Car import *
import csv

from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans
from sklearn.neighbors import kneighbors_graph

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

def anomalyDetection(clusters):
    anomalies = []
    for cluster in clusters:
        clusterAnomalies = []
        clusterCO2 = []
        for car in cluster:
            clusterCO2.append(float(car.CO2uitstootgecombineerd))

        print "size Cluster:", len(cluster), "- CO2 mean:", np.mean(clusterCO2)

        twoDown = np.mean(clusterCO2) - (np.sqrt(np.var(clusterCO2)) * 2)

        for i in range(len(clusterCO2)):
            if twoDown > clusterCO2[i]:    #only low CO2 anomalies
                clusterAnomalies.append(cluster[i])

        for anomaly in clusterAnomalies:
            print anomaly.printType(), "(", anomaly.CO2uitstootgecombineerd, ")"
            anomalies.append(anomaly)
        print ""

    print len(anomalies), "anomalies found."
    return anomalies


def getCarsList(cars):
    carsList = []
    for car in cars:
        carsList.append(car.returnList())
    return carsList

def makeListOfLists(size):
    clusteredData = []
    for _ in range(size):
        clusteredData.append([])
    return clusteredData


# see http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
# clusters = 10
# n_init = number of times run with different centroid seeds
# init = initialization method
# n_jobs = compute n_init in parallel 
# verbose = output
def kMeans(data, nClusters):
    clusteringData = KMeans(n_clusters=nClusters, n_init=100,
    init='random', n_jobs=4).fit(data)
    clusters = clusteringData.labels_
    #print "centers:", clusteringData.cluster_centers_
    return clusters

def agglom(data, n_clusters):
    knn_graph = kneighbors_graph(data, 30, include_self=False)
    
    cluster = AgglomerativeClustering(n_clusters=n_clusters, connectivity=knn_graph, linkage='ward') # use ward / average / complete for different results
    model = cluster.fit(data)
    
    return cluster.fit_predict(data)

def dbScan(cars, data, epsilon, minSamples):
    predict = DBSCAN(eps=epsilon, min_samples=minSamples).fit_predict(data)

    nClusters = len(set(predict))
    print "nClusters", nClusters
    print set(predict)
    return predict

def dbScanPrintNonClustered(cars, predict):
    print ""
    counter = 0
    for j in range(len(predict)):
        if predict[j] == -1:
            print cars[j].printType(), "(", cars[j].CO2uitstootgecombineerd, ")"
            counter += 1
    print counter, "cars have not been clustered\n"

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

def clusterData(cars, clusters, nClusters):
    clusteredData = makeListOfLists(nClusters)
    for i in range(len(clusters)):
        clusteredData[clusters[i]].append(cars[i])
    return clusteredData

def predictionLinReg(cars):
    predictions = []
    predCumalative = 0
    for car in cars:
        cars2 = list(cars)
        cars2.remove(car)
        [soloPredictionCO2] = (linreg(cars2).predict(car.returnLinRegList()))
        newCar = carPrediction(car, soloPredictionCO2)
        predictions.append(newCar)
        predCumalative += np.abs(newCar.difference)
    print len(predictions), "predictions made."
    sortedPredictions = sorted(predictions, key = carPrediction.returnKey)
    print "average prediction Error:", predCumalative / float(len(predictions))
    return sortedPredictions



if __name__ == '__main__':
    cars = getData("benzineData.csv", "Benzine")
    data = getCarsList(cars)

    nClusters = 4

    print "\n\n\nlooking for anomalies with k-means clustering, using", nClusters, "clusters."
    clusterLabels = kMeans(data, nClusters)
    clusters = clusterData(cars, clusterLabels, nClusters)
    anomalyDetection(clusters)

    print "\n\n\nlooking for anomalies with agglomerative clustering, using", nClusters, "clusters."
    clusterLabels = agglom(data, nClusters)
    clusters = clusterData(cars, clusterLabels, nClusters)
    anomalyDetection(clusters)

    print "\n\n\nlooking for anomalies with dbScan"
    clusterLabels = dbScan(cars, data, 1000.0, 100)
    dbScanPrintNonClustered(cars, clusterLabels)
    clusters = clusterData(cars, clusterLabels, len(set(clusterLabels)))
    anomalyDetection(clusters)

    print "\n\n\nlooking for anomalies with Linear Regression"
    predictions = predictionLinReg(cars)
    for i in range(0, len(predictions)):
        prediction = predictions[i]
        if i > 20:
            break
        print prediction.car.printType(), "&", prediction.car.CO2uitstootgecombineerd, "&", prediction.CO2, "&", prediction.difference, """\\\\"""