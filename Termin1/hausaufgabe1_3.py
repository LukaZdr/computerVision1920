# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# AUFGABE 3
float1 = float(input('float1: '))
float2 = float(input('float2: '))
float3 = float(input('float3: '))
float4 = float(input('float4: '))
float5 = float(input('float5: '))

liste = [float1, float2, float3, float4, float5]
print(liste)

min = float1
for f in liste:
    if f < min:
        min = f

print('min ' + str(min) + ' ' + str(liste.index(min)))

max = float1
for f in liste:
    if f > max:
        max = f

print('max ' + str(max) + ' ' + str(liste.index(max)))

liste.sort()
print('median ' + str(liste[2]))

countOdd = 0
for f in liste:
    if f%2 != 0:
        countOdd += 1
print('ungerade ' + str(countOdd))

countEven = 0
for f in liste:
    if f%2 == 0:
        countEven += 1
print('gerade ' + str(countEven))

print('unterschiedlich '+ str(len(set(liste))))


wholeNumbers = 0
for f in liste:
    if f == int(f):
        wholeNumbers += 1
print('ganze zahlen: ' + str(wholeNumbers))
print('reelle zahlen: ' + str(5-wholeNumbers))
