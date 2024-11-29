def square(n):
	return n * n

value = square(5)
print(value)


def add(a, b):
	return a + b

response_add = add(10, 21)
print(response_add)


def student_marks(name, *args):
	sum = 0
	for num in args:
		sum += num

	# print(f"Name: {name} Marks: {sum}")
	# return name, sum
	return [name, sum]


# response_student_marks = student_marks("Al Amin Miah", 75, 80, 81, 92, 94)
# print(response_student_marks)

name, sum = student_marks("Al Amin Miah", 75, 80, 81, 92, 94)
print(f"Name: {name}, Marks: {sum}")


def student_address(**kwargs):
	print(kwargs)


student_address(Name="Al Amin Miah", House_no="11/14", Area="Nolbhog", Thana="Uttara", District="Dhaka")