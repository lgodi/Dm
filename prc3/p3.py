#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[14]:


x=[4,55,21,33,5,92,33,5,91,33,9,29,99,105,39,45,6,62,65,25,10,73,85,11,79,20,56,45,21,8,65,70,30]
print(x)
print("Minimum = ",np.min(x))
print("Maximum = ",np.max(x))
print('Q1 = ', np.quantile(x, .25))
print('Median = ',np.quantile(x, .50))
print('Q3 = ',np.quantile(x, .75))


# In[15]:


sns.boxplot(data=x,color='y')
sns.swarmplot(data=x,color='b')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




