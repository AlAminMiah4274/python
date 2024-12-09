from math import pi


class Shape:

	def __init__(self, name):
		self.name = name



class Rectangle(Shape):

	def __init__(self, name, lenght, width):
		self.lenght = lenght
		self.width = width
		super().__init__(name)

	def area(self):
		return self.lenght * self.width


class Circle(Shape):

	def __init__(self, name, radius):
		self.radius = radius

	def area(self):
		return pi * self.radius*self.radius



my_land = Rectangle("personal wealth", 1500, 1200)
print(my_land.area())

marvel = Circle("gol", 5)
print(marvel.area())