# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:26:53 2019

@author: djkkc
"""
'''
num=[123,234,345,456]
for i in num:
    print(i,'\n')
user=int(input('enter number: '))
if user in num:
    print('the position is',num.index(user))
else:
    print('no match')
'''
'''
names=[]
for i in range(0,3):
    guest=input('Enter a name: ')
    names.append(guest)
a = input('Do you want to add more? ')
while a != 'no':
    guest=input('Enter a name: ')
    names.append(guest)
    a = input('Do you want to add more? ')
print(len(names),'people are invited.')
'''
'''
counts={}
while len(counts)<5:
    s = input('Enter a string: ')
    if s in counts:
        counts[s]=counts[s]+1
    else:
        counts[s]=1
for k in counts:
    print(counts)
'''
'''
food={}
for i in range(1,5):
    food[i]=input('Enter you favorite food: ')
print(food)
rid=int(input('which pair do you wanna remove: '))
del food[rid]
food=sorted(food)
print(food)
'''
'''
name=('China','Korea','Japan','UK','US')
print(name)
user=input('enter a country: ')
print(name.index(user))
ind=int(input('enter a number: '))
print(name[ind])
'''
'''
from array import*
nums=array('i',[])
for i in range(0,5):
    new=int(input('enter: '))
    nums.append(new)
nums=sorted(nums)
nums.reverse()
print(nums)
'''
'''
import random
from array import*
num=array('i',[])
for i in range(0,5):
    a=random.randint(1,100)
    num.append(a)
    print(num[i])
'''
'''
import random,numpy
unum=array('i',[])
for i in range(0,3):
    value=int(input('Enter: '))
    unum.append(value)
rnum=array('i',[])
for i in range(0,5):
    a=random.randint(1,100)
    rnum.append(a)
unum.extend(rnum)
unum=sorted(unum)
for i in range(0,len(unum)):
    print(unum[i])
'''
'''
import numpy
num=array('i')
save=array('i')
for i in range(0,5):
    a=int(input('Enter: '))
    num.append(a)
num=sorted(num)
b=int(input('select: '))
num.remove(b)
save.append(b)
print(num)
save=sorted(save)
print(save)
'''
'''
import numpy
num=array('i',[23,63,124,73,21])
print(num)
a=int(input('select: '))
if a in num:
    b=num.index(a)
    print(b)
else:
    while a not in num:
        a=int(input('select again: '))
    b=num.index(a)
    print(b)
'''
'''
import numpy
num=array('f',[12.32,124.21,46.23,63.12,88.09])
a=int(input('enter between 2 and 5: '))
if a in range(2,6):
    for i in range(0,len(num)):
        num[i]=num[i]/a
        b=num[i]
        print('%.2f'%b)
else:
    while a not in range(2,6):
        a=int(input("DUDE: "))
    for i in range(0,len(num)):
        num[i]=num[i]/a
        b=num[i]
        print('%.2f'%b)
'''
'''
list1=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
a=int(input('Select row: '))
b=int(input('Select column: '))
print(list1[a][b])
'''
'''
list1=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row=int(input('Select row: '))
print('The row u select: ',list1[row])
value=int(input('Add new value: '))
list2=list1[row]
list2.append(value)
list1[row]=list2
print(list1[row])
'''
'''
list1=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row=int(input('Select row: '))
print('The row u select is: ',list1[row])
column=int(input('Select column:'))
print('ur choice', list1[row][column])
a=input('Do you want to change? ')
if a == 'yes':
    b=int(input('Change to: '))
    list1[row][column]=b
    print(list1[row])
else:
    print('error')
'''
list1={}
for i in range(0,4):
    name=input('Enter a name: ')
    list1.keys()
print(list1)
