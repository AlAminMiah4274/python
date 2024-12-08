# base class, parent class, common attribute + functionality class 
# derived class, child class, uncommon attribute + functionality class 



class Gadget:
	
	def __init__(self, brand, price, color, origin):
		self.brand = brand
		self.price = price
		self.color = color
		self.origin = origin


	def run(self):
		return f"I am using {self.brand}"


class Laptop:

	def __init__(self, memory, ssd):
		self.memory = momory
		self.ssd = ssd


	def coding(self):
		return f"Learing python and practicing"


class Phone(Gadget):

	def __init__(self, brand, price, color, origin, dual_sim):
		self.dual_sim = dual_sim
		super().__init__(brand, price, color, origin)

	def phone_call(self, number, text):
		return f"Sending sms to {number}, text: {text}"


	def __repr__(self):
		return f"from phone class: {self.dual_sim}"



class Camera:

	def __init__(self, pixel):
		self.pixel = pixel


	def change_lense(self):
		pass



my_phone = Phone("Vivo", 15000, "Blue", "China", True)
res = my_phone.phone_call(12457, "hey, I am learing oop using python")
print(my_phone.brand, my_phone.price, my_phone.color, my_phone.origin)
# print(res)