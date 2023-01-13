#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data1=pd.read_csv("Mall_Customers.csv")


# In[3]:


data1.head()


# In[4]:


data1.tail()


# In[5]:


s1=data1.shape
print("data1=",s1)


# In[6]:


# checking NULL data in this data set
data1.isnull().any().any()


# In[7]:


data1=data1.iloc[:, [3,4]].values
print(data1)
plt.scatter(data1[:,0],data1[:,1],s=5,c="red")
print(type(data1))


# In[8]:


def euclidean_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points.
    """
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance ** 0.5

def get_neighbors(data, point, eps):
    neighbors = []
    for p in data:
        if euclidean_distance(point, p) < eps:
            neighbors.append(p)
    return neighbors


# In[9]:


def DBSCAN(data, eps, min_points):
    clusters = []
    visited = set()
    
    for point in data:
        #print(data)
        #print(point)
        if tuple(point) in visited:
            continue
        
        visited.add(tuple(point))
        neighbors = get_neighbors(data, point, eps)
        
        if len(neighbors) < min_points:
            # Point is a noise point
            continue
        
        # Point is a core point
        cluster = []
        clusters.append(expand_cluster(data, point, neighbors, cluster, visited, eps, min_points))
    
    return clusters

def expand_cluster(data, point, neighbors, cluster, visited, eps, min_points):
    """
    Expands the cluster to include density-reachable items.
    """
    cluster.append(point)
    visited.add(tuple(point))
    
    i = 0
    while i < len(neighbors):
        neighbor = neighbors[i]
        if tuple(neighbor) in visited:
            i += 1
            continue
        
        visited.add(tuple(neighbor))
        new_neighbors = get_neighbors(data, neighbor, eps)
        if len(new_neighbors) >= min_points:
            neighbors += new_neighbors
        
        cluster.append(neighbor)
        i += 1
    
    return cluster


# In[10]:


eps = 5
min_points = 5
clusters = DBSCAN(data1, eps, min_points)
#print(clusters)
l=len(clusters)
print("NUMBER OF CLUSTERS",l)
c=["red","blue","green","black","cyan","yellow","magenta","lightcoral", "darkorange", "olive", "teal","iolet","kyblue"]
#arr = clusters.to_numpy()
j=0
for i in clusters:
   # random_color=list(np.random.choice(range(255),size=3))
    a=pd.DataFrame(i)
    print(a)
    #print(type(a))
    b=np.array(a)
    print(type(b))
    B=len(b)
    print("NUMBER OF item in this  CLUSTER",B,"\n")
    plt.scatter(b[:,0],b[:,1],s=5,c=c[j])
    j=j+1


# In[ ]:





# In[ ]:





# In[ ]:




