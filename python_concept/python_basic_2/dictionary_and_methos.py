person = {"Name": "Kala Pakhi", "Address": "Kalipur", "Age": 20, "Job": "Facebooker"}
# print(person)
# print(person["Job"])

# print(person.keys())
# print(person.values())

for key, value in person.items():
	# print(key, value)

	if "Job" == key:
		print(value)


person["Language"] = "Python"
person["Name"] = "Sada Pakhi"

del person["Age"]

print(person)