# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:50:38 2019

@author: DBA
"""

def fib(n):
    myList = []
    a, b = 0,1
    while a < n:
        myList.append(a)
        #asignación múltiple de derecha a izquierda
        a,b = b, a+b
    return myList