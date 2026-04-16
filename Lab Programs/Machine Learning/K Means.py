import pandas as pd
from sklearn.cluster import KMeans
data = pd.read_csv("data.csv")
X = data[['age','income']]
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
clusters = kmeans.predict(X)
data['Cluster'] = clusters
print(data)
