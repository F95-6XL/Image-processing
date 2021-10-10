# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:24:02 2021

@author: Joachim
"""
import pandas as pd
import numpy as np
import glob, os
from PIL import Image
from tqdm import tqdm

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                 
		os.makedirs(path) 
        
path = [] # Path of images to be compressed
path_new = [] # Path to store the compressed images


images=glob.glob(path, recursive=True)

mkdir(path_new)

for image in tqdm(images):
    try:
        with open(image, 'rb') as f:
            img = Image.open(f)
            new_image = img.resize((224, 224))  
            new_image.save(path_new+os.path.basename(image))
    except:
        print(1) 
    
    
    
    

 