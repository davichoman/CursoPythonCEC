# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 09:12:22 2019

@author: CEC
"""

def isPrime(num):
    if num <= 1:
        return False
    for i in range (2,int(num**0.5)+1):
        if (num%i == 0):
            return False
    return True

for i in range(1, 100):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
