import csv 
import matplotlib.pyplot as plt
import numpy
import math
import re
#metaclasses allow for iteration
class IterRectangle(type):
    def __iter__(cls):
        return iter(cls.RectangleList)
class IterCircle(type):
    def __iter__(cls):
        return iter(cls.CircleList)
class IterTriangle(type):
    def __iter__(cls):
        return iter(cls.TriangleList)
#shape classes
class Rectangle(metaclass = IterRectangle):
    RectangleList = []

    def __init__(self,name, l, w):
        self.RectangleList.append(self)

        self.name = name
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
class Circle(metaclass = IterCircle):
    CircleList = []
    
    def __init__(self,name, r):
        self.CircleList.append(self)

        self.name = name
        self.radius = r

    def circle_area(self):
        return math.pi*self.radius*self.radius
class Triangle(metaclass = IterTriangle):
    TriangleList = []

    def __init__(self, name, b, h):
        self.TriangleList.append(self)

        self.name = name
        self.base = b
        self.height  = h

    def triangle_area(self):
        return (self.base*self.height)/2
#list and for loops
if __name__ == '__main__':
    Rectangle1 = Rectangle("Rectangle 1",1,5)
    Rectangle2 = Rectangle("Rectangle 2",8,1)
    Rectangle3 = Rectangle("Rectangle 3",10,3)
    Circle1 = Circle("Circle 1",3)
    Circle2 = Circle("Circle 2",3)
    Circle3 = Circle("Circle 3", 9)
    Triangle1 = Triangle("Triangle 1",8,1)
    Triangle2 = Triangle("Triangle 2",9,3)
    Triangle3 = Triangle("Triangle 3",10,4)
    Triangle4 = Triangle("Triangle 4",5,4)

    for instance in Rectangle:
        print("The area of " + instance.name + " is: " + str(instance.rectangle_area()))
    for instance in Circle:
        print("The area of " + instance.name + " is: " + str(instance.circle_area()))
    for instance in Triangle:
        print("The area of " + instance.name + " is: " + str(instance.triangle_area()))


