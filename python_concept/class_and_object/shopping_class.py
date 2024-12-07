class Shopping:

	def __init__(self, name):
		self.name = name
		self.cart = []


	def add_to_cart(self, item, price, quantity):
		product = {"item": item, "price": price, "quantity": quantity}
		self.cart.append(product)


	def checkout(self, amount):
		total = 0
		for item in self.cart:
			total += item["price"] * item["quantity"]

		if amount < total:
			print(f"Please provide {total - amount} more")
		else:
			extra = amount - total
			print(f"Here is your items and change {extra}")


	def remove_item(self, item_name):
		for item in self.cart:
			if item_name == item["item"]:
				self.cart.remove(item)


messi = Shopping("messi")
messi.add_to_cart("ball", 1500, 3)
messi.add_to_cart("boot", 1200, 5)
messi.add_to_cart("t shirt", 1000, 5)
messi.add_to_cart("shorts", 1100, 5)

# messi.checkout(25000)

messi.remove_item("shorts")

for item in messi.cart:
	print(item)