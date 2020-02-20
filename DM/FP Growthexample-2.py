#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np;
import pandas as pd;
import pyfpgrowth;


# In[2]:


dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']];


# In[12]:


patterns = pyfpgrowth.find_frequent_patterns(dataset,4);
#patterns = pyfpgrowth.find_frequent_patterns(dataset, 4);
print("No. of patterns found = ", len(patterns));
patterns


# In[13]:


rules = pyfpgrowth.generate_association_rules(patterns, 0.3)
print("No. of rules found =", len(rules));
rules


# In[ ]:





# In[ ]:





# In[ ]:




