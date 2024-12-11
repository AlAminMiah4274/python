class User:

	def __init__(self, name, age, money):
		self._name = name
		self._age = age
		self.__money = money


	@property
	def age(self):
		return self._age

	@property
	def salary(self):
		return self.__money

	@salary.setter 
	def salary(self, value):
		if value < 0:
			return "Amount should not negative"
		self.__money += value


sumsu = User("kopa", 21, 30000)

print(sumsu.age)
print(sumsu.salary)

sumsu.salary = 5200
print(sumsu.salary)


"""
Property decorator can convert a method into an attribute
"""