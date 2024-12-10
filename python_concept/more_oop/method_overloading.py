class Calculator:

	def add(self, *args):
		self.args = args

		sum = 0
		for arg in args:
			sum += arg 
		return sum

	def mul(self, *args):
		self.args = args

		result = 1
		for arg in args:
			result *= arg
		return result



rahim = Calculator()
print(rahim.add(45, 10, 30, 38))
print(rahim.mul(10, 30, 1000, 15))



# def add(*args):
# 	sum = 0
# 	print(args)
# 	for arg in args:
# 		sum += arg
# 	print(sum)


# add(15, 48, 20)


"""
Overloading in Python refers to the ability to define multiple behaviors for a single operation, 
such as a function, method, or operator, depending on the context or the type of the arguments provided. 
Python supports overloading primarily through method overriding and operator overloading, using magic methods. 

Method Overloading: 
Method overloading allows a class to have multiple methods with the same name but different arguments. 
While Python does not directly support method overloading like some other languages (e.g., Java or C++), 
you can achieve similar behavior using default arguments or variable-length arguments (*args and **kwargs).
"""