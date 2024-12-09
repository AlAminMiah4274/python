from abc import ABC, abstractmethod

class Animal(ABC):

	@abstractmethod
	def eat(self):
		print("I eat grass")

	@abstractmethod
	def move(self):
		print("I am going to somewhere")


class Monkey(Animal):
	def __init__(self, name):
		self.name = name 
		super().__init__()

	def eat(self):
		print("Hey nana, I eat banana")

	def move(self):
		print("Hanging on the branches")


lyka = Monkey("lucky")
lyka.eat()
