from decimal import Decimal
import numpy_financial as npf
from statistics import mean
from array import *
import FV
import numpy as np

x= []

# rate = int(input("Enter Rate: "))
# pmt= int(input("Enter PMT: "))
# pv = int(input("Enter PV: "))
# listOfN = array('i',[])

rate = 5
pmt= 1000
pv = 10000
listOfN = array('i',[])



n = int(input("Number of entries: "))
for i in range(n):
    L = int(input("Enter the periods for each entry: "))
    listOfN.append(L)


def future_value(rate, nper, pmt, pv):  
    global y
    #y = int()
    y = Decimal(npf.fv(rate, nper, pmt, pv))
    y = (round(y, 2))
    


for nper in listOfN:
    future_value((rate/100), nper, pmt, pv)
    x.append(y)
    



print(np.matrix(x))

import pandas as pd
pd.set_option("max_colwidth", None)
print(pd.DataFrame(x))

if n>1:
    print('mean: ', round(mean(x), 2))

#callback same file to repeat another calc
print(" ")
print(" ")
FV

input("Press enter to start another calculation")

