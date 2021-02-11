# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:13:32 2020

@author: rashm
"""


m={}
c=0
fp = open("adult.txt", "r")
B=[]

for line in fp:
    #c+=1
    A = line.split(",")    
    try:
        ed = A[3]
    except IndexError:
        break
    #print(ed,"\n")
    if ed in B:
        continue
    B.append(ed)
print(B)
    
#for M in m :
#    print(m[M],"\n",M)
 #   print ("number of education statuses are",len(m))
 
fp.close()