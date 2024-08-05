# Prodigy_ML_2
Customer Segmentation Using K-Means Clustering
This project demonstrates the use of K-Means clustering to segment customers based on their annual income and spending score.

Table of Contents
Dataset
Requirements
Installation
Usage
Model Evaluation
Visualization
Acknowledgements
Dataset
The dataset used in this project contains information about mall customers, including:

CustomerID
Gender
Age
Annual Income (k$)
Spending Score (1-100)
The dataset is loaded from a CSV file named Mall_Customers.csv.

Requirements
Python 3.6+
pandas
numpy
scikit-learn
matplotlib
Installation
Clone the repository and navigate to the project directory:

git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation
Install the required packages:

pip install pandas numpy scikit-learn matplotlib
Usage
Loading the Dataset
The dataset is loaded using pandas.

Feature Selection
The features used for clustering are:

Annual Income (k$)
Spending Score (1-100)
Data Preprocessing
The data is scaled using StandardScaler from scikit-learn.

Clustering
The K-Means algorithm is used to segment customers into 5 clusters.

Running the Code
Execute the code to perform clustering and visualize the results:

python cluster.py
Model Evaluation
The clustering labels are assigned to the dataset, and the results are visualized using a scatter plot.

Visualization
A scatter plot is created to visualize the customer clusters and centroids.

Acknowledgements
The dataset source for mall customer data.
The scikit-learn and pandas teams for their amazing libraries.
