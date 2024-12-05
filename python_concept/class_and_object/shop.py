class Shop:
	cart = []

	def __init__(self, buyer):
		self.buyer = buyer

	def add_to_cart(self, item):
		self.cart.append(item)



lawrence = Shop("lawrence")
lawrence.add_to_cart("bra")
lawrence.add_to_cart("penti")
lawrence.add_to_cart("sex toy")

print(lawrence.cart)

hamesworth = Shop("Hamesworth")
hamesworth.add_to_cart("cap")
hamesworth.add_to_cart("t shirt")
hamesworth.add_to_cart("shorts")

print(hamesworth.cart)