#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random as sample
import pandas as pd


# In[6]:


d=[3,6,4,7,3,4,6,8,6,10]


# In[7]:


wr=np.random.choice(d,5,replace=False);
print("With Replacement = ",wr)


# In[8]:


wor=np.random.choice(d,5,replace="true");
print("Without Replacement = ",wor)


# In[11]:


emp=[[101,"A","Liza",20000],[102,"B","Krishna",25000],[103,"C","Ram",10000],[104,"D","Rohan",30000],[105,"D","Devanshi",25000],[106,"B","Drashti",20000],[107,"A","Mansi",30000]]
lst=[]
for i in emp:
    for j in i:
        s=i[1];
    print(s)


# In[ ]:




