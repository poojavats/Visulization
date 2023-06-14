#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


df=sns.load_dataset('iris')


# In[3]:


df.head()


# In[4]:


df.count()


# In[5]:


df.tail()


# In[6]:


df['New_leaf']=32


# In[7]:


df


# In[8]:


df.isnull().sum()


# In[9]:


df


# In[13]:


import matplotlib.pyplot as plt


# In[24]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(5, 5))
sns.scatterplot(x=df.sepal_length, y=df.sepal_width)
plt.xlabel("This is x")
plt.ylabel("This is y")
plt.title("This is Title")
plt.show()


# In[25]:


sns.scatterplot(x=df.sepal_length, y=df.sepal_width)


# In[27]:


sns.displot(df['sepal_length'])


# In[28]:


tips=sns.load_dataset('tips')


# In[29]:


tips


# In[31]:


sns.scatterplot(x=tips.total_bill,y=tips.tip)


# In[52]:


tips.head()


# In[53]:


tips['smoker'].value_counts()


# In[61]:



sns.relplot(x=tips.total_bill,y=tips.tip,data=tips,hue='smoker')


# In[62]:


tips.head()


# In[63]:


sns.relplot(x=tips.total_bill,y=tips.tip,data=tips,hue='size')


# In[64]:


sns.relplot(x=tips.total_bill,y=tips.tip,data=tips,hue='sex')


# In[65]:


sns.relplot(x=tips.total_bill,y=tips.tip,data=tips,style='size')


# In[66]:


sns.relplot(x=tips.total_bill,y=tips.tip,data=tips,style='size',hue='time')


# In[70]:


sns.catplot(x='day',y='total_bill',data=tips)


# In[73]:


sns.catplot(x='smoker',y='tip',data=tips)


# In[74]:


sns.jointplot(x=tips.total_bill,y=tips.tip)


# In[75]:


sns.pairplot(tips)


# In[78]:


sns.pairplot(df)


# In[ ]:




