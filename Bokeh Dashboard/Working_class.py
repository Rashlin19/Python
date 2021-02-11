# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:50:16 2020

@author: rashm
"""

from bokeh.plotting import figure, output_file,show
fp = open("adult.data",'r')
W={}

w_status=[]
w_count=[]

print(fp.readline())

for line in fp:
    A = line.split(",")    
    ed = A[6]
    if ed in W:
        W[ed] = W[ed]+1
    else:
        W[ed] = 1
        
for i in W:
    w_status.append(i)
    w_count.append(W[i])
    print(i,W[i])


f1=figure(title = "Marital Status Distribution", plot_width = 400,plot_height=400)
f1.vbar(x=w_status,top = w_count,width=0.5)
show(f1)

fp.close()