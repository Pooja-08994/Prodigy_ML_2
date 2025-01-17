# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Eh3DYLbnYX6I9lTZgE-al3nioe_96K1p
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


data = pd.read_csv('/content/Mall_Customers.csv')


print(data.head())
print(data.isnull().sum())


X = data[['Annual Income (k$)', 'Spending Score (1-100)']]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


k = 5
kmeans = KMeans(n_clusters=k, random_state=42)


kmeans.fit(X_scaled)
labels = kmeans.labels_

data['Cluster'] = labels


plt.figure(figsize=(10, 6))

<Figure size 1000x600 with 0 Axes>
<Figure size 1000x600 with 0 Axes>

for cluster in range(k):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Annual Income (k$)'], cluster_data['Spending Score (1-100)'],
                label=f'Cluster {cluster}')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            marker='x', color='black', label='Centroids', s=100)

plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Clusters of Customers')
plt.legend()
plt.show()

