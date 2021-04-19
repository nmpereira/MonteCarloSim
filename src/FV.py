import pandas as pd
from decimal import Decimal
import numpy_financial as npf
from statistics import mean
from array import *
import numpy as np
import decimal

from pandas.core.indexes.base import Index
from  Variables import *
from tabulate import tabulate
import random

x = []
a = []
# listOfN = array('f', [])

# rand_list =array('i', [])
# rate_array=array('i', [])

# num_years_array = array('i', [])
pmt_array = []
pv_array = array('i', [])
rate_array = []
fv_array = []
decimal.getcontext().prec = 10000

# num_years_array = np.array([])
# pmt_array= np.array([])
# pv_array= np.array([])
# rate_array=np.array([])
index_array = []
# print("rate: ",rate,"%")

variables_imported = [
# ["pmt: ",pmt],
# ["pv: ",pv],
# ["Number of entries: ",num_years],
# ["periods for each entry: ",L],
["return_lower: ", return_lower],
["return_upper: ", return_upper],
["amount_lower: ", amount_lower],
["amount_upper: ", amount_upper],
["current_age: ", current_age],
["Age_end: ", Age_end],
]

print(tabulate(variables_imported))
num_years = Age_end - current_age


def randinputs(n_limit, lower, upper):
    n = 0
    # n_limit=10
    # rand_return =[]
    while n < n_limit:
        # for i in n_limit:
        rand_return = random.randint(lower, upper)
        n = n + 1
        return rand_return

# for i in range(num_years):
#     rand_return = (randinputs(num_years, return_lower, return_upper))
#     rand_list.append(rand_return)
    # global rate
    # rate= (rand_return)

# print("rant_list",rand_list)

# rate = (rand_list)
# rate= [10]
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
    
    # y = Decimal(npf.fv(rate, nper, pmt, pv))
    y = (npf.fv(rate, nper, pmt, pv))
    
    # y = (round( Decimal(y), 2))

# nper=1
# for i in range(num_years):
#     nper += 1
#     rate = randinputs(num_years, return_lower, return_upper)
#     future_value((rate/100), nper, pmt, pv)
#     x.append(y)


def indexer(num_years):
    n = 0
    global index_array
    while n < num_years:
        # for n in range(num_years):
            n += 1
            index_array.append(n)
            # print("index_array",index_array)
            # print("n",n)
    a.append(index_array)


def rate(num_years):
    n = 0
    global rate_array
    global rate
    while n < num_years:
            n += 1
            rate = randinputs(1, return_lower, return_upper) / 100
            rate_array.append(rate)
            # print("rate",rate)
            # print("rate_array",rate_array)   
    a.append(rate_array)


def payment(num_years):
    n = 0
    global pmt_array
    global amount
    while n < num_years:
            n += 1
            amount = randinputs(1, amount_lower, amount_upper) * 12
            pmt_array.append(amount)
            # print("rate",amount)
            # print("rate_array",pmt_array)   
    a.append(pmt_array)

    
def presentvalue(num_years):
    n = 1
    global pv_array
    global pv
    pv_array.append(pv)
    while n < num_years:
            n += 1
            pv_array.append(0)
    a.append(pv_array)


indexer(num_years)
rate(num_years)
payment(num_years)
presentvalue(num_years)

# def df_define():
pd.set_option("max_colwidth", None)
a_transposed = []
a_transposed = pd.DataFrame(a).transpose()
a_transposed.columns = ["index", "rate", "pmt", "pv"]


def futurevalue(num_years):
    n = 0
    # df_define()
    rate_index = a_transposed['rate'].loc[0]
    pmt_index = a_transposed['pmt'].loc[0]
    pv_index = abs(a_transposed['pv'].loc[0])
    index_index = a_transposed['index'].loc[0]

    global fv_array
    global fv
    fv_array.append(abs(npf.fv(rate_index, 1, pmt_index, pv_index)))
    for n in range(num_years - 1):
        n += 1
        rate_index = a_transposed['rate'].loc[n]
        pmt_index = a_transposed['pmt'].loc[n]
        pv_index = fv_array[n - 1]
        index_index = a_transposed['index'].loc[n]
        
        fv = round(abs(npf.fv(rate_index, 1, pmt_index, pv_index)), 2)
        fv_array.append(fv)
        
            # print("rate",amount)
            # print("rate_array",pmt_array)  
         
    a.append(fv_array)
    n = num_years - 1
    print("rate", a_transposed['rate'].loc[n])
    print("pmt", a_transposed['pmt'].loc[n])
    print("PV1", fv_array[n - 1])
    print("PV2", a_transposed['pmt'].loc[n])

    print("fv", round(npf.fv(a_transposed['rate'].loc[n], 1, a_transposed['pmt'].loc[n], fv_array[n - 1])), 2)


futurevalue(num_years)

# for n in range(num_years):
#     rate_index = a_transposed['rate'].loc[n]
#     pmt_index= a_transposed['PMT'].loc[n]
#     pv_index= a_transposed['PV'].loc[n]
#     index_index = a_transposed['index'].loc[n]
# print("rate_index",rate_index)
# print("pmt_index",pmt_index)
# print("pv_index",pv_index)
# print("index_index",index_index)


def simulate(num_years):
    n = 0
    while n < num_years:
        # calculating num_years_array
        # print("num_years",n)
        n += 1
        # num_years_array.append(n)
        # calculating rate
        
        rate = 5
        
        rate_array = [1, 2, 3]

        # calcuting pmt
        # pmt_array =[1,2,3]
        pmt = (1000)
        # for n in range(num_years):
        pmt_add = np.arange(pmt, pmt + pmt, pmt / 2)
        # print("pmt_add", pmt_add)
        pmt_array = np.append(pmt, pmt_add + 1)
            # pmt= array.array('d',[1000])
            # pmt +=1000
            # pmt_array.append(pmt)
            # print(pmt_array)

        # calculating pv
        pv = [0]
        pv_array = [10, 20, 30]

        # Calculating future value
        # for i in range(num_years):
        future_value(rate_array, n, pmt_array, pv_array)
        x.append(y)

# print("simulate(num_years)",simulate(num_years))

# print("num_years_array",num_years_array)

# print(("rate_array",rate_array))
# print(("num_years_array",num_years_array))
# print(("pmt_array",pmt_array))
# print(("pv_array",pv_array))

# print(("num_years",num_years))

# print("np.matrix(x)",np.matrix(x))


# print("pd.DataFrame(a_transposed) \n", a_transposed)
a_transposed = pd.DataFrame(a).transpose()
a_transposed.columns = ["index", "rate", "pmt", "pv", "fv"]
print("pd.DataFrame(a_transposed) \n", a_transposed)
a_transposed_row_PV = a_transposed["pv"] + 1

print(a_transposed_row_PV.loc[0] + 50)

# if num_years > 1:
#     ##print('mean: ', round(mean(x), 2))
#     print('mean: ', round((mean(x)), 2))

# callback same file to repeat another calc
print(" ")
print(" ")

print("End of script!")

