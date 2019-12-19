#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# In[5]:


x=[[27.75],[24.5],[25.5],[26],[25],[27.75],[26.5],[27],[26.75],[26.75],[27.5]]
y=[[17.5],[17.1],[17.1],[17.3],[16.9],[17.6],[17.3],[17.5],[17.3],[17.5],[17.5]]


# In[6]:


regression_model = LinearRegression()
regression_model.fit(x,y)
y_predicted = regression_model.predict(x)
rmse = mean_squared_error(y, y_predicted)
r2 = r2_score(y, y_predicted)


print('Slope:' ,regression_model.coef_)
print('Intercept:', regression_model.intercept_)
print('Root mean squared error: ', rmse)
print('R2 score: ', r2)


# In[4]:


plt.scatter(x, y, s=10)
plt.xlabel('x')
plt.ylabel('y')

# predicted values
plt.plot(x, y_predicted, color='r')
plt.show()


# In[ ]:




