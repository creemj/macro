# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:03:34 2016

@author: jcreem
"""

import pandas as pd
import numpy as np

path = '/Users/jcreem/desktop/economics/data/FDI_data/FDI_DATA.csv'

country=[]
years=[]
fdi=[]

with open(path, "rU") as f:
    text=f.readlines()
    #print(text)
    #for rawline in text:    
        #print(rawline)        
     #   adjline=rawline.replace(',',' ').replace('\n','').split(',')
        #print(adjline)
            #if ',' in adjline:
             #   adjline2=adjline.replace(',','.')
              #  print(adjline2)
            #else:
             #   print(rawline)
            #print(line)
    for i,adjline in enumerate(text):
        #l=[]
        adjline=adjline.replace('\n','').replace(',',' ').split(',')
        #print(adjline)
        if i==0:
        #print(line)
            year= adjline[2:]
            print(year)
        if i==260:
            print(adjline)
         #   place=line[0]
          #  values=line[2:]
           # for i,y in enumerate(year):
            #    country.append(place)
             #   years.append(y)
              #  fdi.append(values[i])
#print(country[35],years[35],fdi[35])                
#table=[country,years,fdi]
#print(table)
                
