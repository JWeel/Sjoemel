import numpy as np
from sklearn.cluster import KMeans
from Car import *
import csv
import matplotlib.pyplot as plt

class SKV(csv.excel):
    delimiter = ","

csv.register_dialect("SKV", SKV)

def getData(dataFile, hoofdbrandstof):
    cars = []
    with open(dataFile, "rU") as csvfile:
        reader = csv.reader(csvfile, "SKV")

        # skip titles
        reader.next()
        for row in reader:
            car = Car()
            car.fillAspects(row)
            if car.Hoofdbrandstof == hoofdbrandstof:
                cars.append(car.returnList())

    return cars

def anomalyDetection(data, clusters):
    anomalyCounter = 0
    for cluster in clusters:
        print "size Cluster:", len(cluster)
        clusterCO2 = []
        for car in cluster:
            clusterCO2.append(float(car[3]))

        mean = np.mean(clusterCO2)
        stdDev = np.sqrt(np.var(clusterCO2))

        twoUp = mean + (stdDev * 2.0)
        twoDown = mean - (stdDev * 2.0)

        for carCO2 in clusterCO2:
            if (twoUp < carCO2) or (twoDown > carCO2):
                anomalyCounter += 1

    print "anomalies:", anomalyCounter
    print ""



# see http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
# clusters = 10
# n_init = number of times run with different centroid seeds
# init = initialization method
# n_jobs = compute n_init in parallel 
# verbose = output
def kMeans(data, clusters):
    # clustering = KMeans(n_clusters=clusters, n_init=100,
    # init='random', n_jobs=4).fit_predict(data)
    clusteringData = KMeans(n_clusters=clusters, n_init=100,
    init='random', n_jobs=4).fit(data)
    
    clustering = clusteringData.labels_

    #print "cluster centroids:"
    clusteringData = clusteringData.cluster_centers_

    #print "total distance of each point to the nearest centroid:"
    #print clustering.inertia_

    print "data:", len(data)
    print "cluster", len(clustering)

    clusteredData = []
    for i in range(clusters):
        clusteredData.append([])
    for i in range(len(clustering)):
        clusteredData[clustering[i]].append(data[i])

    return clusteredData



if __name__ == '__main__':
    cars = getData("cleanData.csv", "Benzine")

    # kmeans with clusters = 8
    clusters = kMeans(data=cars, clusters=8)

    anomalyDetection(cars, clusters)

    # test for all clusters
    # plt.title("Anisotropicly Distributed Blobs")
    # plt.xlabel('amount of clusters')
    # plt.ylabel('Distance')

    # repetitions = 100
    # steps = 20

    # distances = []

    # # test kmeans for different k
    # for step in xrange(1,steps):
    #     print step , "/", steps

    #     # run the kmeans algorithm 100 times with random intialization and take the best
    #     km = KMeans(n_clusters=step, n_init=100, init='random', n_jobs=4).fit(cars)

    #     print km.inertia_

    #     distances.append(km.inertia_)
    #     # plot the total distance of each datapoint to its closest centroid
        

    # plt.plot(range(1,steps), distances)

    # plt.show()

