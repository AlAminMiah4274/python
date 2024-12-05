class Calculator:
	brand = "Casio MS990"

	def add(self, num1, num2):
		return num1 + num2


	def deduct(self, num1, num2):
		return num1 - num2


	def multipy(self, num1, num2):
		return num1 * num2


	def divide(self, num1, num2):
		return num1 // num2



money = Calculator()

# result = money.add(15, 31)
# result = money.deduct(80, 13)
# result = money.multipy(3, 7)
result = money.divide(78, 20)
print(result)