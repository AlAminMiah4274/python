numbers = [14, 100, 54, 100, 79, 100, 25, 100]

numbers.append(1005)
numbers.insert(2, 2005)

if 100 in numbers:
	numbers.remove(100)


if 54 in numbers:
	index = numbers.index(54)
	print("index:", index)


print(numbers[:])
numbers.pop()
# print(numbers.pop())

# numbers.sort(reverse = True)
numbers.sort()
numbers.reverse()

print(numbers[:])