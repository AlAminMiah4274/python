class Bank:

	def __init__(self, balance):
		self.balance = balance
		self.min_withdraw = 100
		self.max_withdraw = 100000


	def get_balance(self):
		return self.balance


	def deposit(self, amount):
		if amount > 0:
			self.balance += amount


	def withdraw(self, amount):
		if amount < self.min_withdraw:
			print(f"Fakir, You can't withdraw less than {self.min_withdraw}")
		elif amount > self.max_withdraw:
			print(f"Bank fakir hoye jabe. You cant't withdraw more than {self.max_withdraw}")
		else:
			self.balance -= amount
			print(f"Here is your money: {amount}")
			print(f"Your balance after withdraw: {self.get_balance()}")


brac = Bank(200000)
brac.deposit(50000)


brac.withdraw(70000)