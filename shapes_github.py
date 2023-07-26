#!/usr/bin/env python
# coding: utf-8

# In[8]:


#area of circle A= (22/7)*radius*radius
def area_of_circle(radius):
    A = (22/7)*radius*radius
    return A


# In[7]:


#area of rectangle A= w*l
def area_of_rectangle(w,r):
    A = w*r
    return A


# In[6]:


#area of triangle A =(height*base)/2
def area_of_triangle(h,b):
    A = (h*b)/2
    return A


# In[5]:


#area of squire  A = a**2
def area_of_squire(a):
    A = a**2
    return A


# In[ ]:


# peri of squire  p = side*4
def peri_of_squire(side):
    P = side*4
    return P


# In[ ]:


#peri of triangle  p = a+b+c
def peri_of_triangle(a,b,c):
    P = a+b+c
    return P


# In[ ]:


# peri of circle  p = 2(22/7)r
def peri_of_circle(r):
    P = 2*(22/7)*r
    return P


# In[ ]:


# peri of rectangle p = 2(l + w)
def peri_of_rectangle(l,w):
    P = 2*(l + w)
    return P

