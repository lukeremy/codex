
# coding: utf-8

# # Sean Lahmn database exploration

# In[1]:

# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import MySQLdb as mdb
import os
import sys

get_ipython().magic(u'matplotlib inline')


# In[2]:

import cufflinks as cf
import plotly.plotly as py
import plotly.graph_objs as go

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot



# In[3]:

# allows us to view plotly in notebooks
# init_notebook_mode(connected=True)
# for offline use
cf.go_offline()


# In[4]:

# view and open csv files


# In[5]:

batting = pd.read_csv("data/baseballdatabank-master/core/Batting.csv")
pitching = pd.read_csv("data/baseballdatabank-master/core/Pitching.csv")


# In[6]:

pitching.head()


# In[7]:

# connect to SQL file


# In[8]:

# filepath to SQL file
data = "stats.sql"


# In[9]:

# open db connection 
# db = mdb.connect(host="localhost", user="root", passwd = "password", db=data)


# # EDA

# In[10]:

# view batting data
batting.head()


# In[11]:

batting.info()


# In[12]:

batting.describe()


# ### What is the relationship between home runs and strikeouts through the years?

# In[7]:

# explore home runs vs strikeouts
sns.lmplot(x='SO', y='HR', data=batting[batting['yearID'] >= 1973], aspect=2)


# In[8]:

batting[batting['yearID'] >= 1973].iplot(kind='scatter',x='SO',y='HR', mode='markers', size=2)


# In[18]:

batting_nums = batting.drop(['playerID','stint','teamID'], axis=1)


# In[19]:

batting_nums.info()
bat = batting_nums[batting_nums['yearID'] >= 1973]
bat.info()


# In[ ]:
# takes too long to run
# sns.pairplot(bat, hue='lgID')


# In[ ]:

sns.heatmap(bat.drop(['yearID'], axis=1).corr(),cmap='magma', linecolor='white', linewidths=.7)
plt.title('Batting correlations')


# In[49]:

# how does HR vs SO ratio change over years?


# In[ ]:

# create data frame of all stats summed per year
gb = bat.groupby('yearID').agg(sum)


# In[55]:

gb.info()


# In[54]:

# plot HR and SO on facet plot
# plt.subplot(2,1,1)
# plt.plot(gb_years['HR'], color='green')
# plt.ylabel('Total HR')
# plt.title('HR and SO in MLB')

# plt.subplot(2,1,2)
# plt.plot(gb_years['SO'], color='red')
# plt.ylabel('Total SO')
# plt.xlabel('Year')#

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(gb_years)


# In[64]:

# group by leagues and years
gb_years = bat.groupby(['yearID','lgID']).agg(sum)
gb_years.tail(6)

HR = bat[['HR', 'lgID', 'yearID']]
# bat[['HR','lgID']].groupby(bat['yearID']).agg(sum)
HR.head()
# In[75]:
# takes too long to run, not very informative
# sns.pairplot(batting, hue='lgID')


# In[68]:

gb_years['ratio'] = gb_years['HR'] / gb_years['SO']
gb_years.dropna().describe()


# In[69]:

gb_years[(gb_years['ratio'] == gb_years['ratio'].dropna().min()) & gb_years['yearID'] >= 1973]


# In[70]:

gb_yrs = [go.Scatter(x=gb_years.index, y=gb_years['ratio'])]


# In[72]:

plt.plot(gb_years.index, gb_years['ratio'], gb_years.index, gb_years['HR'], gb_years.index, gb_years['SO'])


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



