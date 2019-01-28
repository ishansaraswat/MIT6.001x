# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:54:59 2019

@author: ishan
"""

balance = 42
annualInterestRate = 0.2 
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12

#for month 0
unpaid_bal = balance - monthlyPaymentRate*balance

for i in range(12):
    rem_bal = unpaid_bal + monthlyInterestRate*unpaid_bal
    #print('Month ' + str(i+1) + ' Remaining balance: ' + str(round(rem_bal, 2)))
    unpaid_bal = rem_bal - monthlyPaymentRate*rem_bal
    
print('Remaining balance: ' + str(round(rem_bal, 2)))


