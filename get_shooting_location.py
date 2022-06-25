#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:39:48 2021
This script is used to create a csv file contains shooting location of images

@author: Yimin Zhang
"""
import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import requests
import re
import reverse_geocoder 
from bs4 import BeautifulSoup






def get_html(url): #定义函数
    headers = {
        'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'
 
    }     #模拟浏览器访问
    response = requests.get(url,headers = headers)       #请求访问网站
    html = response.text       #获取网页源码
    return html                #返回网页源码


# Read file that contains the website url 
df_category = pd.read_csv('*.csv')

df = pd.read_csv('*.csv') 

index_unique = np.unique(df.landmark_id)

id_coordinates = np.empty((0,2))
country = []
boolean = []


for index in tqdm(index_unique):
    url=df_category.category[index]
    soup = BeautifulSoup(get_html(url), 'lxml')   #初始化BeautifulSoup库,并设置解析器

    # for tbody in soup.find_all(name='tbody'):
    swith = False    
    for a in soup.find_all(name='a'): 
        try:
            coordinates = np.array((float(a.attrs['data-lat']), float(a.attrs['data-lon'])))
            # print(coordinates)
            # reverse_geocoder.search(coordinates)
            id_coordinates = np.concatenate((id_coordinates, coordinates[np.newaxis,:]),axis = 0)
            swith = True
            break
        except:
            continue
        
    if swith == False:
        id_coordinates = np.concatenate((id_coordinates, np.array([[0,0]])),axis = 0)
    boolean.append(swith)
    for caption in soup.find_all(name='title'):  
        country.append(caption.string[9:-20])

        
df_histo = pd.DataFrame({'landmark_id':index_unique.flatten(),'gps_lat':id_coordinates[:,0],'gps_lon':id_coordinates[:,1],'name':country,'found':boolean})
df_histo.to_csv("gps_information.csv",index=False, sep=',')        
