# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:30:13 2020

@author: rashm
"""

from bokeh.plotting import figure, output_file,show
import math
fp = open("adult.data",'r')
M={}

m_status=[]
m_count=[]

#print(fp.readline())

for line in fp:
    A = line.split(",")    
    ed = A[5]
    if ed in M:
        M[ed] = M[ed]+1
    else:
        M[ed] = 1
        
for i in M:
    m_status.append(i)
    m_count.append(M[i])
    print(i,M[i])

f1=figure(title = "Marital Status Distribution", plot_width = 400,plot_height=400, x_range = m_status)
f1.xaxis.major_label_orientation = math.pi/2
f1.vbar(x=m_status,top = m_count,width=0.5)
show(f1)

