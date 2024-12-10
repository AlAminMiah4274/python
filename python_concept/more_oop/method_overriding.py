class Person:

	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address


	def profession(self):
		print("I am doing nothing")



class Athletes(Person):

	def __init__(self, name, age, address, type):
		self.type = type
		super().__init__(name, age, address)

	# this method is overriding the profession method in Person class 
	def profession(self):
		print(f"{self.type}")


messi = Athletes("LM10", 38, "Miami", "Footballer")
messi.profession()


""" 
Overriding: Replacing a parent class's method with a new implementation in the subclass.

Overriding in Python refers to the ability of a subclass to provide a specific implementation for a method that is already defined in its parent class. 
When a method in the subclass has the same name and parameters as a method in the parent class, 
the method in the subclass "overrides" the method in the parent class.
"""