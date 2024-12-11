import math

def timer(function):

	def inner(*args, **kwargs):
		print("inner started")
		function(*args, **kwargs)
		print("inner ended")

	return inner

@timer
def get_factorial(n):
	result = math.factorial(n)
	print(f"factorial of {n}:", result)

get_factorial(5)


# def get_factorial(n):
# 	result = math.factorial(n)
# 	print(f"factorial of {n}:", result)

# timer(get_factorial)(n = 5)





"""
DECORATOR: Decorator is just a function that takes another function as an argument


Programmer must read books: 
https://www.alexhyett.com/books-for-programmers/ 
"""