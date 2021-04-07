from decimal import Decimal
import numpy_financial as npf
from statistics import mean
from array import *
#import FV
import numpy as np
import decimal

x= []

rate = int(input("Enter Rate: "))
pmt= int(input("Enter PMT: "))
pv = int(input("Enter PV: "))
listOfN = array('i',[])




num = int(input("Number of entries: "))
for i in range(num):
    L = int(input("Enter the periods for each entry: "))
    listOfN.append(L)


def future_value(rate, nper, pmt, pv):  
    global y
    #y = int()
    
    decimal.getcontext().prec=10000
    y = Decimal(npf.fv(rate, nper, pmt, pv))
    y = (round(y, 2))
    


for nper in listOfN:
    future_value((rate/100), nper, pmt, pv)
    x.append(y)
    



print(np.matrix(x))

import pandas as pd
pd.set_option("max_colwidth", None)
print(pd.DataFrame(x))

if num>1:
    #print('mean: ', round(mean(x), 2))
    print('mean: ', (mean(x)))

#callback same file to repeat another calc
print(" ")
print(" ")
#FV

input("Press enter to start another calculation")

