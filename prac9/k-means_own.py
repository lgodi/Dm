#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# In[7]:


Data = {'x': [13,68,44,57,33,79,36,1,39,44,45,35,26,86,40,56],
        'y': [45,33,55,78,99,53,32,6,87,55,76,43,33,24,46,77]
       }
  
df = DataFrame(Data,columns=['x','y'])
print (df)


# In[8]:


f = DataFrame(Data,columns=['x','y'])
  
kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=40, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=40, marker='s')


# In[9]:


f = DataFrame(Data,columns=['x','y'])
  
kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=40, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=40, marker='s')


# In[ ]:




