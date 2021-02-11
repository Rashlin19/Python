# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:02:35 2020

@author: rashm
"""
from bokeh.plotting import figure,show
from bokeh.layouts import column
#import pandas as pd
#import math

#output_file("age_d.html")
fp = open("adult.data",'r')
age_counts ={}

#age distribution

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


#marital status distribution

M={}

m_status=[]
m_count=[]

print(fp.readline())

for line in fp:
    A = line.split(",")    
    ma = A[5]
    if ma in M:
        M[ma] = M[ma]+1
    else:
        M[ma] = 1
        
for i in M:
    m_status.append(i)
    m_count.append(M[i])
    print(i,M[i])


f2=figure(title = "Marital Status Distribution", plot_width = 400,plot_height=400)
f2.vbar(x=m_status,top = m_count,width=0.5)
show(f2)

#working class distribution
W={}

w_status=[]
w_count=[]

print(fp.readline())

for line in fp:
    A = line.split(",")    
    wc = A[6]
    if wc in W:
        W[wc] = W[wc]+1
    else:
        W[wc] = 1
        
for i in W:
    w_status.append(i)
    w_count.append(W[i])
    print(i,W[i])


f3=figure(title = "Working class Distribution", plot_width = 400,plot_height=400)
f3.vbar(x=w_status,top = w_count,width=0.5)
show(f3)

#education distribution


#combining all To create dashboard
show(column(f1, f2, f3))
 
fp.close()
