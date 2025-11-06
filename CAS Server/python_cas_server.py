#!/usr/bin/env python
# coding: utf-8

# In[18]:


import swat
import os


# In[19]:


cashost = 'sas-cas-server-default-client'
casport = 5570
passwordToken = os.environ.get('ACCESS_TOKEN')


# In[21]:


conn = swat.CAS(hostname=cashost, port=casport, password=passwordToken)


# In[24]:


display(conn)
print(conn.serverstatus())
type(conn)
conn.about()['About']['Viya Version']


# In[23]:


conn.fileInfo(caslib = 'casuser')


# In[28]:


import pandas as pd
import numpy as np

conn.read_csv('data/courses/CASL/data/my_data/cars.csv', casout={'name':'cars', 'caslib':'casuser', 'replace':True})

conn.fileInfo(caslib = 'casuser')


# In[30]:


castbl = conn.CASTable('cars', caslib = 'casuser')

display(type(castbl), castbl)

castbl.tableDetails()

df = castbl.head()

display(df)


# In[ ]:




