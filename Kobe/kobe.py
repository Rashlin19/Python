# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:31:33 2020

@author: rashm
"""
#from bokeh.io import output_file, show,figure
from bokeh.plotting import figure, output_file,show
import pandas as pd
import math

output_file("kobe.html")
df= pd.read_csv('kobe.csv',delimiter=',')
x= list(df['Year'])
y= list(df['PTS'])

x1 =[]
for i in range(21):
    x1.append(i)
    
p=figure(plot_width = 400,plot_height=400,x_range=x1)
p.xaxis.major_label_orientation = math.pi/2
p.line(x1,y,line_width=2)

show(p)