# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:12:37 2020

@author: rashm
"""

import pandas as pd
from bokeh.plotting import figure
 
d ={}
#==================
def get_all_lab(df,cid):
    x= df[cid].unique()
    return x 

# get label count for all age groups

def get_lab_cnts_ages(df,cid):
    dis=[]
    age_grp=[]
    
    for x in range (20,110,10):
        upper = x
        if upper ==20:
            lower = 0
        else:
            lower = x-10
            
        df_x = df [(df[0]>=lower )& (df[0]<upper)]
        x = df_x[cid].value_counts()
        lbls = x.keys()
        cnts = x.tolist()
        d = dict(zip(lbls,cnts))
        dis.append(d)
        age_grp.append(str(lower) + "," +str(upper))
    return (age_grp,dis)

def fig(d, all_lab):
    x=[]
    y=[]
    for l in all_lab:
        x.append(l)
        if l in d:
            y.append(d[1])
        else:
            y.append(0)
    f = figure(x_range=x, plot_width =300,plot_heinght = 300)
    f.vbar(x=x,top=y,width=0.2)
    return f
#====================================

        #print(lower," ",upper)
        #print(x)
    
        

df = pd.read_csv("C:/Fall 2020/IFT 598 - Data Visualization/data/US_CENSUS/adult.txt",header=None)
#print(df)

(age_grp_mart,dis_mar) = get_lab_cnts_ages(df,5)
mart-labls = get_all_lab
#print(age_grp)
#print(dis)



get_lab_cnts_ages(df,5)
a = get_all_lab(df,5)
print(a)


'''
df_x = df[df[0]<20]
print(df_x)

x = df_x[5].value_counts()
print(x)

df_y= df[(df[0]>=20) & (df[0]<30)]
y = df_y[5].value_counts()
print(y)
'''