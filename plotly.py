#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go


# In[5]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=[1,2,3,4,5],y=[3,4,5,6,7],mode='markers'))
fig.show()


# In[9]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=[1,2,3,4,5],y=[5,6,7,8,9],mode='lines'))
fig.show()


# In[13]:


fig=go.Figure()
fig.add_trace(go.Bar(x=[1,2,3,4,5],y=[5,7,8,9,10]))
fig.show()


# In[15]:


x=[1,2,3,4,5,5,10,10,2,2,8,8,101,77,5,6,6,6,77,55,10]


# In[19]:


fig=go.Figure(data=[go.Histogram(x=x)])
fig.show()


# In[20]:


import seaborn as sns
df=sns.load_dataset('tips')


# In[21]:


df


# In[25]:


fog=go.Figure(data=[go.Histogram(x=df.total_bill)])
fog.show()


# In[29]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=df.total_bill,y=df.tip,mode='markers'))
fig.show()


# In[33]:


import plotly.graph_objects as go
fig=go.Figure()
fig.add_trace(go.Scatter(x=df.total_bill,y=df.tip,mode='markers',marker_size=10*df['size']))
fig.show()


# In[37]:


import plotly.graph_objects as go
fig=go.Figure()
fig.add_trace(go.Scatter3d(x=df.total_bill,y=df.tip,mode='markers',z=df['size']))
fig.show()


# In[40]:


import plotly.graph_objects as go
fig=go.Figure()
fig.add_trace(go.Scatter3d(x=[1,2,3,4,5],y=[5,6,7,8,9],mode='lines',z=[2,3,4,5,6]))
fig.show()


# In[42]:


import plotly.graph_objects as go
fig=go.Figure()
fig.add_trace(go.Scatter3d(x=[1,2,3,4,5],y=[5,6,7,8,9],mode='markers',z=[2,3,4,5,6]))
fig.show()


# In[ ]:




