#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file_path = 'df.csv'
df = pd.read_csv(file_path)
df


# In[3]:


df.info()


# In[4]:


df.dtypes


# In[5]:


df['dob'] = pd.to_datetime(df['dob']).dt.year
df['dob'] = 2024 - df['dob']


# In[6]:


df['dob']


# In[9]:


df.dtypes


# In[11]:


df.rename(columns={'dob':'age', 'amt':'amount'}, inplace=True)
df

