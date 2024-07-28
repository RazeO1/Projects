#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests
import random

def get_random_quotes():
    
    try:
        response = requests.get("https://type.fit/api/quotes")
        if response.status_code == 200:
            data = response.json()
            quote = random.choice(data)
            print(quote["text"])
            print(quote["author"])
        
        else:
            print("Error:", response.status_code, response.text)
        
    
    except:
        print("Error: Something went wrong!")
    
get_random_quotes()



# In[ ]:




