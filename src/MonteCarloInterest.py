import random
from  Variables import *
from tabulate import tabulate
import pandas as pd
import numpy as np
import numpy_financial as npf
import statistics
from numba import jit
import time
from datetime import timedelta


start_time = time.monotonic()

variables_imported = [
 #["pmt: ",pmt],
 ["pv: ",pv],
# ["Number of entries: ",num_years],
# ["periods for each entry: ",L],
["return_lower: ", return_lower],
["return_upper: ", return_upper],
["amount_lower: ", amount_lower],
["amount_upper: ", amount_upper],
["current_age: ", current_age],
["Age_end: ", Age_end],
["simulation_trials: ", simulation_trials],
]

print(tabulate(variables_imported))
num_years = Age_end - current_age
Grand_Future_Value=[]
Grand_Future_Value_mean=[]


def simulate(trials):
    for trial in range(trials):
        index=np.array([])
        nper=np.array([])
        data=[]
        PresentValue=[]
        AnnualRate=np.array([])
        PaymentAmount=[]
        FutreValue=[]
        
        
       
        def randomizer(lower, upper):
            return round(random.uniform(lower, upper), 2)

        #def num_years():
        #    pass

        def indexer(num_years):
            index=np.arange(num_years)
            #for years in range(num_years):
            #    index.append(years)
            data.append(index)
            return index
                

        def rate(return_lower, return_upper):
            return randomizer(return_lower, return_upper)

        def Nperiod(index):
            nper=np.arange(index)+1
            #for i in range(index):
            #    nper.append(i+1)
            data.append(nper)
            return nper

        def pmt(amount_lower, amount_upper):
            return randomizer(amount_lower, amount_upper)

        def present_value(index):
            for i in index:
                PresentValue.append(0)
            #PresentValue[1]= pv
            data.append(PresentValue)
            return PresentValue
        def Annual_rate(index):
            AnnualRate =np.full((1,50),random.random())
            #AnnualRate = np.array([random.random() for _ in range(index)])
            # for i in index:
            #     AnnualRate.append(rate(return_lower, return_upper))
            data.append(AnnualRate)
            print(AnnualRate)
            return AnnualRate
        def Payment_amount(index):
            for i in index:
                PaymentAmount.append(pmt(amount_lower, amount_upper))
            data.append(PaymentAmount)
            return PaymentAmount
        
        def Future_value(index):
            def futureval(AnnualRate,index,PaymentAmount, PresentValue):
                return round(npf.fv(AnnualRate, index, PaymentAmount, PresentValue),2)

                

            for i in index:
                if i ==0:
                    FutreValue.append(futureval(AnnualRate[i]/100,nper[i],PaymentAmount[i], PresentValue[i]))
                    
                else:
                    FutreValue.append(futureval(AnnualRate[i]/100,nper[i],PaymentAmount[i], PresentValue[i]+PresentValue[0]))
                    
            data.append(FutreValue)
            return FutreValue




        dataframe = []
        #dataframe.clear()
        
        pmt(amount_lower, amount_upper)
        indexer(num_years)
        Nperiod(num_years)
        present_value(index)
        Annual_rate(index)
        Payment_amount(index)
        Future_value(index)



        # print("rate:",return_lower, return_upper)
        # print("pmt:",pmt(amount_lower, amount_upper))
        # print("num_years:",num_years)

        # print("indexer:",indexer(num_years))
        # print("Nperiod:",Nperiod(num_years))
        # print("present_value:", present_value(index))
        # print("Annual_rate:",Annual_rate(index))
        # print("Payment_amount:",Payment_amount(index))
        # print("Future_value:",Future_value(index))

        pd.set_option("max_colwidth", None)
        dataframe = pd.DataFrame(data).transpose()
        dataframe.columns = ["index","Year", "Present Value", "rate","Payment Amount", "Future Value"]


        
        dataframe['index']=dataframe['index'].map('{:,.0f}'.format)
        dataframe['Year']=dataframe['Year'].map('{:,.0f}'.format)

        dataframe['rate']=dataframe['rate'].map('{:.3f} %'.format)
        dataframe['Payment Amount']=dataframe['Payment Amount'].map('$ {:,}'.format)
        dataframe['Present Value']=dataframe['Present Value'].map('$ {:,}'.format)

        #print("pd.DataFrame(dataframe) \n", dataframe)
        
        Grand_Future_Value.append(dataframe['Future Value'].iloc[-1])
        

        dataframe['Future Value']=dataframe['Future Value'].map('$ {:,}'.format)
        if trial==0:
            print("pd.DataFrame(dataframe) \n", dataframe)

simulate(2000)
pd.set_option('display.float_format', '$ {:,}'.format)
Grand_dataframe = pd.DataFrame(Grand_Future_Value)
Grand_dataframe.columns = ["Trials"]
print("Grand_dataframe \n",Grand_dataframe)
Grand_Future_Value_mean=statistics.mean(Grand_Future_Value)
print( "Average: ",'$ {:,}'.format(round(Grand_Future_Value_mean,2)))

print(Grand_dataframe.describe())

#input("Press Enter to continue.")
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))