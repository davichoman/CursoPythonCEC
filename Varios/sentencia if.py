# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:15:34 2019

@author: CEC
"""
def isPrime(num):
    if num <= 1:
        return False
    for i in range (2,num):
        print(num, i, num%i)
        if (num%i == 0):
            return False
    return True

while True:
    x = input("Ingrese un número: ")
    if(x=='Q' or x == 'q'):
        break
    x=int(x)
    if (isPrime(x)):
        print("El número ", x, "es primo")
    else:
        print("El número ", x, "no es primo")