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



# see http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
# clusters = 10
# n_init = number of times run with different centroid seeds
# init = initialization method
# n_jobs = compute n_init in parallel 
# verbose = output
def kMeans(data, clusters):
    clustering = KMeans(n_clusters=clusters, n_init=100,
    init='random', n_jobs=4).fit(data)

    print "cluster centroids:"
    print clustering.cluster_centers_

    print "total distance of each point to the nearest centroid:"
    print clustering.inertia_

    return 1



if __name__ == '__main__':
    cars = getData("cleanData.csv", "Benzine")

    # kmeans with clusters = 8
    kMeans(data=cars, clusters=8)

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

