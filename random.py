# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:59:35 2019

@author: djkkc
"""

'''
import random

fruit = ["apple", 'peach', 'banana', 'cherry', 'orange']
choice = random.choice(fruit)
print(choice)
'''
'''
import random
coin = ['h','t']
com = random.choice(coin)
user = input('Make a choice: ')
if user == com:
    print('You win')
else:
    print('Bad luck')
    print('The answer is:',com)
'''
'''
import random
num = random.randint(1,5)
user = int(input('Make your choice: '))
if num == user:
    print('u lucky motherfucker')
elif num < user:
    print('too high')
    user = int(input('Make your choice: '))
    if user == num:
        print('correct')
    else:
        print('dumbaaaaaaaaaaaaass')
elif num > user:
    print('too low')
    user = int(input('Make your choice: '))
    if user == num:
        print('correct')
    else:
        print('go fuck urself')
'''
'''
import random
color=['white','yellow','green','black','red']
p = random.choice(color)
u = input('make ur goddamn choice u motherless cocksucker: ')
while p!=u:
    print('the answer is:', p)
    u = input('dont tell me u r a fuckin moron:')
print('fuckoff')
'''