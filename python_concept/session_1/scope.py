money_in_pocket = 1000000

def buy_things(things_name, amount):
	global money_in_pocket
	remaining_money = money_in_pocket - amount
	# money_in_pocket = money_in_pocket - amount
	money_in_pocket = remaining_money

	print("inside:", money_in_pocket)


buy_things("House", 800000)
print("outside:", money_in_pocket)