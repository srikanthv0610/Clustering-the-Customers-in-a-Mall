# Clustering-the-Customers-in-a-Mall

The project aimes to group the different types of customers in a mall using the K-Means clustering technique.  

**Why:** This project shows how to use Machine Learning in business. By clustering your [customer data](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/tree/main/dataset) you can group them by age, salary, gender or any other feature that you have in your customer dataset. The algorithm will assure to find the best strategy for a market using the customer trends.

**Code:** The main code used in this project is the [Clustering_CustomerInMall.ipynb](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/Clustering_CustomersInMall.py). The custom algorith KMeans is in file [Kmeans_numpy_script.py](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/Kmean_numpy_scipt.py). It is optional to use this but it will help you in understanding how clustering works using K-mean.

## Feature Transformation:

* Check for missing datas
* Convert the Genders to numbers
* Feature scaling

## Visualizing the Data:

Pairplot to compare the relation between parameters:

![Correlation_plot](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/Figure_2.png)

## Visualizing the K-mean Clustering:

![Cluster_plot](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/Figure_3.png)

## Cluster-wise Parameter Analysis and Observations:

* BoxPlot to visualize the K(=5) clusters with respect to **Age**:

 ![AgeCluster_plot](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/agewise_cluster.png)
 
 
* BoxPlot to visualize the K(=5) clusters with respect to **Income earned**:

 ![IncomeCluster_plot](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/income_cluster.png)
 
 * BoxPlot to visualize the K(=5) clusters with respect to **Customer Spndings**:

 ![SpendingCluster_plot](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/Spending_cluster.png)
 
 
 
