# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:31:33 2020

@author: rashm
"""
#from bokeh.io import output_file, show,figure
from bokeh.plotting import show, output_file,figure
import pandas as pd
import math


output_file("kobe.html")
df= pd.read_csv('kobe.csv',delimiter=',')
xlabels= list(df['Year'])
y= list(df['PTS'])

x=[]
for s in range(1,21,1):
    x.append(s-0.5)

    
p=figure(plot_width =600,plot_height=400,x_range=xlabels, title = " Kobe Bryant points - Line graph")
p.xaxis.major_label_orientation = math.pi/2
p.line(x,y,line_width=1)

show(p)