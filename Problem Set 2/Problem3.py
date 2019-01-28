# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:37:27 2019

@author: ishan
"""

balance = 320000
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

monthlyInterestRate = annualInterestRate / 12.0
lower = balance/12.0
upper = balance * (1 + monthlyInterestRate)**12 / 12.0
debt_paid = False

while not debt_paid:
    mon_paymnt = (lower + upper)/2
    rem_balance = evaluate(balance, annualInterestRate, mon_paymnt)
    
    if rem_balance > 0.001:
        lower = mon_paymnt
    elif rem_balance < -0.001:
        upper = mon_paymnt
    elif abs(rem_balance) <= 0.001:
        print('Lowest Payment: ' + str(round(mon_paymnt, 2)))
        debt_paid = True
    
        

