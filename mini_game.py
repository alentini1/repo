# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:53:39 2021

@author: alentini1
"""

print("We are currently offering an amzong 1.5% on 5 year CDs")
print("Tell me how much you have...")
print("...I'll tell you what it will be over the next 5 years.")
print("Enter initial deposit:")
initial_deposit = float(input())

    
deposit = 1000
r = .015
print("{:<10s}{:>10s}".format("Year", "Balance"))
print("_"*20)
for year in range (1,6):
    print(f"{year:<10d}{deposit*(1+r)**year:>10.2f}")
    
