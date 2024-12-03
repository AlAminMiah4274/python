def doubled(x):
	return x * 2

result = doubled(420)
# print(result)


double = lambda num : num * 2
add = lambda x, y : x + y

# print(double(420))
# print(add(4, 10))
output = add(52, 19)
# print(output)

multi_parameter = lambda a, b, c, d : (a + b) * (c + d)

response = multi_parameter(4, 21, 3, 5)
# print(response)

numbers = [2, 8, 7, 9, 5, 3, 6]
# print(numbers)
double_nums = list(map(lambda x : x ** x, numbers))
# print(double_nums)

actress = [
	{"name": "Eva Green", "age": 40},
	{"name": "gal gadot", "age" : 36},
	{"name": "natalie portman", "age": 45},
	{"name": "ana de arms", "age": 28},
	{"name": "Jenifer lopez", "age": 40},
	{"name": "angelina jolly", "age": 42}
]

juniors = filter(lambda actor : actor["age"] < 40, actress)
fivers = filter(lambda actor : actor["age"] % 5 == 0, actress)
print(list(fivers))
# print(list(juniors))