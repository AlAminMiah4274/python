def square(n):
	return n ** 2

nums = [2, 8, 5, 3, 9]
square_nums = list(map(square, nums))

print(square_nums)