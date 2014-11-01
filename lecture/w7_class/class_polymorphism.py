# -*- coding: utf-8 -*-

class Figure:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def getArea(self):
		pass

class Triangle(Figure):
	def getArea(self):
		return self.width * self.height / 2.0

class Rectangle(Figure):
	def getArea(self):
		return self.width * self.height

myTriangle = Triangle(10,10)
myRectangle = Rectangle(10,10)

print "Triangle Area is", myTriangle.getArea()
print "Rectangle Area is", myRectangle.getArea()

