class Phone:
	menufacturer = "China"

	def __init__(self, owner, brand, price):
		self.owner = owner
		self.brand = brand
		self.price = price

	def send_sms(self, phone, sms):
		text = f"sending to {pohne} {sms}"

		return text


my_phone = Phone("Al Amin Miah", "Vivo", 15000)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone("Lisa", "Apple", 150000)
print(her_phone.owner, her_phone.brand, her_phone.price)

mom_phone = Phone("Joya", "Nokia", 2300)
print(mom_phone.owner, mom_phone.brand, mom_phone.price)