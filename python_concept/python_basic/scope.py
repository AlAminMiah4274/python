balance = 3000

def buy_things(item, price):

	"""
	you can access global variable in the local scope
	But to modify the global variable should be called 'global' keyword
	"""

	global balance
	print("balance before buying:", balance)
	balance = balance - price
	print("balance after buying:", balance)

buy_things("sunglass", 1000)