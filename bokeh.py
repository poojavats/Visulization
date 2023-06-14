#!/usr/bin/env python
# coding: utf-8

# In[2]:


import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()


# In[5]:


from bokeh.plotting import figure,output_file, show
from bokeh.sampledata.iris import flowers
output_file('test.html')
p=figure(title='This is my Test flower')
p.xaxis.axis_label="pettel_length"
p.yaxis.axis_label="pettel_width"
p.circle(flowers['petal_length'],flowers['petal_width'])
show(p)


# In[6]:


flowers


# In[7]:


from bokeh.plotting import figure,output_file, show
from bokeh.sampledata.iris import flowers
output_file('test.html')
p=figure(title='This is my Test flower')
p.xaxis.axis_label="pettel_length"
p.yaxis.axis_label="pettel_width"
p.line(flowers['petal_length'],flowers['petal_width'])
show(p)


# In[ ]:




