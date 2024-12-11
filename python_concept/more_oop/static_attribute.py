class Shopping:
	cart = []

	def __init__(self, name):
		self.name = name


	def add_to_cart(self, product_name, price, quantity):
		products = {"product_name": product_name, "price": price, "quantity": quantity}
		self.cart.append(products)


shila = Shopping("Shila Islam")
shila.add_to_cart("penti", 150, 3)
shila.add_to_cart("bra", 200, 2)

rahima = Shopping("Angel Rahima")
rahima.add_to_cart("palju", 300, 1)
rahima.add_to_cart("tops", 400, 1)
rahima.add_to_cart("shoes", 180, 1)


print(shila.cart)
print(rahima.cart)

