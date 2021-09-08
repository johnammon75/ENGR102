# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Ammon
# Section:      528
# Assignment:   lab0b-2
# Date:         3 9 2021
#
import math

print("This shows the evaluation of (e^x-1)/x evaluated close to x=0")
print("My guess is 1")

print((math.exp(1) -1)/1)
print((math.exp(0.1) -1)/0.1)
print((math.exp(0.01) -1)/0.01)
print((math.exp(0.001) -1)/0.001)
print((math.exp(0.0001) -1)/0.0001)
print((math.exp(0.00001) -1)/0.00001)
print((math.exp(0.000001) -1)/0.000001)
print((math.exp(0.0000001) -1)/0.0000001)

print("\nMy guess was a little off")
