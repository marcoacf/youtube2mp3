#!/usr/bin/env python
# coding: utf-8

# ## Download Video in MP3 format using PyTube

# https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/

# In[1]:


#get_ipython().system('pip install pytube')
#get_ipython().system('pip install pytube3')
#get_ipython().system('pip install os_sys')


# In[2]:


# importing packages
from pytube import YouTube
import os

# url input from user
yt = YouTube(
	str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")


# In[ ]:




#https://www.youtube.com/watch?v=nllmm7Q4sj0
    
#https://www.youtube.com/watch?v=s88r_q7oufE    

