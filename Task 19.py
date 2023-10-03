#!/usr/bin/env python
# coding: utf-8

# ### Create a Python script that simulates a simple login system. The script should prompt the user to enter their username and password. If the entered username and password match the predefined credentials, the script should log a successful login event to a log file. If the credentials do not match, it should log a failed login attempt to the log file. Example Output Assuming the predefined credentials are username: "user123" and password: "pass123", here's an example output of the script:

# In[1]:


import time

username = "subhasri123"
password = "challa123"

user_name = input("enter your username::")
pass_word = input("enter your password::")

now = time.strftime("%m/%d/%Y, %H:%M:%S")  

if (username == user_name) and (password == pass_word):
    print(f'login successful for subhasri123 ({now})')
    
else:
    print(f'login failed for subhasri123 ({now})')


# ### Create any 5 of following modules
# a. Restaurant
# 
# b. IPL
# 
# c. Mathematics
# 
# d. Data Science
# 
# e. India
# 
# f. Shopping mall
# 
# g. Amazon_price
# 
# Do some research while creating them

# In[6]:


import mathematics


# In[8]:


mathematics.authors()


# In[9]:


mathematics.operations()


# In[10]:


mathematics.symbols()


# In[11]:


mathematics.types()


# ### Amazon

# In[6]:


import Amazon


# In[7]:


Amazon.footwear()


# In[8]:


Amazon.kurtis()


# In[10]:


Amazon.phones()


# In[11]:


Amazon.shirts()


# ### IPL

# In[17]:


import IPL as i


# In[18]:


IPL.citys()


# In[19]:


IPL.seasons()


# In[20]:


IPL.teams()


# In[21]:


IPL.toss()


# ### India

# In[4]:


import India


# In[5]:


India.cities()


# In[6]:


India.festivals()


# In[7]:


India.languages()


# 

# In[ ]:




