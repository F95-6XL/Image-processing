# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:46:30 2021
Download images from online database
@author: Joachim
"""


import os
import pandas as pd
import requests
from tqdm import tqdm


# Function to create new folder
def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                 
		os.makedirs(path)           


def urllib_download(IMAGE_URL,path):
    """
    Use "request" to download images

    Parameters
    ----------
    IMAGE_URL : string
        URL of the image.
    path : string
        Local path to save the image.

    Returns
    -------
    None.

    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
    
    r = requests.get(IMAGE_URL,headers=headers)   
    with open(path,'wb') as f:
        f.write(r.content)
        
		
data = pd.read_csv('data.csv')
# data = data.head(100)

l_id = data.landmark_id[0]
file = ".\\training_data_clean\\"

for i in tqdm(range(len(data))):
    path = os.path.join(file,str(data.iat[i,3]))
    mkdir(path)  
    try:
        urllib_download(data.iat[i,2],path+'\\'+str(data.iat[i,1])+'.jpg')
    except:
        pass


