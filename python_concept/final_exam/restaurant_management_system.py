from abc import ABC

class User(ABC):
	def __init__(self, name, email, phone, address):
		self.name = name
		self.email = email
		self.phone = phone
		self.address = address



class Customer(User):
	def __init__(self, name, email, phone, address):
		super().__init__(name, email, phone, address)


	def view_menu(self):
		pass


	def place_order(self):
		pass


	def check_available_balance(self):
		pass

	def view_previous_order(self):
		pass


	def add_balance(self):
		pass




class Admin(User):
	def __init__(self, name, email, phone, address):
		super().__init__(name, email, phone, address)


	