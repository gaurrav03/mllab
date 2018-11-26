

#just run both the programs and show the graph.



# K-Means Clustering

# Importing the libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris_dataset=load_iris()
X = iris_dataset["data"]


# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')



##########################################################################################
#EM algorithm


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris_dataset=load_iris()
X = iris_dataset["data"]
y=iris_dataset["target"]



from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=3)
gmm.fit(X)

y_kmeans = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')







