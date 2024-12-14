from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurant import Restaurant
from users import Customer, Admin, Employee


mayer_hotel = Restaurant("Mayer Dua Hotel")

def customer_menu():
	name = input("Enter your name : ")
	email = input("Enter your email : ")
	phone_no = input("Enter your phone_no : ")
	address = input("Enter your address : ")

	customer = Customer(name = name, email = email, phone_no = phone_no, address = address)

	while True:
		print(f"Welcome {customer.name} !!")
		print("1. View menu")
		print("2. Add item to cart")
		print("3. View cart")
		print("4. Pay bill")
		print("5. Exit")

		choice  = int(input("Enter your choice : "))

		if choice == 1:
			customer.view_menu(mayer_hotel)
		elif choice == 2:
			item_name = input("Enter your item name : ")
			item_quantity = int(input("Enter your item quantity : "))
			customer.add_to_cart(mayer_hotel, item_name, item_quantity)
		elif choice == 3:
			customer.view_cart()
		elif choice == 4:
			customer.pay_bill()
		elif choice == 5:
			break
		else:
			print("Invalid input")


def admin_menu():
	name = input("Enter your name : ")
	email = input("Enter your email : ")
	phone_no = input("Enter your phone_no : ")
	address = input("Enter your address : ")

	admin = Admin(name = name, email = email, phone_no = phone_no, address = address)


	while True:
		print(f"Welcome {admin.name} !!")
		print("1. Add new item")
		print("2. Add new employee")
		print("3. View employees")
		print("4. View items")
		print("5. Delete item")
		print("6. Exit")

		choice = int(input("Enter your choice : "))

		if choice == 1:
			item_name = input("Enter item name : ")
			item_price = int(input("Enter item price : "))
			item_quantity = int(input("Enter item quantity : "))
			item = FoodItem(item_name, item_price, item_quantity)

			admin.add_new_item(mayer_hotel, item)
		elif choice == 2:
			emp_name = input("Enter employee name : ")
			emp_email = input("Enter employee email : ")
			emp_phone_no = input("Enter employee phone no : ")
			emp_address = input("Enter employee address : ")
			emp_age = input("Enter employee age : ")
			emp_designation = input("Enter employee designation : ")
			emp_salary = input("Enter employee salary : ")
			employee = Employee(emp_name, emp_email, emp_phone_no, emp_address, emp_age, emp_designation, emp_salary)

			admin.add_employee(mayer_hotel, employee)
		elif choice == 3:
			admin.view_employee(mayer_hotel)
		elif choice == 4:
			admin.view_menu(mayer_hotel)
		elif choice == 5:
			item_name = input("Enter item name : ")
			admin.remove_item(mayer_hotel, item_name)
		elif choice == 6:
			break
		else:
			print("invalid input")



while True:
	print("Welcome !!")
	print("1. Customer")
	print("2. Admin")
	print("3. Exit")

	choice = int(input("Enter your choice : "))

	if choice == 1:
		customer_menu()
	elif choice == 2:
		admin_menu()
	elif choice == 3:
		break
	else:
		print("Invalid input")