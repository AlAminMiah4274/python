def call():
	print("Calling someone I don't know.")

	return "calling loved one"


class Phone:
	price = 15000
	brand = "Vivo"
	color = "Blue"

	def call(self):
		print("Calling one person.")


	def send_sms(self, phone, sms):
		text = f"Sending sms to: {phone} and message: {sms}"
		print("result of self:", self)

		return text


my_phone = Phone()
your_phone = Phone()

num = your_phone.send_sms(993347, "this my phone number")
print(num)

# print(my_phone.price)
# my_phone.call()

# call()
# print(call())

result = my_phone.send_sms(4578, "I forgot to miss you.")
print(result)