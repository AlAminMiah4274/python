from abc import ABC

class User(ABC):
	def __init__(self, name, email, address):
		self.name = name
		self.email = email
		self.address = address



class Customer(User):
	def __init__(self, name, email, address):
		super().__init__(name, email, address)
		self.__wallet = 0
		self.cart = Order()


	def view_menu(self, restaurant):
		restaurant.menu.view_menu()


	def place_order(self, restaurant, item_name, quantity):
		order_price = 0
		for item in restaurant.menu.items:
			if item.name.lower() == item_name.lower():
				order_price = item.price
				item.quantity -= quantity


		order = MenuItem(item_name, order_price, quantity)
		self.cart.add_order(order)


	def check_available_balance(self):
		print(f"You have {self.__wallet} taka")


	def view_previous_order(self):
		self.cart.view_cart()


	def add_balance(self, amount):
		if amount > 0:
			self.__wallet += amount
		else:
			print("amount should not negative")



class Order:
	def __init__(self):
		self.orders = []


	def add_order(self, order):
		self.orders.append(order)


	def view_cart(self):
		print("******** Past Order **********")
		for order in self.orders:
			print(f"Name: {order.name}, Price: {order.price}, Quantity: {order.quantity}")




class Admin(User):
	def __init__(self, name, email, address):
		super().__init__(name, email, address)


	def add_item_to_menu(self, restaurant, item):
		restaurant.menu.add_item(item)


	def add_customer_to_restaurant(self, restaurant, customer):
		restaurant.add_customer(customer)



	def view_customers_of_restaurant(self, restaurant):
		restaurant.view_customers()


	def remove_customer_from_restaurant(self, restaurant, customer_name):
		restaurant.remove_customer(customer_name)


	def remove_item_from_menu(self, restaurant, item_name):
		restaurant.menu.remove_item(item_name)


	def view_items_of_menu(self, restaurant):
		restaurant.menu.view_menu()




class Restaurant:
	def __init__(self, name, address):
		self.name = name
		self.address = address
		self.menu = Menu()
		self.customers = []


	def find_customer(self, customer_name):
		for customer in self.customers:
			if customer.name.lower() == customer_name.lower():
				return customer

		return None


	def add_customer(self, customer):
		self.customers.append(customer)


	def remove_customer(self, customer_name):
		customer = self.find_customer(customer_name)

		if customer:
			self.customers.remove(customer)
			print("customer deleted successfully...")
		else:
			print("customer not found !!")


	def view_customers(self):
		for customer in self.customers:
			print(f"Name: {customer.name}, Email: {customer.email}, Address: {customer.address}")
		



class Menu:
	def __init__(self):
		self.items = []


	def find_item(self, item_name):
		for item in self.items:
			if item.name.lower() == item_name.lower():
				return item

		return None


	def add_item(self, item):
		self.items.append(item)


	def remove_item(self, item_name):
		item = self.find_item(item_name)

		if item:
			self.items.remove(item)
			print("item deleted successfully...")
		else:
			print("item not found !!")


	def view_menu(self):
		print("********** Menu ************")
		print(f"Name\tPrice\tQuantity")
		for item in self.items:
			print(f"{item.name}\t{item.price}\t{item.quantity}")



class MenuItem:
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity



mayer_hotel = Restaurant("Mayer Dua Hotel", "uttara")

def customer_menu():
	name = input("Enter your name : ")
	email = input("Enter your email : ")
	address = input("Enter your address : ")

	customer = Customer(name, email, address)

	while True:
		print(f"Welcome {customer.name}")
		print("1. See Menu : ")
		print("2. Check Balance : ")
		print("3. Place Order : ")
		print("4. See Previous Order : ")
		print("5. Add Balance : ")
		print("6. Exit : ")

		choice = int(input("Enter your choice : "))

		if choice == 1:

			customer.view_menu(mayer_hotel)

		elif choice == 2:

			customer.check_available_balance()

		elif choice == 3:
			

			item_name = input("Enter item name : ")
			item_quantity = int(input("Enter item quantity : "))

			customer.place_order(mayer_hotel, item_name, item_quantity)

		elif choice == 4:

			customer.view_previous_order()

		elif choice == 5:

			amount = int(input("Enter your amount : "))

			customer.add_balance(amount)

		elif choice == 6:
			break
		else:
			print("invalid input !!")


def admin_menu():
	name = input("Enter your name : ")
	email = input("Enter your email : ")
	address = input("Enter your address : ")

	admin = Admin(name, email, address)

	while True:

		print(f"Welcome {admin.name}")
		print("1. Add New Item : ")
		print("2. Delete Item : ")
		print("3. See Menu : ")
		print("4. Add Customer : ")
		print("5. Delete Customer : ")
		print("6. See Customers : ")
		print("7. Exit : ")

		choice = int(input("Enter your choice : "))

		if choice == 1:

			item_name = input("Enter item name : ")
			item_price = int(input("Enter item price : "))
			item_quantity = int(input("Enter item quantity : "))

			item = MenuItem(item_name, item_price, item_quantity)

			admin.add_item_to_menu(mayer_hotel, item)

		elif choice == 2:

			item_name = input("Enter item name : ")
			admin.remove_item_from_menu(mayer_hotel, item_name)

		elif choice == 3:

			admin.view_items_of_menu(mayer_hotel)

		elif choice == 4:

			customer_name = input("Enter customer name : ") 
			customer_email = input("Enter customer email : ") 
			customer_address = input("Enter customer address : ")

			customer = Customer(customer_name, customer_email, customer_address) 
			admin.add_customer_to_restaurant(mayer_hotel, customer)

		elif choice == 5:

			customer = input("Enter customer name : ")
			admin.remove_customer_from_restaurant(mayer_hotel, customer)

		elif choice == 6:
			
			admin.view_customers_of_restaurant(mayer_hotel)

		elif choice == 7:
			break
		else:
			print("invalid input")


while True:
	print("Welcome !!")
	print("1. Customer : ")
	print("2. Admin : ")
	print("3. Exit : ")

	choice = int(input("Enter your choice : "))

	if choice == 1:

		customer_menu()

	elif choice == 2:

		admin_menu()

	elif choice == 3:
		break
	else:
		print("invalid input")