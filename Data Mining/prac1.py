#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt

#%matplotlib is a magic function in IPython. ... 
#%matplotlib inline sets the backend of matplotlib to the 'inline' backend: 
#With this backend, the output of plotting commands is displayed 
#inline within frontends like the Jupyter notebook, directly below the code cell that produced it.
get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.style.use('ggplot')

np.random.seed(1)

#numpy.random.normal(loc = 0.0, scale = 1.0, size = None)
#creates an array of specified shape and fills it with random values which is actually a part of Normal(Gaussian)Distribution. 
#This is Distribution is also known as Bell Curve because of its characteristics shape.
#loc   : [float or array_like]Mean of the distribution. 
#scale : [float or array_like]Standard Derivation of the distribution. 
#size  : [int or int tuples]. 
#Round an array to the given number of decimals
data = np.round(np.random.normal(10, 5, 100))
#data=np.round(np.random.rand(100))

print("1D Array filled with random values as per gaussian distribution : \n", data) 

plt.hist(data, bins=20, range=(5,10), edgecolor='black')
plt.show()


# In[8]:


lst[5.2,3.2,5.7,6.9,2.8,3.5,6.7,7.8,7.3,7.2,9.5,4.5,4.2,2.8,4.9,5.9,9.2,5.7,4.5]
mean = np.mean(lst)
mean


# In[9]:


import numpy as np
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt


# In[10]:


lst[5.2,3.2,5.7,6.9,2.8,3.5,6.7,7.8,7.3,7.2,9.5,4.5,4.2,2.8,4.9,5.9,9.2,5.7,4.5]
mean = np.mean(lst)
mean


# In[11]:


data=list[5.2,3.2,5.7,6.9,2.8,3.5,6.7,7.8,7.3,7.2,9.5,4.5,4.2,2.8,4.9,5.9,9.2,5.7,4.5]
mean = np.mean(data)
mean


# In[12]:


#mean
list=[5.2,3.2,5.7,6.9,2.8,3.5,6.7,7.8,7.3,7.2,9.5,4.5,4.2,2.8,3.2,4.9,5.9,9.2,5.7,4.5]
mean = np.mean(list)
mean


# In[22]:


#median
np.median(list)


# In[23]:


#mode
mode = stats.mode(list)

print("The modal value is {} with a count of {}".format(mode.mode[0], mode.count[0]))


# In[24]:


# range 
np.ptp(list)   


# In[25]:


#variance
np.var(list)


# In[26]:


#standard deviation
np.std(list)


# In[27]:


stats.sem(list)


# In[28]:


#graph

plt.hist(list, bins=10, range=(0,10), edgecolor='black')
plt.show()


# In[ ]:




