
# coding: utf-8

# In[2]:


import numpy as np
import cv2 as cv2
import moviepy as mov
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
import proglog
#proglog.notebook()


# # Extracting Text From Video
# Given a screen captured video clip with scrolling text. What would be a viable (possible efficient) way of doing it?
# 
# Let's find out!

# In[10]:


#get_ipython().system('ls')


# In[11]:


cap = cv2.VideoCapture(0)


# In[4]:


ret, frame = cap.read()


# In[5]:


plt.imshow(frame)


# In[6]:


frame.shape


# In[7]:


#cap.release()


# In[12]:


while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[3]:


help(cv2.waitKey)

