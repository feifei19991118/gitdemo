# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:45:54 2019

@author: CYF
"""

d=[]
for i in range(7):
    a,b=map(int,input().split())
    c=a+b
    d.append(c)
for i in range(len(d)):
    if d[i]<=8:
        d[i]==0
if d.count(0)==7:
    print(0)
else:
    e=max(d)
    f=d.index(e)
    print(f+1)
