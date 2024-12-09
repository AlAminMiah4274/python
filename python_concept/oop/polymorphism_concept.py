class Animal:

	def __init__(self, name):
		self.name = name


	def make_sound(self):
		print("the animal is making some sound")


class Cat(Animal):

	def __init__(self, name):
		self.name = name
		super().__init__(name)


	def make_sound(self):
		print("Meow meow")


class Dog(Animal):

	def __init__(self, name):
		self.name = name 
		super().__init__(name)

	def make_sound(self):
		print("Gheu gheu")


class Goat(Animal):

	def __init__(self, name):
		self.name = name
		super().__init__(name)

	def make_sound(self):
		print("u ma bo bo")


don = Cat("The real don")
# don.make_sound()

shephard = Dog("Bangla kutta")
# shephard.make_sound()


mess = Goat("LM10")
# mess.make_sound()

less = Goat("ney mama")
# less.make_sound()


animals = [don, shephard, mess, less]
for animal in animals:
	animal.make_sound()