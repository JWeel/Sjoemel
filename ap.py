import numpy as np
import csv

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

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
 

X = getData("cleanData.csv", "Benzine")

predict = DBSCAN(eps=1000.0, min_samples=500).fit_predict(X)
#labels = predict.labels_

n_clusters_ = len(set(predict)) - (1 if -1 in predict else 0)

count = 0
for dingetje in predict:
	if dingetje == -1:
#		print dingetje
		count += 1

#for p in predict:
#	print p
print predict
print n_clusters_
print count
print len(predict)
print "Accuracy = ", str(((len(predict) - count)) / float(len(predict)) * 100) + "%"
#labels = predict.labels_
#print labels
