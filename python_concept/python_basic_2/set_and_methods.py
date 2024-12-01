# set: unique items collection --->

numbers = [10, 78, 120, 10, 20, 50, 20]
print(numbers)

# items = {10, 20, 10, 10, 78, 120, 10, 20, 50, 20}
# print(items)


numbers_set = set(numbers)
print(numbers_set)

numbers_set.pop()
numbers_set.clear()
print(numbers_set)

# if 120 in numbers_set:
# 	numbers_set.remove(120)
# else:
# 	print("100 Not exist")

# print(numbers_set)

# numbers_set.add(105)
# print(numbers_set)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)


""" Operations in set """
# print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)