# Mall Customer Segmentation using K-mean Clustering Algorithm:

The project aimes to group the different types of customers in a mall using the K-Means clustering technique.  

**Why:** This project shows how to use Machine Learning in business. By clustering your [customer data](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/tree/main/dataset) you can group them by age, salary, gender or any other feature that you have in your customer dataset. The algorithm will assure to find the best strategy for a market using the customer trends.

![Cluster](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/Clustering.png)

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

**Observations:**
* We have 5 clusters into which the customers are grouped. 
* The centroid points in each clusters are the mean values of that clusters to which the other customers belong.

## Cluster-wise Parameter Analysis and Observations:

**1)** BoxPlot to visualize the K(=5) clusters with respect to **Age**:
 ![AgeCluster_plot](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/agewise_cluster.png)
  
**Observations:**
* Average age for customers in cluster one: 44.3
* Average age for customers in cluster two: 51.8
* Average age for customers in cluster three: 32.1
* Average age for customers in cluster four: 41.6
* Average age for customers in cluster five: 24.3
 
**2)** BoxPlot to visualize the K(=5) clusters with respect to **Income earned**:

 ![IncomeCluster_plot](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/income_cluster.png)
 
 **Observations:**
* Average annual income (in thousends) for customers in cluster one: 25.8
* Average annual income (in thousends) for customers in cluster two: 55.2
* Average annual income (in thousends) for customers in cluster three: 79.4
* Average annual income (in thousends) for customers in cluster four: 80.5
* Average annual income (in thousends) for customers in cluster five: 40.6
 
 **3)** BoxPlot to visualize the K(=5) clusters with respect to **Customer Spndings**:

 ![SpendingCluster_plot](https://github.com/srikanthv0610/Clustering-the-Customers-in-a-Mall/blob/main/plots/Spending_cluster.png)
 
  **Observations:**
* Average Spending Score (1-100) for customers in cluster one: 16.2
* Average Spending Score (1-100) for customers in cluster two: 48.8
* Average Spending Score (1-100) for customers in cluster three: 85.0
* Average Spending Score (1-100) for customers in cluster four: 15.9
* Average Spending Score (1-100) for customers in cluster five: 63.6
 

