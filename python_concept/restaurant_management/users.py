"""
Users are:
Admin
Customer 
Employee

Common characteristics of the users:
name
phone no 
email
address
"""

from abc import ABC
from orders import Order


class User(ABC):
	def __init__(self, name, email, phone_no, address):
		self.name = name
		self.email = email
		self.phone_no = phone_no
		self.address = address



class Customer(User):
	def __init__(self, name, email, phone_no, address):
		super().__init__(name, email, phone_no, address)
		self.cart = Order()


	def view_menu(self, restaurant):
		restaurant.menu.show_menu()


	def add_to_cart(self, restaurant, item_name, quantity):
		item = restaurant.menu.find_item(item_name)
		if item:
			if quantity > item.quantity:
				print("Item quantity exceeded !!")
			else:
				item.quantity = quantity
				self.cart.add_item(item)
				print("item added")
		else:
			print("item not found")


	def view_cart(self):
		print("********* Cart **********")
		print("Name\tPrice\tQuantity")
		for item, quantity in self.cart.items.items():
			print(f"{item.name}\t{item.price}\t{quantity}")

		print(f"Total Price: {self.cart.total_price}")


	def pay_bill(self):
		print(f"Total {self.cart.total_price} paid successfully")
		self.cart.clear()




class Employee(User):
	def __init__(self, name, email, phone_no, address, age, designation, salary):
		super().__init__(name, email, phone_no, address)
		self.age = age
		self.designation = designation
		self.salary = salary



class Admin(User):
	def __init__(self, name, email, phone_no, address):
		super().__init__(name, email, phone_no, address)
		# self.employees = []


	# def add_employee(self, name, email, phone_no, address, age, designation, salary):
	# 	employee = Employee(name, email, phone_no, address, age, designation, salary)
	# 	self.employees.append(employee)

	def add_employee(self, restaurant, employee):
		restaurant.add_employee(employee)


	# def view_employee(self):
	# 	for emp in self.employees:
	# 		print(f"Name: {emp.name}, Designation: {emp.designation}, Salary: {emp.salary}")

	def view_employee(self, restaurant):
		restaurant.view_employee()


	def add_new_item(self, restaurant, item):
		restaurant.menu.add_menu_item(item)


	def view_menu(self, restaurant):
		restaurant.menu.show_menu()


	def remove_item(self, restaurant, item_name):
		restaurant.menu.remove_item(item_name)