class Shopping:
	cart = []

	def __init__(self):
		self.name = "jamuna"
		self.location = "bashundhara"

	def purchase(self, item, price, amount):
		remaining_amount = amount - price 
		print(f"buying: {item} for price: {price} and reamining {remaining_amount}")

	@classmethod
	def hudai_dekhi(self, item):
		print("Hudai dekhte aschhi", item)

	@staticmethod
	def multiply(a, b):
		result = a * b
		print(result)




# Shopping.purchase('a', 5, 257, 300)
# mia = Shopping()
# mia.purchase(5, 297, 300)

# mia.hudai_dekhi("shorts")
print(Shopping.cart)
# Shopping.hudai_dekhi("shorts")
Shopping.multiply(4, 5)


"""
static method ---> utility function
class method ----> factory method 
"""