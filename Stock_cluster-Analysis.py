
# coding: utf-8

# In[27]:

import pandas as pd
from sklearn.cluster import KMeans


# In[28]:

df = pd.read_csv('/home/thuwarakesh/projects/Stock Clusters/data_quaterly.csv', parse_dates=True, index_col='Date')


# In[29]:

df = df.to_period().T
df.head()


# In[30]:

n_clusters = 3
kmeans3 = KMeans(n_clusters=n_clusters).fit(df)
clusts3 = pd.Series(kmeans3.labels_,index=df.index)


# In[31]:

n_clusters = 5
kmeans5 = KMeans(n_clusters=n_clusters).fit(df)
clusts5 = pd.Series(kmeans5.labels_,index=df.index)


# In[36]:

n_clusters = 8
kmeans8 = KMeans(n_clusters=n_clusters).fit(df)
clusts8 = pd.Series(kmeans8.labels_,index=df.index)


# In[37]:

n_clusters = 10
kmeans10 = KMeans(n_clusters=n_clusters).fit(df)
clusts10 = pd.Series(kmeans10.labels_,index=df.index)


# In[38]:

clusts = pd.concat([clusts3, clusts5, clusts8, clusts10], axis=1)
clusts.columns = ['clusts3', 'clusts5', 'clusts8', 'clusts10']
clusts.head()


# In[39]:

clusts.to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/1-cluster_labels.csv')


# In[40]:

metad = pd.read_csv('/home/thuwarakesh/projects/Stock Clusters/tokens.csv')


# In[41]:

metad.head()


# In[42]:

clust_details = clusts.merge(metad, 
             how='left', 
             left_index=True, 
             right_on='Ticker symbol')


# In[43]:

clust_details.to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/1-cluster_labels.csv')


# In[44]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[14]:

clust3_summary = pd.crosstab(clust_details['clusts3'], clust_details['GICS Sector'])


# In[45]:

clust3_summary.to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/2-cluster3_summary.csv')
clust3_summary


# In[18]:

fig, ax = plt.subplots()
clust3_summary.plot(kind='bar', ax=ax)
fig.set_figheight(12)
fig.set_figwidth(10)


# In[46]:

clust3_detail_summary =  pd.crosstab(clust_details['clusts3'], clust_details['GICS Sub Industry'])
clust3_detail_summary.idxmax(axis=1).to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/2-cluster3_detail_summary.csv')


# In[47]:

clust5_summary = pd.crosstab(clust_details['clusts5'], clust_details['GICS Sector'])
clust5_summary.to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/5-cluster5_summary.csv')
clust5_summary


# In[48]:

fig, ax = plt.subplots()
clust5_summary.plot(kind='bar', ax=ax)
fig.set_figheight(12)
fig.set_figwidth(10)


# In[49]:

clust5_detail_summary = pd.crosstab(clust_details['clusts5'], clust_details['GICS Sub Industry'])
clust5_detail_summary.idxmax(axis=1).to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/7-clust5_detail_summary.csv')


# In[50]:

clust8_summary = pd.crosstab(clust_details['clusts8'], clust_details['GICS Sector'])
clust8_summary.to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/8-clust8_summary.csv')
clust8_summary


# In[51]:

fig, ax = plt.subplots()
clust8_summary.plot(kind='bar', ax=ax)
fig.set_figheight(12)
fig.set_figwidth(10)


# In[52]:

clust8_detail_summary = pd.crosstab(clust_details['clusts8'], clust_details['GICS Sub Industry'])
clust8_detail_summary.idxmax(axis=1).to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/10-clust8_detail_summary.csv')


# In[53]:

clust10_summary = pd.crosstab(clust_details['clusts10'], clust_details['GICS Sector'])
clust10_summary.to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/11-clust10_summary.csv')
clust10_summary


# In[54]:

fig, ax = plt.subplots()
clust10_summary.plot(kind='bar', ax=ax)
fig.set_figheight(12)
fig.set_figwidth(10)


# In[55]:

clust10_detail_summary = pd.crosstab(clust_details['clusts10'], clust_details['GICS Sub Industry'])
clust10_detail_summary.idxmax(axis=1).to_csv('/home/thuwarakesh/projects/Stock Clusters/Results/13-clust10_detail_summary.csv')


# In[ ]:



