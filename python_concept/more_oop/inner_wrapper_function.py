def double_decker():
	print("this is double decker")

	def inner_function():
		print("hi, from inner function")

		return 2024

	return inner_function


print(double_decker()())


def do_something(work):
	print("work started")
	work()
	print("work ended")

def coding():
	print("coding in Python")


do_something(coding)