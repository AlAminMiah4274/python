class Laptop:

	def __init__(self, brand, price, color, memory):
		self.brand = brand
		self.price = price
		self.color = color
		self.memory = memory


	def run(self):
		return f"Running laptop: {self.brand}"

	def coding(self):
		return f"Learing python and practicing"



class Phone:

	def __init__(self, brand, price, color, dual_sim):
		self.brand = brand
		self.price = price
		self.color = color
		self.dual_sim = dual_sim


	def run(self):
		return f"Sudhu phone tipa tipi kore"


	def phone_call(self, number, text):
		return f"Sending sms to: {number} with: {text}"



class Camera:

	def __init__(self, brand, price, color, pixel):
		self.brand = brand
		self.price = price
		self.color = color
		self.pixel = pixel


	def run(self):
		return f"Chhobi tulte pare na abar vab ney"


	def change_lense(self):
		pass

