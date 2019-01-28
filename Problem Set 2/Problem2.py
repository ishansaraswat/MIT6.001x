# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:28:21 2019

@author: ishan
"""

balance = 3926
annualInterestRate = 0.2

def evaluate(balance, annualInterestRate, mon_pay, n=12):
    '''
    Inputs: balance, annual interest rate, monthly payment amount, number of months
    Returns: remaining balance at the end of year
    '''
    monthlyInterestRate = annualInterestRate/12.0
    unpaid_balance = balance - mon_pay
    updated_balance = unpaid_balance * (1 + monthlyInterestRate)
    n -= 1
    if n == 0:
        return round(updated_balance, 2)
    else:
        return evaluate(updated_balance, annualInterestRate, mon_pay, n)

mon_pay = 10
debt_paid = False

while not debt_paid:
    rem_balance = evaluate(balance, annualInterestRate, mon_pay)
    if rem_balance > 0:
        mon_pay += 10
    else:
        print('Lowest Payment: $' + str(mon_pay))
        break
    
 