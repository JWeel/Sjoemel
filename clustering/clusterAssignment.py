import csv #for reading in file
from Car import *

#splitts the data on the ';'.
class SKV(csv.excel):
    delimiter = ";"

csv.register_dialect("SKV", SKV)

def getData(dataFile):
    cars = []
    with open(dataFile, "rU") as csvfile:
        reader = csv.reader(csvfile, "SKV")
        for row in reader:
            car = Car()
            car.fillAspects(row)
            cars.append(car)
        print len(cars)
    return cars

def getClusterData(dataFile):
    clusters = []
    with open(dataFile, "rU") as csvfile:
        reader = csv.reader(csvfile, "SKV")
        for row in reader:
            aspects = row
            if clusters == []:
                for i in range(len(aspects) - 1):
                    clusters.append(Car())
            #print aspects[0]
            for i in range(1, len(aspects)):
                clusters[i-1].addAspect(aspects[0], aspects[i])
            #clusters.append(Car().fillAspects(row))
        #print len(cars)
    return clusters

def findClusters(cars, clusters):
    clusteredCars = []
    for i in range(len(clusters)):
        clusteredCars.append([])
    for car in cars:
        bestFit = 0
        bestFitValue = 999999999
        i = 0
        for cluster in clusters:
            fit = similarityCars(car, cluster)
            if fit < bestFitValue:
                bestFit = i
                bestFitValue = fit
            i += 1
        clusteredCars[int(bestFit)].append(car)
    return clusteredCars

if __name__ == '__main__':
    cars = getData("cleanData.csv")
    clusters = getClusterData("clusters1.csv")
    # i = 0
    # for car in cars:
    #     if car.Brandstofverbruikgecombineerd == '4.1':
    #         print car.returnPrintable()
    #         print i
    #         print float(car.Brandstofverbruikgecombineerd)
    #     i += 1
    clusteredCars = findClusters(cars, clusters)
    for cluster in clusteredCars:
        print len(cluster)