#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:11:19 2019

@author: fahadtariq
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transation = []
for i in range(0,7501):
    transation.append([str(dataset.values[i,j]) for j in range(0,20)])
        
 #training the model   
from apyori import apriori
results =  apriori(transation , min_support= 0.003 , min_confidence=0.2, min_lift= 3 , min_length = 2) 
    
#Visualizing the Results
results = list(rules)
    
clean_results = []
for i in range(0, len(results)):
    clean_results.append('RULE:\t' + str(results[i][0]) + '\nSUPPORT:\t' + str(results[i][1]) + '\nCONFIDENCE:\t' + str(results[i][2][0][2]) + '\nLIFT:\t' + str(results[i][2][0][3]))
    
    
 '''   
list_array = []

for i in range(0,7501):
    for j in range(0,20):
        list_array.append([str(dataset.values[i,j])])'''
        
        
    