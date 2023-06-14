#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x=np.linspace(0,10,200)


# In[3]:


x


# In[4]:


y=np.sin(x)


# In[5]:


y


# In[6]:


plt.plot(x,y)


# In[7]:


plt.plot(x,y)
plt.xlabel("This is my X data")
plt.ylabel("This is my y data")
plt.title("This is my graph")

plt.show()


# In[8]:


x=np.random.rand(50)
y=np.random.rand(50)
plt.scatter(x,y)


# In[9]:


x,y


# In[10]:


colours=np.random.rand(50)
x=np.random.rand(50)
y=np.random.rand(50)
sizes=1000*np.random.rand(50)
plt.scatter(x,y,c=colours,s=sizes,alpha=.8)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("random data")


# In[11]:


a=np.random.randn(20)
b=np.random.randn(20)
plt.plot(a,b)


# In[12]:


a=np.random.rand(50)
b=np.sin(a)
plt.plot(a,b)


# In[13]:


x=np.linspace(1,20,100)
x


# In[14]:


y=np.sin(x)


# In[15]:


plt.plot(x,y)


# In[16]:



plt.xlabel("This is X plot")
plt.ylabel("This is y Plot")
color=np.random.rand(50)
sizes=200*np.random.rand(50)
plt.scatter(a,b,c=color,s=sizes,alpha=.8)


# In[17]:


a-np.random.rand(50)


# In[18]:


x=['a','b','c','d','e']


# In[19]:


#colors=np.random.rand(5)
y=np.random.rand(5)
plt.bar(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("this is bar plot")


# In[20]:


y


# In[22]:


# To show in Horizontal Mode
plt.barh(x,y)


# In[25]:


x= np.linspace(1,20,100)
y= np.sin(x)
plt.xlabel("This is my X data")
plt.ylabel("This is my Y data")
plt.plot(x,y,'--r')


# In[36]:


x= np.linspace(1,20,100)
y= np.sin(x)
plt.figure(figsize=(5,2))
plt.plot(x,y,'--b')
plt.xlabel("This is my X data")
plt.ylabel("This is my Y data")
plt.grid()
plt.show()


# In[61]:


x= np.random.rand(50)
y= np.random.rand(50)
plt.figure(figsize=(5,5))
colors=np.random.rand(50)
plt.scatter(x,y,c='r',alpha=.8,marker='p')
plt.xlabel("This is my X data")
plt.ylabel("This is my Y data")
plt.grid()
plt.show()


# In[68]:


x=[4,5,6,7,8,9]
y=[60,70,80,90,55,100]
plt.plot(x,y)
plt.show()


# In[69]:


x=[4,5,6,7,8,9]
y=[60,70,80,90,55,100]
plt.scatter(x,y)
plt.show()


# In[72]:


data=[1,2,3,4,5,1,2,3,7,8,1,2,3]
plt.hist(data)


# In[75]:


x=[4,5,6,7,8,9]
y=[60,30,80,19,40,1]
colors=['r','b','#4E301D','#DCF6AE','#33FFD1','#B233FF']
plt.scatter(x,y,c=colors)
plt.show()


# In[80]:


x=np.random.rand(50)
y=np.random.rand(50)
z=np.random.rand(50)
fig= plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
plt.show()


# In[ ]:




