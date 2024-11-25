# default parameter value, *args, **kwargs 


# default parameter value: 
def sum(num = 0, num2 = 0):
	result = num + num2

	return result

total = sum(45, 20)
# print("total:", total)


# *args: 
def all_sum(*args):
	print(args)
	sum = 0
	for arg in args:
		sum += arg
	return sum

total = all_sum(48, 54, 10, 70, 80)
print("Total args:", total)