print("Al Amin " + "Miah")
print(405 + 15)
print([10, 78, 50] + [91, 100])


class Person:

	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight

	def eat(self):
		print("The person eats")


class Cricketer(Person):

	def __init__(self, name, age, height, weight, team):
		self.team = team
		super().__init__(name, age, height, weight)


	def eat(self):
		print("Cricketer eats only vegitables")


	def __add__(self, other):
		return self.age + other.age


smith = Cricketer("Steven", 29, 5.9, 70, "Australia")
david = Cricketer("Warner", 29, 5.9, 70, "Australia")

print(smith + david)