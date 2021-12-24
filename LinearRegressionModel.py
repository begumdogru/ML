#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd>


# In[2]:


import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


test = pd.read_csv(r"C:\Users\Lenovo\test.csv")


# In[4]:


test.head()


# In[11]:


x = test[["x"]]
y = test[["y"]]
plt.plot(x, y, 'o')


# In[12]:


from sklearn.linear_model import LinearRegression


# In[13]:



line_fitter = LinearRegression()
line_fitter.fit(x, y)


# In[14]:


y_predict = line_fitter.predict(x)


# In[15]:


plt.plot(x, y_predict)
plt.show()

