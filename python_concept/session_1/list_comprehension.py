numbers = [1, 2, 5, 3]

# for num in numbers:
# 	square = num ** 2


# for i in range(len(numbers)):
# 	numbers[i] = numbers[i] ** 2

# print(numbers)


square_nums = [number ** 2 for number in numbers]

# print(square_nums)

nums = [1, 2, 3, 4, 5, 6]

# odd_nums = []
# for num in nums:
# 	if num % 2 == 1:
# 		odd_nums.append(num)

# print(odd_nums)


odd_nums = [num for num in nums if num % 2 == 1 and num > 1]
print(odd_nums)