import numpy as np
from sklearn.cluster import KMeans
from Car import *
import csv
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.neighbors import kneighbors_graph

from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

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
        print "size Cluster:", len(cluster)
        clusterCO2 = []
        for car in cluster:
            clusterCO2.append(float(car.CO2uitstootgecombineerd))

        twoDown = np.mean(clusterCO2) - (np.sqrt(np.var(clusterCO2)) * 2.0)
        threeUp = np.mean(clusterCO2) + (np.sqrt(np.var(clusterCO2)) * 3.0)

        for i in range(len(clusterCO2)):
            #if threeUp < clusterCO2[i]:    #only low CO2 anomalies
            if twoDown > clusterCO2[i]:    #only low CO2 anomalies
                anomalies.append(cluster[i])

    print ""
    for anomaly in anomalies:
        print anomaly.printType()

    print "anomalies:", len(anomalies)


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
def kMeans(cars, data, nClusters):
    #cars = data
    #data = getCarsList(cars)

    clusteringData = KMeans(n_clusters=nClusters, n_init=100,
    init='random', n_jobs=4).fit(data)
    
    clusters = clusteringData.labels_

    #clusteringData = clusteringData.cluster_centers_

    clusteredData = makeListOfLists(nClusters)
    for i in range(len(clusters)):
        clusteredData[clusters[i]].append(cars[i])

    return clusteredData

def agglom(cars, data, n_clusters):
    #cars = data
    #data = getCarsList(cars)

    knn_graph = kneighbors_graph(data, 30, include_self=False)
    
    cluster = AgglomerativeClustering(n_clusters=n_clusters, connectivity=knn_graph, linkage='ward') # use ward / average / complete for different results
    model = cluster.fit(data)
    clusters = cluster.fit_predict(data)
    
    clusteredData = makeListOfLists(n_clusters)
    for i in range(len(clusters)):
        clusteredData[clusters[i]].append(cars[i])

    return clusteredData

def dbScan(cars, data, epsilon, minSamples):
    predict = DBSCAN(eps=epsilon, min_samples=minSamples).fit_predict(data)
    #labels = predict.labels_

    #n_clusters_ = len(set(predict)) - (1 if -1 in predict else 0)

    nClusters = len(set(predict))
    print "nClusters", nClusters

    clusteredData = makeListOfLists(nClusters)
    for i in range(len(predict)):
        clusteredData[predict[i]].append(cars[i])

    counter = 0
    for j in range(len(predict)):
        if predict[j] == -1:
            counter += 1
            print cars[j].printType()
    print "amount of -1:", counter

    print set(predict)

    return clusteredData


if __name__ == '__main__':
    cars = getData("cleanDataDummy.csv", "Benzine")
    data = getCarsList(cars)

    print "\n\n\nlooking for anomalies with k-means clustering"
    clusters = kMeans(cars, data, 5)                  # kmeans with clusters = 8
    anomalyDetection(clusters)

    print "\n\n\nlooking for anomalies with agglomerative clustering"
    clusters = agglom(cars, data, 5)                  # agglom with clusters = 5
    anomalyDetection(clusters)

    print "\n\n\nlooking for anomalies with dbScan"
    clusters = dbScan(cars, data, 500.0, 100)
    anomalyDetection(clusters)