class Shop:
	shopping_mall = "Jamuna"


	def __init__(self, buyer):
		self.buyer = buyer
		self.cart = []


	def add_to_cart(self, item):
		self.cart.append(item)


jolly = Shop("Joly")
jolly.add_to_cart("guns")
jolly.add_to_cart("pistol")
jolly.add_to_cart("knife")

print(jolly.cart)

lopez = Shop("Jennifer")
lopez.add_to_cart("shoe")
lopez.add_to_cart("purse")
lopez.add_to_cart("phone")

print(lopez.cart)

hamesworth = Shop("chris")
hamesworth.add_to_cart("cap")
hamesworth.add_to_cart("t shirt")
hamesworth.add_to_cart("shorts")

print(hamesworth.cart)