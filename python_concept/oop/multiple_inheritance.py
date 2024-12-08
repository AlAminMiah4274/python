class Family:

	def __init__(self, address):
		self.address = address


	def __repr__(self):
		return f"{self.address}"


class School:

	def __init__(self, id, level):
		self.id = id
		self.level = level

	def __repr__(self):
		return f"{self.id} {self.level}"


class Sports:

	def __init__(self, game):
		self.game = game


	def __repr__(self):
		return f"{self.game}"


class Student(Family, School, Sports):

	def __init__(self, name, address, id, level, game):
		self.name = name
		Family.__init__(self, address)
		School.__init__(self, id, level)
		Sports.__init__(self, game)


	def __repr__(self):
		return f"{self.name} {Family.__repr__(self)} {School.__repr__(self)} {Sports.__repr__(self)}"



mia = Student("Malkova", "Los Angels", 1001, 8, "Porn")
print(mia)