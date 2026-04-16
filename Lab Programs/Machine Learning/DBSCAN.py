import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("data.csv")
X = data[['age', 'income']]
X = StandardScaler().fit_transform(X)
model = DBSCAN(eps=0.5, min_samples=3)
clusters = model.fit_predict(X)
print("Cluster labels:")
print(clusters)
data['Cluster'] = clusters
print(data)
