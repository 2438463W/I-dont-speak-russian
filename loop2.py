# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:36:09 2019

@author: djkkc
"""
"""
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
t = a + b
q = "y"
while q == "y":
    q = input("Do want an another number? ")
    if q == "y":
        c = int(input("Enter a number: "))
        t = t + c
print ("\nThe sum is: ",t)    
"""
'''
compnum = 50
num = int(input("Enter a number: "))
count=1
while num != 50:
    if num > 50:
        print ("Your number is a bit higher. ")
        num = int(input("Try again: "))
    elif num < 50:
        print ("Your number is a bit lower.")
        num = int(input("Try again: "))
    count=count+1
print ("Well done, you took", count,"attempts. ")
'''
'''
def product(*nums, scale=1):
    p = scale
    for n in nums:
        p *= n
    return 
print(product(3,5))
'''