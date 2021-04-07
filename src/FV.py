import pandas as pd
from decimal import Decimal
import numpy_financial as npf
from statistics import mean
from array import *
#import FV
import numpy as np
import decimal

x = []
listOfN = array('f', [])


def isfloatnum(promptflt):
    while True:
        try:
            valuefl = float(input(promptflt))
        except ValueError:
            print("Try again!")
        else:
            break
    return valuefl


def isintnum(promptint):
    while True:
        try:
            valueint = int(input(promptint))
        except ValueError:
            print("Try again!")
        else:
            break
    return valueint


rate = isfloatnum("Enter Rate: ")
pmt = isfloatnum("Enter PMT: ")
pv = isfloatnum("Enter PV: ")
num = isintnum("Number of entries: ")

for i in range(num):
    L = isfloatnum("Enter the periods for each entry: ")
    listOfN.append(L)


def future_value(rate, nper, pmt, pv):
    global y
    decimal.getcontext().prec = 10000
    y = Decimal(npf.fv(rate, nper, pmt, pv))
    y = (round(y, 2))


for nper in listOfN:
    future_value((rate/100), nper, pmt, pv)
    x.append(y)


print(np.matrix(x))

pd.set_option("max_colwidth", None)
print(pd.DataFrame(x))

if num > 1:
    #print('mean: ', round(mean(x), 2))
    print('mean: ', round((mean(x)), 2))

# callback same file to repeat another calc
print(" ")
print(" ")
# FV

input("Press enter to start another calculation")
