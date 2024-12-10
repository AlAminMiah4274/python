class Person:

	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight

	def eat(self):
		print("vat, mangso")

	def exercise(self):
		raise NotImplementedError
		print("called")


class Cricketer(Person):

	def __init__(self, name, age, height, weight, team):
		self.team = team
		super().__init__(name, age, height, weight)


	def eat(self):
		print("vegitables")

	def exercise(self):
		print("Gym e giye tk khoroch kore gham joray")


	def __add__(self, other):
		return self.age + other.age



stark = Cricketer("Mitchel", 28, 6.7, 70, "Australia")
smith = Cricketer("Stiven", 31, 5.8, 71, "Australia")

# stark.eat()
# stark.exercise()
# print(stark.team)


print(102 + 54)
print("warner" + "smith")
print([12, 31, 58, 10] + [13, 78, 34, 21, 108])
# print(stark + smith)