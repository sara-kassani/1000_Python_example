#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import zipfile
from tqdm import tnrange, tqdm_notebook
import os
import SimpleITK as sitk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from PIL import Image
import pydicom
from IPython import display
import time
from mpl_toolkits.mplot3d import Axes3D
import copy
matplotlib.rcParams['figure.figsize'] = (20, 12)
import scipy.signal


# In[2]:


raw_img_filename= "../data/LNDb-0265.mhd"    # MetaImage (mhd): raw, compressed


# In[3]:


raw_img= sitk.ReadImage(raw_img_filename)
# out_img= sitk.ReadImage(out_img_filename)


# In[4]:


print("img size: {}".format(raw_img.GetSize()))
print("img origin: {}".format(raw_img.GetOrigin()))
print("img spacing: {}".format(raw_img.GetSpacing()))
print("img width: {}".format(raw_img.GetWidth()))
print("img height: {}".format(raw_img.GetHeight()))
print("img depth: {}".format(raw_img.GetDepth()))
print("img direction: {}".format(raw_img.GetDirection()))


# In[5]:


# calculate img resolution: with*height
img_resolution= raw_img.GetSize()[0] * raw_img.GetSize()[1]
# or
# img_resolution= raw_img.GetWidth() * raw_img.GetHeight()

img_resolution


# In[6]:


raw_np= sitk.GetArrayFromImage(raw_img)
raw_np


# In[9]:


assert(raw_np is not None), 'raw cannot be None'
print(raw_np.shape)


# In[10]:


img= raw_np[150, :, :]
print("img shape:", img.shape)
print("img ndim:", img.ndim)
print("img min: {}, max: {}".format(img.min(), img.max()))


# In[13]:


plt.figure(figsize=(12, 8))
plt.imshow(img, cmap='gray')
plt.title= "raw data"
plt.show()

