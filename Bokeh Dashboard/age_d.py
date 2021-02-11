# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:15:45 2020

@author: rashm
"""
from bokeh.plotting import figure, output_file,show
#import pandas as pd
#import math

output_file("age_d.html")
fp = open("adult.txt",'r')
age_counts ={}

age_category = []
count = []

for line in fp:
    A = line.split(",") 
    age = int(A[0])
    cat = int(age/10) *10
  
    if cat in age_counts:
        age_counts[cat]= age_counts[cat]+1
    else:
        age_counts[cat] = 1 
        
    
for a in range(10,100,10):
    if a in age_counts:
        age_category.append(a)
        count.append(age_counts[a])
        print(a,age_counts[a])
        
f1=figure(title = "Age Distribution", plot_width = 400,plot_height=400)
f1.vbar(x=age_category,top = count,width=0.5)
show(f1)





        
    
                
               
            
        
       
        
                
      
        
    


        
        
    