class Bank:

	def __init__(self, holder_name, initial_deposit):
		self.holder_name = holder_name
		self.__balance = initial_deposit
		self._branch = "Uttara 05"


	def get_balance(self):
		return f"Your Current balance {self.__balance}tk"

	def deposit(self, amount):
		self.__balance += amount
		return f"Your money deposited. Current balance {self.__balance}"

	def withdraw(self, amount):
		if amount > self.__balance:
			return f"Not enough money in your account. Current balance {self.__balance}"
		else:
			self.__balance -= amount
			return f"Here is your money {amount}. Balance after withdraw {self.__balance}"



malkova = Bank("Mia Malkova", 150000)
# print(malkova.get_balance())
# print(malkova.deposit(50000))
print(malkova.withdraw(160000))