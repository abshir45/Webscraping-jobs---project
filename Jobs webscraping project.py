#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

r=requests.get("https://realpython.github.io/fake-jobs/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"card"}) 

all[0].find("h2",{"class":"title is-5"}).text


# In[2]:


all


# In[32]:


L=[]
for item in all:
    d={}
    d["Date"]=item.find("p",{"class":"is-small has-text-grey"}).text.replace("\n","")
    d["Job title"]=item.find("h2",{"class":"title is-5"}).text
    d["Location"]=item.find("p",{"class":"location"}).text.replace("\n","").replace(" ","")
    L.append(d)
    


# In[33]:


L


# In[34]:


import pandas
df=pandas.DataFrame(L)


# In[35]:


df


# In[36]:


df.to_csv("Output.csv") 


# In[ ]:




