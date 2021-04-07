import numpy_financial as npf
from statistics import mean
from array import *
import FV

x= []



rate = int(input("Enter Rate: "))
listOfN = array('i',[])
pmt= int(input("Enter PMT: "))
pv = int(input("Enter PV: "))

n = int(input("Number of entries: "))
for i in range(n):
    L = int(input("Enter the periods for each entry: "))
    listOfN.append(L)


def future_value(rate, nper, pmt, pv):  
    global y 
    y= npf.fv(rate, nper, pmt, pv)
    


for nper in listOfN:
    future_value((rate/100), nper, pmt, pv)
    x.append(y)

print(x)
if n>1:
    print('mean: ', mean(x))

#callback same file to repeat another calc
print(" ")
print(" ")
FV

input("Press enter to start another calculation")

