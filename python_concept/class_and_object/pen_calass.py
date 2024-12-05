class Pen:

	def __init__(self, brand, color, price):
		self.brand = brand
		self.color = color
		self.price = price


	def paragraph(self, name, text):
		line = f"A paragraph about {name}: {text}"

		return line



my_pen = Pen("High School", "Red", 5)
print(my_pen.brand, my_pen.color, my_pen.price)

her_pen = Pen("All Time", "pink", 6)
print(her_pen.brand, her_pen.color, her_pen.price)

his_pen = Pen("i-teen", "green", 10)
print(his_pen.brand, his_pen.color, his_pen.price)


print(my_pen.paragraph("Cow", "The cow is a domestic animal. It has four legs, one tail. It eats grass. It gives us milk to drink"))