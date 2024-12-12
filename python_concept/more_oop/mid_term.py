class Library:

	book_list = []

	@classmethod
	def entry_book(self, book_id, title, author, availability):
		book = {"book_id": book_id, "title": title, "author": author, "availability": availability}
		self.book_list.append(book)



class Book(Library):

	def __init__(self, book_id, title, author, availability):
		self.__book_id = book_id
		self.__title = title
		self.__author = author
		self.__availability = availability
		super().entry_book(book_id, title, author, availability)


	@classmethod
	def borrow_book(self, book_name):
		# print(Library.book_list)

		for item in Library.book_list:
			if book_name == item["title"] and item["availability"] == True:
				item["availability"] = False
				print(f"{book_name} successfully borrowed")
			elif book_name == item["title"] and item["availability"] != True:
				print("You've already borrowed this book. Try another")


	@classmethod
	def return_book(self, book_name):

		for item in Library.book_list:
			if book_name == item["title"] and item["availability"] == False:
				item["availability"] = True
				print(f"{book_name} successfully returned")	
			elif book_name == item["title"] and item["availability"] != False:
				print("It's not right book you've borrowed")


	@classmethod
	def view_book_info(self):
		# print(Library.book_list)

		for item in Library.book_list:
			print(item)






amin = Book(101, "atomic habits", 'james clear', True)
amin = Book(102, "atomic", 'clear', True)
amin = Book(103, "habits", 'james', True)
amin = Book(104, "a habits", 'j clear', True)

# print(amin.borrow_book())
# amin.borrow_book("habits")
# amin.return_book("habits")
# amin.view_book_info()



while True:
	print("""
	1. View All Books
	2. Borrow Book
	3. Return Book
	4. Exit
	""")


	user_input = int(input("Please press only number here: "))


	if user_input == 1:
		Book.view_book_info()


	if user_input == 2:
		book_name = input("Enter book_name: ")
		Book.borrow_book(book_name)


	if user_input == 3:
		book_name = input("Enter book_name: ")
		Book.return_book(book_name)


	if user_input == 4:
		break

