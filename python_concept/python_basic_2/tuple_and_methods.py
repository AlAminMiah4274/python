def multiple():
	return 3, 5

# print(multiple())


things = "pen", "pencil", "tripod", "airpod"
# print(things)


for thing in things:
	print(thing, end = " ")

print()
print(things[::-1])

on_table = ("book", "pen", "laptop", "keyboared", "mouse")
print(on_table)


if "mouse" in on_table:
	print("exists")


many_things = ([1, 2, 3, 4, 5], "Book", "Pen", (8, 4, 5, 7, 9), {"name" : "Al Amin Miah", "age" : 24, "Address" : "Uttara"})

many_things[0][3] = 800

print(many_things)