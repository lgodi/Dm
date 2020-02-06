#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np;
import pandas as pd;
from apyori import apriori;


# In[2]:


data = pd.read_csv('store_data.csv');
data.head()


# In[3]:


data.shape


# In[4]:


data = pd.read_csv('store_data.csv',header=None);
data.head()


# In[5]:


data.shape


# In[6]:


records = [];
for i in range(0, 10):  
    records.append([str(data.values[i,j]) for j in range(0, 7)]);
association_rules = apriori(records, min_support=0.0050, min_confidence=0.3, min_lift=3, min_length=2);
association_results = list(association_rules);


# In[9]:


for item in association_results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
    print(len(association_results))


# In[ ]:




