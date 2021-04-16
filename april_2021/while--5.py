#!/usr/bin/env python

j = 100
x = 3
i = 5**x*4 #Potência = **
j = j + 40

while x >= 5:
    j = j-15
    x +=1
    i = i+x-j
    continue
print("j= {}, i= {}, x = {}.".format(j,i,x))