#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np;
import pandas as pd;
import pyfpgrowth;


# In[3]:


data=[['f','a','c','d','g','l','m','p'],
     ['a','b','c','f','l','m','o'],
     ['b','f','h','o','j','a','w'],
     ['b','e','k','s','p'],
     ['a','f','c','o','e','l','p','m','n']];


# In[8]:


patterns = pyfpgrowth.find_frequent_patterns(data, 3);
#patterns = pyfpgrowth.find_frequent_patterns(dataset, 4);
print("No. of patterns found = ", len(patterns));
patterns


# In[7]:


rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
print("No. of rules found =", len(rules));
rules


# In[ ]:




