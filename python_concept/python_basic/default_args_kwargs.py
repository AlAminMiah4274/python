# default parameter value, *args, **kwargs 


# default parameter value: 
def sum(num = 0, num2 = 0):
	result = num + num2

	return result

total = sum(45, 20)
# print("total:", total)


# *args: 
def all_sum(*args):
	# print(args)
	sum = 0
	for arg in args:
		sum += arg
	return sum

total = all_sum(48, 54, 10, 70, 80)
# print("Total args:", total)

# kwargs: 
def full_name(first, last):
	name = f"{first} {last}"
	return name

# inorder 
# person_name = full_name("Alu", "Kodu")

person_name = full_name(last="Kodu", first="Alu")
# print(person_name)


def famous_name(**kwargs):
	for key, value in kwargs.items():
		print(key, value)

	print(kwargs["last"])

famous_name(first = "Taher", last = "Ali", title = "Taheri", additional = "Hujur")


# return multiple value:
def a_lot(num1, num2):
	add = num1 + num2
	subtract = num1 - num2
	multiply = num1 * num2
	divide = num1 / num2

	# return [add, subtract, multiply, divide]
	return add, subtract, multiply, divide

print(a_lot(12, 3))