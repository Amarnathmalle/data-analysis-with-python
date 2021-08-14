#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv("Police Data.csv")


# In[3]:


data.head()


# In[4]:


data.dtypes


# In[5]:


data.isnull().sum()


# In[6]:


data.shape


# In[7]:


data.head(2)
data.drop(columns="country_name",inplace=True)


# In[ ]:





# In[8]:


data[data.violation == 'Speeding'].driver_gender.value_counts()


# In[9]:


data.groupby("driver_gender").search_conducted.sum()


# In[10]:


data.search_conducted.value_counts()


# In[11]:


data.stop_duration.value_counts()


# In[12]:


data['stop_duration']=data['stop_duration'].map({'0-15 Min':7.5,'16-30 Min':24,'30+ Min':45 })


# In[13]:


data


# In[14]:


data['stop_duration'].mean()


# In[15]:


data.head(2)


# In[16]:


data.groupby('violation').driver_age_raw.describe()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




