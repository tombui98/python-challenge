#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 18:23:33 2023

@author: tombui
"""
import os
import pandas as pd
path = os.getcwd()
file_name = os.path.join(path, r'Resources/budget_data.csv')

df = pd.read_csv (file_name)
total_month = df.shape[0]
net_profit = df.iloc[:,1].sum()

total_change = 0
greatest_increase, greatest_decrease = 0,0
month_increase, month_decrease = '', ''
num_change = 0
for i in range(1, total_month):
  change = df.iloc[i, 1] - df.iloc[i-1, 1]
  if change != 0:
    total_change += change # total_change = total_change + change
    num_change += 1
    if change> greatest_increase:
      greatest_increase = change
      month_increase = df.iloc[i, 0]
    if change < greatest_decrease:
      greatest_decrease = change
      month_decrease = df.iloc[i, 0]
average_change = total_change/num_change

print("Financial Analysis")
print("----------------------------")
print("Total Months: %d"%total_month)
print("Total: $%d"%net_profit)
print("Average Change: $%.2f"%average_change)
print("Greatest Increase in Profits: %s ($%d)"%(month_increase, greatest_increase))
print("Greatest Decrease in Profits: %s ($%d)"%(month_decrease, greatest_decrease))

file_name = os.path.join(path, r'analysis/results.txt')
f = open(file_name, 'w')
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write("Total Months: %d\n"%total_month)
f.write("Total: $%d\n"%net_profit)
f.write("Average Change: $%.2f\n"%average_change)
f.write("Greatest Increase in Profits: %s ($%d)\n"%(month_increase, greatest_increase))
f.write("Greatest Decrease in Profits: %s ($%d)\n"%(month_decrease, greatest_decrease))
f.close()