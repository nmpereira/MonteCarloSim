import numpy_financial as npf
from statistics import mean
from array import *

x= []
nperlist = array('i',[])

n = int(input("Number of entries: "))
for i in range(n):
    L = int(input("Enter a number: "))
    nperlist.append(L)


def future_value(rate, nper, pmt, pv):  
    global y 
    y= npf.fv(rate, nper, pmt, pv)

for i in range(10):
    for nper in nperlist:
        future_value(0.05/12, nper*12, -100, -100)
        x.append(y)


print(mean(x))

input()

