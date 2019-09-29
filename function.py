# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:07:06 2019

@author: djkkc
"""
namelist = ["qwe", "asd", 'zxc']
def name(n):
    x = None
    while x != "e":
        x = input("Enter 'a' for add,\n'c' for change,\n'd' for delete,\n'v' for view,\n'e' for exit: ")
        if x == 'a':
            a = input("Please add a name: ")
            n.append(a)
        elif x == 'c':
            c = input ("Please select a name: ")
            if c in n:
                o = input ("The name will be changed to: ")
                n.remove(c)
                n.append(o)
            else:
                print("There is no match.")     
        elif x == "d":
            d = input("Which name do you like to delete? ")
            n.remove(d)
        elif x == "v":
            print(n)
        elif x == "e":
            print("Thank you.")
        else:
            print("Invalid input. ")
    return 
name(namelist)

        