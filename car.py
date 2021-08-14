#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
car=pd.read_csv("Cars Data.csv")
car.head()


# In[2]:


car.shape


# In[3]:


car.isnull().sum()


# In[4]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)


# In[5]:


car.isnull().sum()


# In[6]:


car.dtypes


# In[7]:


car['Length'].fillna(car['Length'].mean(), inplace=True)


# In[8]:


car.isnull().sum()


# In[9]:


car['Make'].value_counts()


# In[10]:


car.head()
car[car['Origin'].isin(['Asia','Europe'])]


# In[11]:



car[~(car['Weight'] > 4000)]


# In[12]:


car.head(2)
car['MPG_City'] = car['MPG_City'].apply(lambda x :x-2)


# In[13]:


car


# In[ ]:





# In[ ]:





# In[ ]:




