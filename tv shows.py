#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
netflix=pd.read_csv("Netflix Dataset.csv")


# In[11]:


netflix.head()


# In[12]:


netflix.dtypes


# In[13]:


netflix.shape


# In[14]:


netflix.isnull().sum()


# In[17]:


netflix.size


# In[18]:


netflix.columns


# In[21]:


netflix[netflix.duplicated()]


# In[28]:


netflix.drop_duplicates(inplace = True)


# In[29]:


netflix.shape


# In[31]:


netflix.isnull().sum()


# In[36]:


import seaborn as sns
sns.heatmap(netflix.isnull())


# In[61]:


netflix[netflix['Title'].isin(['House of Cards'])]


# In[63]:


netflix[netflix['Title'].str.contains('House of Cards')]


# In[64]:


netflix.columns


# In[73]:


netflix['New_date']=pd.to_datetime(netflix['Release_Date'])


# In[74]:


netflix.dtypes


# In[75]:


netflix.head()


# In[76]:


netflix['New_date'].dt.year.value_counts()


# In[78]:


netflix['New_date'].dt.year.value_counts().plot(kind='bar')


# In[93]:


netflix.groupby('Category').Category.count()


# In[95]:


sns.countplot(netflix['Category'])


# In[97]:


netflix['year']=netflix['New_date'].dt.year


# In[98]:


netflix.head(2)


# In[110]:


netflix[(netflix['Category']=='Movie') &(netflix['year']==2020)]


# In[113]:


netflix[(netflix['Category']=='TV Show') &(netflix['Country']=='India')]['Title']


# In[115]:


netflix['Director'].value_counts().head(10)


# In[127]:


netflix[(netflix['Category']=='Movie')&(netflix['Type']=='Comedies') | (netflix['Country']=='United Kingdom')]


# In[132]:


netflix_new=netflix.dropna()


# In[133]:


netflix_new.head()


# In[134]:


netflix_new.shape


# In[145]:


netflix.sort_values(by='year',ascending = False)


# In[ ]:




