# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:26:12 2019

@author: DBA
"""

print ("### Visualiza el contenido el archivo ###")
file=open("devices.txt","r")
for item in file:
    # elimina espacios en blanco
    item=item.strip()
    print(item)
file.close()


print ("### Almacena en un lista ###")
devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)