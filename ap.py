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
 

"""

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

X = StandardScaler().fit_transform(X)
"""
X = getData("cleanData.csv", "Benzine")

# Compute DBSCAN
#db = DBSCAN(eps=0.3, min_samples=10).fit(X)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True

# Number of clusters in labels, ignoring noise if present.

predict = DBSCAN(eps=670.0, min_samples=1000).fit_predict(X)
#labels = predict.labels_

n_clusters_ = len(set(predict)) - (1 if -1 in predict else 0)

count = 0
for dingetje in predict:
	if dingetje == -1:
#		print dingetje
		count += 1

#for p in predict:
#	print p
#print predict
#print n_clusters_
print count
print len(predict)
print "Accuracy = ", str(((len(predict) - count)) / float(len(predict)) * 100) + "%"
#labels = predict.labels_
#print labels

#print('Estimated number of clusters: %d' % n_clusters_)
#print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
#print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
#print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
#print("Adjusted Rand Index: %0.3f"
#      % metrics.adjusted_rand_score(labels_true, labels))
#print("Adjusted Mutual Information: %0.3f"
#      % metrics.adjusted_mutual_info_score(labels_true, labels))
#print("Silhouette Coefficient: %0.3f"
#      % metrics.silhouette_score(X, labels))

##############################################################################
# Plot result
#import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
#unique_labels = set(labels)
#colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
#for k, col in zip(unique_labels, colors):
#    if k == -1:
#        # Black used for noise.
#        col = 'k'
#
#    class_member_mask = (labels == k)
#
#    xy = X[class_member_mask & core_samples_mask]
#    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#             markeredgecolor='k', markersize=14)
#
#    xy = X[class_member_mask & ~core_samples_mask]
#    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#             markeredgecolor='k', markersize=6)

#plt.title('Estimated number of clusters: %d' % n_clusters_)
#plt.show()
