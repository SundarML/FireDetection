#!/usr/bin/env python
# coding: utf-8

# In[35]:


import os
import numpy as np
import cv2
from PIL import Image
path = 'D:/ML/Fire/Images'
#Original images from github
#https://github.com/cair/Fire-Detection-Image-Dataset
images_path = [os.path.join(path, i) for i in os.listdir(path)]
fire_data_sets = []

for img_path in images_path:
    PIL_img = Image.open(img_path).convert('L')
    img_numpy = np.array(PIL_img, 'uint8')
    fire_data_sets.append(img_numpy)
#print(os.listdir(path))


# In[69]:


path_img = 'D:/ML/Fire'
def save_images(datasets, path):
    part_1_img_numpy = datasets[:35]
    part_2_img_numpy = datasets[35:80]
    part_3_img_numpy = datasets[80:110]
    imgs = [part_1_img_numpy, part_2_img_numpy, part_3_img_numpy]
    names = ['part1','part2','part3']
    
    for name,x in zip(names,imgs):
        np.save(path+'/'+name, x)
        #print(path+'/'+name, x)
        
    
    


# In[70]:


save_images(fire_data_sets, path_img)


# In[50]:





# In[54]:





# In[57]:





# In[37]:


import matplotlib.pyplot as plt
plt.imshow(fire_data_sets[2])


# In[ ]:





# In[ ]:




