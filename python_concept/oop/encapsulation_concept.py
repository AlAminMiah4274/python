class Bank:

	def __init__(self, holder_name, initial_deposit):
		self.holder_name = holder_name
		self.__balance = initial_deposit



sunderland = Bank("library girl", 15000)

print(sunderland.__balance)