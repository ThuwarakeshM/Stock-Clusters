
# coding: utf-8

# In[1]:

import pandas as pd
import glob


# In[3]:

path = '/home/thuwarakesh/projects/Stock Clusters/data'
all_files = glob.glob(path + '/*.csv')


# In[4]:

names = [f.split('/')[-1][:-4] for f in all_files]


# In[5]:

data = pd.concat([pd.read_csv(f, parse_dates=True, index_col='Date').pct_change() for f in all_files], keys= names)


# In[13]:

df = data.unstack(0)['Close']


# In[16]:

df=df[1:]


# In[17]:

df.to_csv('/home/thuwarakesh/projects/Stock Clusters/data.csv')


# In[18]:

df = df[[token for token in df.columns if len(df[token].dropna())>1200]].dropna()


# In[19]:

df_monthly = df.resample('M').mean()
df_monthly.to_csv('/home/thuwarakesh/projects/Stock Clusters/data_monthly.csv')


# In[20]:

df_quaterly = df.resample('Q').mean()
df_quaterly.to_csv('/home/thuwarakesh/projects/Stock Clusters/data_quaterly.csv')


# In[8]:

df.resample('M').mean()


# In[ ]:



