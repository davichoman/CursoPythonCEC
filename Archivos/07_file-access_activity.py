# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:43:38 2019

@author: DBA
"""

file=open("devices.txt","a")
while True:
    newItem=input("Ingrese un nuevo dispositivo: ")
    if newItem == "exit":
        print("All done!")
        break
    file.write(newItem.strip() + "\n")
file.close()
    