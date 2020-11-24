import csv 
import matplotlib.pyplot as plt
import numpy
import math
import re

shapelist = []
with open('shapes.txt') as csvfile:
    shapes = csv.reader(csvfile)
    for i in shapes:
        shapelist.append(i)

class IterRectangle(type):
    def __iter__(cls):
        return iter(cls.RectangleList)

class Rectangle(metaclass = IterRectangle):
    RectangleList = []
    RecLenList = []
    RecWidList = []
    for i in shapelist:
        if 'Rectangle' in i:
            RectangleList.append([i])
            RecLenList.append(int(i[1]))
            RecWidList.append(int(i[2]))

    def __init__(self, l, w):
        self.RectangleList.append(self)
        self.RecLenList.append(l)
        self.RecWidList.append(w)

        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width



#print(Rectangle(Rectangle.RecLenList[0], Rectangle.RecWidList[0]).rectangle_area())

#print(Rectangle.RectangleList)

for i in Rectangle.RectangleList:
    print(Rectangle(Rectangle.RecLenList[0], Rectangle.RecWidList[0]).rectangle_area())

#Rectangle1 = Rectangle(Rectangle.RecLenList[0],Rectangle.RecWidList[0])
#print(Rectangle1.rectangle_area())


#print("The area of is: " + str(Rectangle.rectangle_area([Rectangle1])))
