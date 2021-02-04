
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt


# In[3]:


x = [1, 2, 3]
y = [1.2, 1.9, 3.2]


# In[4]:


plt.plot(x, y, 'ro')
plt.title("Distribution")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("distribution")


# In[5]:


def fit(x, y):
    n = len(x)

    x_mean = sum(x)/n
    y_mean = sum(y)/n

    num = 0
    denom = 0
    for i in range(n):
        num += (x[i] - x_mean)*(y[i] - y_mean)
        denom += (x[i] - x_mean)**2

    slope = num/denom
    intercept = y_mean - slope*x_mean
    return slope, intercept


# In[6]:


m, c = fit(x, y)


# In[7]:


x = np.array(x)
y = np.array(y)


# In[8]:


plt.plot(x, m*x + c)
plt.plot(x, y, 'bo')
plt.title("Best fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("best_fit")

