import math
import matplotlib.pyplot as plt
import numpy
import csv 
import re

shapelist = []
with open('shapes.txt') as csvfile:
    shapes = csv.reader(csvfile)
    for i in shapes:
        shapelist.append(i)
print(shapelist)

reclist = []
for x in shapelist:
    if 'Rectangle' in x:
        y = x 
        reclist.append(y)
print(reclist)

class IterShape(type):
    def __iter__ (cls):
        return iter(cls.reclist)

class Rectangle(metaclass = IterShape):
    reclist = []
    def __init__(self,name, l, w):
        self.reclist.append(self)

        self.name = name
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width




for instance in Rectangle:
    print("The area of " + instance.name + " is: " + str(instance.rectangle_area()))

