# -- coding: utf-8 --
"""
Created on Sun Oct 18 17:21:37 2020

@author: rashm
"""
from bokeh.plotting import figure,show, output_file
from bokeh.layouts import column, row
import math

output_file("age_d.html")

fp = open("adult.data",'r')

#age distribution

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

fp.close()

#marital status distribution

M={}

m_status=[]
m_count=[]

#print(fp.readline())
fp = open("adult.data",'r')

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

f2=figure(title = "Marital Status Distribution", x_range = m_status ,
          plot_width = 400,plot_height=400)
f2.xaxis.major_label_orientation = math.pi/2
f2.vbar(x=m_status,top = m_count,width=0.5)


fp.close()

#working class distribution

W={}

w_status=[]
w_count=[]

#print(fp.readline())
fp = open("adult.data",'r')

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


f3=figure(title = "Working class Distribution", x_range = w_status ,
          plot_width = 400,plot_height=400)
f3.xaxis.major_label_orientation = math.pi/2
f3.vbar(x=w_status,top = w_count,width=0.5)

fp.close()

#education distribution

E={}

e_status=[]
e_count=[]

#print(fp.readline())
fp = open("adult.data",'r')

for line in fp:
    A = line.split(",")    
    ec = A[3]
    if ec in E:
        E[ec] = E[ec]+1
    else:
        E[ec] = 1
        
for i in E:
    e_status.append(i)
    e_count.append(E[i])
    print(i,E[i])


f4=figure(title = "Education Distribution", x_range = e_status ,
          plot_width = 400,plot_height=400)
f4.xaxis.major_label_orientation = math.pi/2
f4.vbar(x=e_status,top = e_count,width=0.5)


#combining all To create dashboard
show(row(column(f1, f2),column( f3,f4)))
 
fp.close()