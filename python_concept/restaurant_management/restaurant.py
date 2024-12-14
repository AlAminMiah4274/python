from menu import Menu

class Restaurant:
	def __init__(self, name):
		self.name = name
		self.employees = []
		self.menu = Menu()


	def add_employee(self, employee):
		self.employees.append(employee)


	def view_employee(self):
		for emp in self.employees:
			print(f"Name: {emp.name}, Designation: {emp.designation}, Salary: {emp.salary}")


