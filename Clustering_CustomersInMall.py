import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers_data = pd.read_csv('Learning_Dataset/clustering-python-master/Customer_in_Mall/Mall_Customers.csv')
print(customers_data.head())
customers_data = customers_data.drop('CustomerID', axis=1)

### Feature Transformation
from sklearn.preprocessing import LabelEncoder
encode = LabelEncoder()

# Converting Genders to numbers
encoded_sex = encode.fit_transform(customers_data.iloc[:, 0])
customers_data['Genre'] = encoded_sex
print(customers_data.head())

#pairplot to analyse the correlation between parameters
plt.figure(1)
sns.pairplot(customers_data)

# Applying principal component analysis on our data
# Getting Eigenvalues and Loading Scores
from sklearn.decomposition import PCA
pca_reducer = PCA(n_components=2)
reduced_data = pca_reducer.fit_transform(customers_data)
print(reduced_data.shape)

from sklearn.cluster import KMeans
km = KMeans(n_clusters=5)
cluster = km.fit(reduced_data)

plt.figure(2)
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], label='Datapoints')
plt.scatter(cluster.cluster_centers_[:, 0], cluster.cluster_centers_[:, 1], label='Clusters')
plt.title("Sklearn version of KMeans")
plt.legend()

# Using our designed algorithm from Kmean_numpy class
from Kmean_numpy_scipt import *
km_numpy = KMeans_numpy(n_clusters=5, tolerance=0.0001)

clusters, clusterd_data = km_numpy.fit(reduced_data)
clusters = np.array(clusters)

cluster_one_data = np.array(clusterd_data[0])
cluster_two_data = np.array(clusterd_data[1])
cluster_three_data = np.array(clusterd_data[2])
cluster_four_data = np.array(clusterd_data[3])
cluster_five_data = np.array(clusterd_data[4])

plt.figure(figsize=(12, 6))
plt.scatter(cluster_one_data[:, 0], cluster_one_data[:, 1], c='r', label='Cluster One')
plt.scatter(cluster_two_data[:, 0], cluster_two_data[:, 1], c='b', label='Cluster two')
plt.scatter(cluster_three_data[:, 0], cluster_three_data[:, 1], c='g', label='Cluster three')
plt.scatter(cluster_four_data[:, 0], cluster_four_data[:, 1], c='y', label='Cluster four')
plt.scatter(cluster_five_data[:, 0], cluster_five_data[:, 1], color='orange', label='Cluster five')
plt.scatter(clusters[:, 0], clusters[:, 1], marker='*', s=200, color='black', label='Centroids')
plt.title("Custom KMeans results")
plt.legend()

### Mean Shift

from sklearn.cluster import MeanShift

mshift = MeanShift(bandwidth=25)
cluster_mean = mshift.fit(reduced_data)

plt.figure(figsize=(12, 6))
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], label='Datapoints')
plt.scatter(cluster_mean.cluster_centers_[:, 0], cluster_mean.cluster_centers_[:, 1], label='Clusters')
plt.title("Sklearn version of KMeans")
plt.legend()


### Analysing the Cluster:
full_data_kmeans = KMeans_numpy(n_clusters=5)
centroids, clus_data = full_data_kmeans.fit(customers_data.values)

cluster_1 = pd.DataFrame(clus_data[0], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
cluster_2 = pd.DataFrame(clus_data[1], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
cluster_3 = pd.DataFrame(clus_data[2], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
cluster_4 = pd.DataFrame(clus_data[3], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
cluster_5 = pd.DataFrame(clus_data[4], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
print(cluster_1)

# Creating a clusrter-wise dataframe for Analysis
for i in range(6):
    if i == 0:
        cluster_no = 1
        df_new = pd.DataFrame({"Age": cluster_1['Age'], "Income": cluster_1['Annual Income (k$)'],
                              "Spending": cluster_1['Spending Score (1-100)'], "cluster_number": 1, })
        data_new = df_new

    if i == 1:
        cluster_no = 2
        df_new = pd.DataFrame({"Age": cluster_2['Age'], "Income": cluster_2['Annual Income (k$)'],
                              "Spending": cluster_2['Spending Score (1-100)'], "cluster_number": 2})
        data_new = data_new.append(df_new)

    if i == 2:
        cluster_no = 3
        df_new = pd.DataFrame({"Age": cluster_3['Age'], "Income": cluster_3['Annual Income (k$)'],
                              "Spending": cluster_3['Spending Score (1-100)'], "cluster_number": 3})
        data_new = data_new.append(df_new)

    if i == 3:
        cluster_no = 4
        df_new = pd.DataFrame({"Age": cluster_4['Age'], "Income": cluster_4['Annual Income (k$)'],
                              "Spending": cluster_4['Spending Score (1-100)'], "cluster_number": 4})
        data_new = data_new.append(df_new)

    if i == 4:
        cluster_no = 5
        df_new = pd.DataFrame({"Age": cluster_5['Age'], "Income": cluster_5['Annual Income (k$)'],
                              "Spending": cluster_5['Spending Score (1-100)'], "cluster_number": 5})
        data_new = data_new.append(df_new)


# box plots to compair cluster-wise different parameters:
plt.figure()
sns.boxplot(x='cluster_number', y='Age', data=data_new)

plt.figure()
sns.boxplot(x='cluster_number', y='Income', data=data_new)

plt.figure()
sns.boxplot(x='cluster_number', y='Spending', data=data_new)
plt.show()

print("Average age for customers in cluster one: {}".format(np.array(cluster_1['Age']).mean()))
print("Average annual income (in thousends) for customers in cluster one: {}".format(np.array(cluster_1['Annual Income (k$)']).mean()))
print("Deviation of the mean for annual income (in thousends) for customers in cluster one: {}".format(np.array(cluster_1['Annual Income (k$)']).std()))
print("In cluster one we have: {} customers".format(cluster_1.shape[0]))
print("From those customers we have {} male and {} female".format(cluster_1.loc[(cluster_1['Genre'] == 1.0)].shape[0], cluster_1.loc[(cluster_1['Genre'] == 0.0)].shape[0]))


