import pandas as pd
from decimal import Decimal
import numpy_financial as npf
from statistics import mean
from array import *
import numpy as np
import decimal
from  Variables import *
from tabulate import tabulate
import random

x = []
listOfN = array('f', [])

rand_list =array('i', [])
rate_array=array('i', [])

# num_years_array = array('i', [])
# pmt_array= array('i', [])
# pv_array= array('i', [])

num_years_array = np.array([])
pmt_array= np.array([])
pv_array= np.array([])

#print("rate: ",rate,"%")

variables_imported = [
["pmt: ",pmt],
["pv: ",pv],
["Number of entries: ",num_years],
["periods for each entry: ",L],
["return_lower: ",return_lower],
["return_upper: ",return_upper],
["amount_lower: ",amount_lower],
["amount_upper: ",amount_upper],
["current_age: ",current_age],
["Age_end: ",Age_end],
]

print(tabulate(variables_imported))
num_years = Age_end - current_age




def randinputs(n_limit, lower, upper):
    n = 0
    # n_limit=10
    #rand_return =[]
    while n < n_limit:
        #for i in n_limit:
        rand_return = random.randint(lower, upper)
        n = n + 1
        return rand_return
    

# for i in range(num_years):
#     rand_return = (randinputs(num_years, return_lower, return_upper))
#     rand_list.append(rand_return)
    #global rate
    # rate= (rand_return)
    

#print("rant_list",rand_list)

#rate = (rand_list)
#rate= [10]
# for i in rand_list:
#     rate.append(rand_list)




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





# rate = isfloatnum("Enter Rate: ")
# pmt = isfloatnum("Enter PMT: ")
# pv = isfloatnum("Enter PV: ")
# num_years = isintnum("Number of entries: ")

# for i in range(num_years):
   
#     #L = isfloatnum("Enter the periods for each entry: ")
#     listOfN.append(L)


def future_value(rate, nper, pmt, pv):
    global y
    decimal.getcontext().prec = 10000
    #y = Decimal(npf.fv(rate, nper, pmt, pv))
    y = (npf.fv(rate, nper, pmt, pv))
    #y = (round( Decimal(y), 2))

# nper=1
# for i in range(num_years):
#     nper += 1
#     rate = randinputs(num_years, return_lower, return_upper)
#     future_value((rate/100), nper, pmt, pv)
#     x.append(y)



def simulate(num_years):
    n = 0
    while n < num_years:
        #calculating num_years_array
        #print("num_years",n)
        n+=1
        #num_years_array= np.append(n)
        #calculating rate
        
        rate = 5
        
        rate_array= [1,2,3]


        #calcuting pmt
        pmt= 1000
        #pmt_array= np.append(pmt+100)

        #calculating pv
        pv= [0]
        #pv_array = np= np.append(pmt)


        #Calculating future value
        for i in range(num_years):
            future_value(rate_array, rate_array, rate_array, rate_array)
            x= np.append(y)




simulate(num_years) 
#print("num_years_array",num_years_array)


print((rate_array))
print((num_years_array))
print((pmt_array))
print((pv_array))










#print(np.matrix(x))

pd.set_option("max_colwidth", None)
print(pd.DataFrame(x))


#if num_years > 1:
    ##print('mean: ', round(mean(x), 2))
    #print('mean: ', round((mean(x)), 2))

# callback same file to repeat another calc
print(" ")
print(" ")

print("End of script!")


