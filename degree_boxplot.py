#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns


# In[54]:


df = pd.read_csv('mystringdb.txt', sep=' ')
mydf = df[(df['combined_score'] >= 500)]
mydf[['ignore1', 'protein1']] = mydf['protein1'].str.split('.',expand=True)
mydf[['ignore2', 'protein2']] = mydf['protein2'].str.split('.',expand=True)


# In[55]:


network = nx.from_pandas_edgelist(mydf, source = 'protein1', target = 'protein2')


# In[57]:


highdegree = [n for n,d in network.degree if d > 100]  


# In[58]:


lowdegree = [n for n,d in network.degree if d <= 100]


# In[59]:


db = pd.read_csv('myensembldb.txt', sep='\t')


# In[60]:


db.tail()


# In[61]:


mydb = db.dropna()


# In[81]:


hd_df = mydb[mydb['Protein stable ID'].isin(highdegree)]
ld_df = mydb[mydb['Protein stable ID'].isin(lowdegree)]


# In[96]:


hd_df['degree'] = 'high degree'
ld_df['degree'] = 'low degree'


# In[100]:


final = pd.concat([hd_df,ld_df], axis=0)


# In[168]:


plot = final.groupby(['degree', 'Protein stable ID'])['Pfam ID'].count().to_frame(name="Pfam ID").reset_index()


# In[170]:


sns.boxplot(x="degree", y="Pfam ID", data=plot)
plt.savefig('degree_boxplot.png', dpi=300, bbox_inches='tight')


# In[ ]:




