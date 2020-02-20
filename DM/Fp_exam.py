#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np;
import pandas as pd;
import pyfpgrowth;


# In[2]:


data=[['E','K','M','N','O','Y'],
      ['D','E','K','N','O','U'],
      ['A','E','K','M'],
      ['C','K','M','U','Y'],
      ['C','E','I','K','O','O']];


# In[4]:


patterns = pyfpgrowth.find_frequent_patterns(data, 2);
#patterns = pyfpgrowth.find_frequent_patterns(dataset, 4);
print("No. of patterns found = ", len(patterns));
patterns


# In[5]:


rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
print("No. of rules found =", len(rules));
rules


# In[ ]:




