#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np;
import pandas as pd;
from apyori import apriori;


# In[8]:


data = pd.read_csv('items.csv');
data.head()


# In[9]:


data.shape


# In[10]:


data = pd.read_csv('items.csv',header=None);
data.head()


# In[11]:


data.shape


# In[15]:


records = [];
for i in range(0, 5):  
    records.append([str(data.values[i,j]) for j in range(0, 8)]);
association_rules = apriori(records, min_support=0.0050, min_confidence=0.3, min_lift=3, min_length=2);
association_results = list(association_rules);


# In[16]:


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




