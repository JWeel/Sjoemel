# ignore deprecated warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import numpy as np
from Car import *
import csv
import matplotlib.pyplot as plt
import itertools

from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.neighbors import kneighbors_graph

from sklearn.cross_validation import train_test_split

# set plot size
from pylab import rcParams
rcParams['figure.figsize'] = 20, 10


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
    # print "centers:", clusteringData.cluster_centers_
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

def clusterData(cars, clusters, nClusters):
    clusteredData = makeListOfLists(nClusters)
    for i in range(len(clusters)):
        clusteredData[clusters[i]].append(cars[i])

    return clusteredData



def initPlots():
    # plt.figure(figsize=(20,10))
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    f.set_size_inches(30, 30)

    plt.title('Clusters plotted 2d')
    ax1.set_xlabel('Massaleegvoertuig')
    ax1.set_ylabel('CO2')

    ax2.set_xlabel('Cilinderinhoud')
    ax2.set_ylabel('CO2')

    ax3.set_xlabel('Vermogen')
    ax3.set_ylabel('CO2')

    ax4.set_xlabel('Zuinigheidslabel')
    ax4.set_ylabel('CO2')

    return ax1, ax2, ax3, ax4


def plotClusters(clusters, subplots):
    
    ax1 = subplots[0]
    colors = ["r", "b", "g", "y"]
    for i, cluster in enumerate(clusters):

        X1 = []
        X2 = []
        X3 = []
        X4 = []
        Y = []

        # append the attributes of each subplot to its list
        for car in cluster:
            Y.append(car.CO2uitstootgecombineerd)
            X1.append(car.Massaleegvoertuig)
            X2.append(car.Cilinderinhoud)
            X3.append(car.Vermogen)
            # convert a,b,c,d.. labels to 1,2,3,4
            X4.append(ord(car.Zuinigheidslabel.lower()) - 96)

        # plot the current cluster in each subplot
        subplots[0].scatter( X1, Y, color=colors[i])
        subplots[1].scatter( X2, Y, color=colors[i])
        subplots[2].scatter( X3, Y, color=colors[i])
        subplots[3].scatter( X4, Y, color=colors[i])




    #print clusters



if __name__ == '__main__':
    cars = getData("cleanDataDummy.csv", "Benzine")
    data = getCarsList(cars)

    nClusters = 4

    ax1, ax2, ax3, ax4 = initPlots()

    # kmeans clustering
    clusterLabels = kMeans(data, nClusters)                  
    # kmeans with clusters = nClusters
    clustersKMeans = clusterData(cars, clusterLabels, nClusters)

    # # agglomerative clustering
    # clusterLabels = agglom(data, nClusters)                  
    # # agglom with clusters = nClusters
    # clustersAgglom = clusterData(cars, clusterLabels, nClusters)

    # # db-scan clustering
    # clusterLabels = dbScan(cars, data, 1000.0, 100)
    # dbScanPrintNonClustered(cars, clusterLabels)
    # clustersDBscan = clusterData(cars, clusterLabels, len(set(clusterLabels)))


    plotClusters(clustersKMeans, [ax1, ax2, ax3, ax4])

    plt.show()
